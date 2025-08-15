terraform {
  required_version = ">= 1.5.0"
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

resource "aws_s3_bucket" "this" {
  bucket = var.bucket_name
}

variable "aws_region" {
  type        = string
  description = "AWS region"
  default     = "us-east-1"
}

variable "bucket_name" {
  type        = string
  description = "S3 bucket name"
}

output "bucket_id" {
  value = aws_s3_bucket.this.id
}