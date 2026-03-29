terraform {
  backend "s3" {
    bucket = "shishir-panchase-terraform-state"
    key    = "production/terraform.tfstate"
    region = "us-east-1"
  }
}