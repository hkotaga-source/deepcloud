variable "region" {
  description = "AWS region"
  type        = string
  default     = "ap-south-1"
}

variable "app_name" {
  description = "Name used for all resources"
  type        = string
  default     = "deepcloud"
}

variable "image_tag" {
  description = "Container image tag pushed to ECR"
  type        = string
  default     = "latest"
}

variable "container_port" {
  description = "Port the API listens on"
  type        = number
  default     = 8000
}

variable "cpu" {
  description = "Fargate task CPU units"
  type        = number
  default     = 512
}

variable "memory" {
  description = "Fargate task memory (MiB)"
  type        = number
  default     = 1024
}

variable "desired_count" {
  description = "Number of running tasks"
  type        = number
  default     = 1
}
