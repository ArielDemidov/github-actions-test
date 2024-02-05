import os

if os.getenv('CI'):
    print('Looks like GitHub!')
else:
    print('Maybe running locally?')

print(f"Bucket: {os.getenv('S3_BUCKET_NAME')}")