#!/bin/bash
# EC2 user-data script (alternative to Ansible) for the Web Tier
yum update -y
yum install -y nginx
systemctl enable nginx
systemctl start nginx
echo "<h1>Web tier is up - replace with registration.html via Ansible</h1>" > /usr/share/nginx/html/index.html
