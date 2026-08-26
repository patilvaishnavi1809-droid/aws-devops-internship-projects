#!/bin/bash
# Launch an EC2 instance WITH all required tags -> should SUCCEED

aws ec2 run-instances \
  --image-id ami-0c2b8ca1dad447f8a \
  --instance-type t2.micro \
  --key-name your-key-pair \
  --tag-specifications 'ResourceType=instance,Tags=[
      {Key=Name,Value=Rahul},
      {Key=emailID,Value=rahul@example.com},
      {Key=phoneNo,Value=9999999999},
      {Key=Place,Value=Pune}
  ]' \
  --count 1
