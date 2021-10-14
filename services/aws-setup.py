import boto3
import requests

# Get the service client.
s3 = boto3.client('s3')

# Generate the URL to get 'key-name' from 'bucket-name'
url = s3.generate_presigned_url(
    ClientMethod='get_object',
    Params={
        'Bucket': 'bucket-name',
        'Key': 'key-name'
    }
)

# Use the URL to perform the GET operation. You can use any method you like
# to send the GET, but we will use requests here to keep things simple.
response = requests.get(url)