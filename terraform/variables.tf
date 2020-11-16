# variable "access_key" {
#   description = "AWS Access Key"
# }

# variable "secret_key" {
#   description = "AWS Secret Key"
# }

variable "region" {
  description = "AWS Region"
  default     = "us-west-2"
}

variable "az_1" {
  description = "AWS AZ 1"
  default     = "a"
}

variable "org" {
  description = "Organisation"
  default     = "canexia"
}
variable "env" {
  description = "Environment"
  default     = "qa"
}

variable "private_access_ips" {
  description = "IPs to allow private access from"
  default     = "0.0.0.0/0"
}
