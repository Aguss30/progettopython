terraform {
  required_providers {
    github = {
      source  = "integrations/github"
      version = "~> 6.0"
    }
  }
}

provider "github" {
  token = var.github_token
}

variable "github_token" {
  type      = string
  sensitive = true
}

resource "github_repository" "demo" {
  name        = "terraform-demo-repo"
  description = "Repository creato con Terraform per esercitarmi"
  visibility  = "public"
  auto_init   = true
}