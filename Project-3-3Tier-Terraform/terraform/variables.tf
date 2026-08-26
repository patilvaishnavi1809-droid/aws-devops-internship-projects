variable "project_name" {
  type    = string
  default = "three-tier-app"
}

variable "aws_region" {
  type    = string
  default = "ap-south-1"
}

variable "vpc_cidr" {
  type    = string
  default = "10.0.0.0/16"
}

variable "public_subnet_cidrs" {
  type    = list(string)
  default = ["10.0.1.0/24", "10.0.2.0/24"]
}

variable "private_subnet_cidrs" {
  type    = list(string)
  default = ["10.0.11.0/24", "10.0.12.0/24"]
}

variable "azs" {
  type    = list(string)
  default = ["ap-south-1a", "ap-south-1b"]
}

variable "key_name" {
  type    = string
  default = "your-key-pair"
}

variable "web_ami_id" {
  type    = string
  default = "ami-0c2b8ca1dad447f8a"
}

variable "db_password" {
  type      = string
  sensitive = true
}
