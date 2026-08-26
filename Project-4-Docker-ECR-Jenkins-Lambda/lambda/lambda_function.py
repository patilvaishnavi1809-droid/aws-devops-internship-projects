"""
Lambda function triggered automatically after a Docker image is pushed to ECR.

Trigger options (pick one):
  1. EventBridge rule listening for the "ECR Image Action" event
     (source: aws.ecr, detail-type: "ECR Image Action", action-type: PUSH)
  2. A direct 'aws lambda invoke' call from the last Jenkins pipeline stage

This function logs the push details to DynamoDB and sends an SNS notification.
"""
import json
import os
import datetime
import boto3

dynamodb = boto3.resource("dynamodb")
sns = boto3.client("sns")

TABLE_NAME = os.environ.get("DYNAMODB_TABLE", "ecr-push-log")
SNS_TOPIC_ARN = os.environ.get("SNS_TOPIC_ARN", "")


def lambda_handler(event, context):
    # Support both EventBridge-triggered events and direct Jenkins invocations
    detail = event.get("detail", event)
    repository = detail.get("repository", detail.get("repository-name", "unknown"))
    image_tag = detail.get("image_tag", detail.get("image-tag", "unknown"))
    timestamp = datetime.datetime.utcnow().isoformat()

    # 1. Log to DynamoDB
    table = dynamodb.Table(TABLE_NAME)
    table.put_item(Item={
        "repository": repository,
        "image_tag": image_tag,
        "pushed_at": timestamp
    })

    # 2. Notify via SNS (optional but recommended)
    if SNS_TOPIC_ARN:
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject=f"New image pushed: {repository}:{image_tag}",
            Message=f"Repository: {repository}\nTag: {image_tag}\nPushed at: {timestamp}"
        )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Logged image push successfully",
            "repository": repository,
            "image_tag": image_tag
        })
    }
