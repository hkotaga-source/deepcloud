output "ecr_repository_url" {
  description = "Push images here"
  value       = aws_ecr_repository.app.repository_url
}

output "cluster_name" {
  value = aws_ecs_cluster.app.name
}

output "service_name" {
  value = aws_ecs_service.app.name
}

output "log_group" {
  value = aws_cloudwatch_log_group.app.name
}
