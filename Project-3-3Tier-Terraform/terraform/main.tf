terraform {
  required_version = ">= 1.5"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

module "vpc" {
  source                = "./modules/vpc"
  project_name          = var.project_name
  vpc_cidr               = var.vpc_cidr
  public_subnet_cidrs   = var.public_subnet_cidrs
  private_subnet_cidrs  = var.private_subnet_cidrs
  azs                    = var.azs
}

module "web_ec2" {
  source             = "./modules/ec2"
  instance_name      = "${var.project_name}-web"
  ami_id             = var.web_ami_id
  subnet_id          = module.vpc.public_subnet_ids[0]
  security_group_id  = module.vpc.web_sg_id
  key_name           = var.key_name
  assign_public_ip   = true
  user_data          = file("${path.module}/../ansible/templates/web_userdata.sh")
}

module "app_ec2" {
  source             = "./modules/ec2"
  instance_name      = "${var.project_name}-app"
  ami_id             = var.web_ami_id
  subnet_id          = module.vpc.private_subnet_ids[0]
  security_group_id  = module.vpc.app_sg_id
  key_name           = var.key_name
  assign_public_ip   = false
}

module "rds" {
  source                = "./modules/rds"
  project_name          = var.project_name
  private_subnet_ids    = module.vpc.private_subnet_ids
  db_security_group_id  = module.vpc.db_sg_id
  db_password           = var.db_password
}
