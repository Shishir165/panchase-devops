output "s3_bucket_name" {
  value       = aws_s3_bucket.website.bucket
  description = "S3 bucket name"
}

output "route53_nameservers" {
  value       = aws_route53_zone.website.name_servers
  description = "Add these 4 nameservers to Namecheap DNS settings"
}

output "acm_certificate_arn" {
  value       = aws_acm_certificate.website.arn
  description = "SSL certificate ARN"
}

# =============================================
# STEP 2 — uncomment after certificate ISSUED
# =============================================

 output "cloudfront_url" {
   value       = aws_cloudfront_distribution.website.domain_name
   description = "CloudFront URL"
 }

 output "cloudfront_distribution_id" {
   value       = aws_cloudfront_distribution.website.id
   description = "CloudFront distribution ID"
 }

 output "website_url" {
   value       = "https://${var.domain_name}"
   description = "Final website URL"
 }