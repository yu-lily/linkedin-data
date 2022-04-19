import json
from logging import exception
import boto3
import base64
import os
import io
import time

client = boto3.resource('s3')
output_bucket = client.Bucket(os.environ['OUTPUT_BUCKET'])

def handler(event, context):
    print('request: {}'.format(json.dumps(event)))

    # Write to output bucket
    output_bucket.put_object(Body=open('test.html', 'rb'), Key='test.html')