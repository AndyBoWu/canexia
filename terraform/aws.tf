# make sure you create this profile in your aws config file first

provider "aws" {
  region = "${var.region}"
  # access_key = "${var.access_key}"
  # secret_key = "${var.secret_key}"
  shared_credentials_file = "~/.aws/credentials"
  profile                 = "canexia"
}
