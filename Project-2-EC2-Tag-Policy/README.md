# Project 2 - EC2 Instance Launch Using Tag Policy

## Project Overview

This project demonstrates enforcing mandatory tags for Amazon EC2 instances using an AWS policy-based approach.

The project verifies EC2 instance launch behavior when required tags are missing and when the required tags are provided.

## Objective

- Configure mandatory EC2 tagging.
- Define the required tag policy.
- Attempt to launch an EC2 instance without the required tag.
- Verify the rejection of the EC2 launch request.
- Launch an EC2 instance with the required tag.
- Verify successful EC2 instance creation.


## Required Tag

| Key | Value |
|---|---|
| Environment | Test |

## Project Screenshots

### 1. AWS Console Region

![AWS Console Region](screenshots/aws-console-region-project%202.png)

### 2. Required Tags

![Required Tags](screenshots/required-tags-project%202.png)

### 3. Tag Policy JSON

![Tag Policy JSON](screenshots/tag-policy-json-project%202.png)

### 4. Valid Tag Policy JSON

![Valid Tag Policy JSON](screenshots/tag-policy-valid-json-project%202.png)

### 5. EC2 Tags Policy Created

![EC2 Tags Policy Created](screenshots/policy-ec2-tags-created-project%202.png)

### 6. Tag Policies Enabled

![Tag Policies Enabled](screenshots/tag-policies-enabeld-project%202%20.png)

### 7. Launch EC2 Without Required Tags

![Launch EC2 Without Tags](screenshots/ec2-launch-instance-without-tags-project%202.png)

### 8. EC2 Launch Rejected Without Required Tags

![EC2 Launch Rejected](screenshots/ec2-without-tags-denied-project%202.png)

The EC2 launch request was rejected when the required tag was not provided.

### 9. EC2 Launch With Required Tags

![EC2 Launch With Required Tags](screenshots/ec2-with-required-tags-success-project%202.png)

The EC2 instance launch was successful after the required tag was provided.

