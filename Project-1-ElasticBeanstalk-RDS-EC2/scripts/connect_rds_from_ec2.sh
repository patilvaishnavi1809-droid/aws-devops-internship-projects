#!/bin/bash
# ---------------------------------------------------------------------------
# Run this script on the standalone EC2 instance (NOT the Beanstalk instance)
# to install a MySQL client and connect to the RDS database that Elastic
# Beanstalk provisioned.
# ---------------------------------------------------------------------------

# 1. Update packages and install the MySQL client
sudo yum update -y
sudo yum install -y mysql

# 2. Connect to the RDS instance
#    Replace the placeholders below with the values shown in:
#    Elastic Beanstalk Console -> Configuration -> Database
RDS_ENDPOINT="your-rds-endpoint.xxxxxxxx.ap-south-1.rds.amazonaws.com"
RDS_PORT="3306"
RDS_USER="ebroot"
RDS_DB="ebdb"

mysql -h "$RDS_ENDPOINT" -P "$RDS_PORT" -u "$RDS_USER" -p "$RDS_DB"

# Once connected, you can test with:
#   SHOW DATABASES;
#   SHOW TABLES;
