provider "aws" {
  region = var.region
}

module "infrastructure" {
  source      = "./infrastructure"
  domain_name = var.domain_name
  index       = var.index
  secret_arn  = var.secret_arn
}