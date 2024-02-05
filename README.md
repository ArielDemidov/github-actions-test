# github-actions-test

Running the following command on WSL Kali-linux:

```bash
echo "S3_BUCKET_NAME=$(terraform output -raw aws_s3_bucket | tr -d '"')" >> test.txt
```

yields me with a txt file containing: `S3_BUCKET_NAME=test-eladbe-test`
