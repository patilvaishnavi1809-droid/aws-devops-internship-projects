# AWS Elastic Beanstalk + RDS MySQL Project

## Project Overview

This project demonstrates deploying a Node.js web application using AWS Elastic Beanstalk with Amazon RDS MySQL.

The project also includes:

- Amazon EC2
- Amazon RDS MySQL
- AWS Systems Manager Parameter Store
- IAM Role
- Amazon CloudWatch
- EC2-to-RDS connectivity
- Database read/write testing
- Secure credential management

## Architecture

```text
AWS Elastic Beanstalk
        |
        v
Node.js Web Application
        |
        v
Amazon RDS MySQL
        ^
        |
EC2 Instance
        |
MySQL Client

---

# Project Screenshots

## 1. Create Application in Elastic Beanstalk

![Create Application](screenshots/Application-Create%20in%20EB%20Project-1.png)

## 2. Elastic Beanstalk Environment Running

![Elastic Beanstalk Environment Running](screenshots/EB-Env-Running-Project%201%20.png)

## 3. EC2 SSM IAM Role

![EC2 SSM IAM Role](screenshots/EC2-SSM-IAM-ROLE-Project%201.png)

## 4. Elastic Beanstalk Environment Setup

![Elastic Beanstalk Environment Setup](screenshots/Elastic-Beanstalk-ENV-Setup%20Project-1.png)

## 5. MySQL Client Installation

![MySQL Client Installation](screenshots/MYSQL-Client%20installed-Project%201.png)

## 6. RDS Creation

![RDS Creation](screenshots/RDS-Creating-project%201%20.png)

## 7. RDS VPC Verification

![RDS VPC Verification](screenshots/RDS-VPC%20Verification-Project%201.png)

## 8. RDS Read and Write Test

![RDS Read Write Test](screenshots/RDS-read-write-test-Project%201.png)

## 9. SSM Parameter Store

![SSM Parameter Store](screenshots/SSM-parameters-from-Project%201.png)

## 10. Sample Web Application

![Sample Web Application](screenshots/Sampel-Web-application-PROJECT%201.png)

## 11. CloudWatch RDS CPU Monitoring

![CloudWatch RDS CPU Monitoring](screenshots/cloudwatch-rds-cpu-Project%201.png)

## 12. Elastic Beanstalk, RDS and EC2 Running

![Elastic Beanstalk RDS EC2 Running](screenshots/eb-rds-ec2%20running-Project%201%20.png)

## 13. EC2 Connected to RDS MySQL

![EC2 RDS MySQL Connected](screenshots/ec2-rds-mysql%20connected-project%201%20.png)

## 14. Parameter Store Credentials

![Parameter Store Credentials](screenshots/parameter-store-credentials-Project%201.png)

## 15. RDS Database Verification

![RDS Database Verification](screenshots/rds-db%20verification-project%201.png)

## 16. RDS Secure Test Script

![RDS Secure Test Script](screenshots/rds-secure-test-script-project%201.png)

---

# Key Learning Outcomes

- Deployed a Node.js application using AWS Elastic Beanstalk.
- Integrated Amazon RDS MySQL with the application.
- Configured EC2 connectivity to RDS.
- Installed and used the MySQL client.
- Tested database read/write operations.
- Stored database credentials using AWS Systems Manager Parameter Store.
- Configured IAM roles.
- Monitored RDS using Amazon CloudWatch.
- Verified communication between EC2 and RDS.