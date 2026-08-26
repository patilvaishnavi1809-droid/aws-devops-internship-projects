#!/bin/bash
# Launch an EC2 instance WITHOUT the required tags -> should FAIL
# if the tag policy / SCP is correctly enforced.

aws ec2 run-instances \
  --image-id ami-0c2b8ca1dad447f8a \
  --instance-type t2.micro \
  --key-name your-key-pair \
  --count 1

# Expected output:
# An error occurred (UnauthorizedOperation) when calling the RunInstances operation:
# You are not authorized to perform this operation. Encoded authorization
# failure message ...
