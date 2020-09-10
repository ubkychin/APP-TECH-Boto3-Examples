import boto3
import uuid


idPost = uuid.uuid4()
print(idPost)

# Create boto3 s3Resource
s3Resource = boto3.resource('s3')

response = s3Resource.create_bucket(Bucket=str(idPost))

print(response)