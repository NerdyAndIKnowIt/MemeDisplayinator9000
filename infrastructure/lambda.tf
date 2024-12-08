resource "aws_lambda_function" "lambda" {
  filename         = "LambdaPackage.zip" # lambda package
  function_name    = "meme_retriever_lambda"
  role             = aws_iam_role.lambda_exec.arn
  handler          = "LambdaPythonPackage.LambdaHandler"
  runtime          = "python3.11"
}

resource "aws_iam_role" "lambda_exec" {
  name = "lambda_exec_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action    = "sts:AssumeRole"
        Effect    = "Allow"
        Principal = { 
            Service = "lambda.amazonaws.com" 
        }
      }
    ]
  })
}

resource "aws_iam_role_policy" "lambda_policy" {
  name   = "lambda_policy"
  role   = aws_iam_role.lambda_exec.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action   = [
            "logs:CreateLogGroup", 
            "logs:CreateLogStream", 
            "logs:PutLogEvents"
        ]
        Effect   = "Allow"
        Resource = "arn:aws:logs:*:*:*"
      },
      {
        Action   = [
            "s3:PutObject",
            "s3:DeleteObject",
            "s3:ListBucket"
        ]
        Effect   = "Allow"
        Resource = [
            "arn:aws:s3:::MemeDisplayinator9000.com", 
            "arn:aws:s3:::MemeDisplayinator9000.com/*"       
        ]
      }
    ]
  })
}