terraform {
  backend "s3" {
    bucket         = "terraform-state-mybucket07"
    key            = "terraform/state.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-lock"
  }
	}
