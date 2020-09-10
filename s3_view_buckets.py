import boto3

s3Resource = boto3.resource('s3')

# Access the collection
myBuckets = s3Resource.buckets


for bucket in myBuckets.all():
    print(bucket.name , " created: ", bucket.creation_date)

    for file in bucket.objects.all():
        print(file)

    print('----------------------------------')
    print()
