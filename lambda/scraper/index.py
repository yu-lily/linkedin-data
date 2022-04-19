import json
import boto3
import requests
import os

client = boto3.resource('s3')
output_bucket = client.Bucket(os.environ['OUTPUT_BUCKET'])

def handler(event, context):
    print('request: {}'.format(json.dumps(event)))
    
    try:
        print(event['url'])
        url = event['url']
    except:
        url = 'test2.html'

    # Write to output bucket
    output_bucket.put_object(Body=open('test.html', 'rb'), Key=url)