provider "aws" {
  region = eu-north-1
}


resource "aws_s3_bucket" "my_bucket" {
  bucket = "my-unique-s3-bucket-name"  # Replace with your desired S3 bucket name
  acl    = "public"  # Set the bucket ACL (Access Control List). Other options include "public-read", "public-read-write", etc.

  tags = {
    Name        = "MyS3Bucket"
    Environment = "Production"
  }

  versioning {
    enabled = true  # Enable versioning for the bucket
  }

  logging {
    target_bucket = aws_s3_bucket.my_bucket.id  # Log storage bucket (current bucket in this case)
    target_prefix = "logs/"
  }
}

output "s3_bucket_name" {
  value = aws_s3_bucket.my_bucket.bucket
}

resource "aws_glue_catalog_database" "example_database" {
  name = "example_database"
}

resource "aws_glue_job" "glue_job" {
  name     = "reddit_terraform"
  role_arn = aws_iam_role.example.arn

command {
    name = "pythonshell"
    python_script_location = "s3://your-s3-bucket/path/to/your/python/script.py"  # Replace with your S3 path to the Python script
  }

  default_arguments = {
    "--additional-option" = "value",
  }

  glue_version = "1.0"
  max_capacity = 2.0  # Maximum number of DPUs (Data Processing Units) for the job
  timeout      = 60   # Job timeout in minutes

  execution_property {
    max_concurrent_runs = 1  # Maximum number of concurrent runs for the job
  }

  connections {
    connections = ["example_connection"]
  }

  command {
    name        = "glueetl"
    script_location = "s3://your-s3-bucket/path/to/your/etl/script.py"  # Replace with your S3 path to the ETL script
  }

  depends_on = [aws_glue_catalog_table.example_table]
}


resource "aws_redshift_cluster" "redshift_cluster" {
  cluster_identifier = "reddit_db"
  database_name      = "your_database_name"
  master_username    = "username"
  master_password    = "pass"
  node_type          = "dc1.large"
  cluster_type       = "single-node"
}
