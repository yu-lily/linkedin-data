import json
import boto3
import requests
import os

client = boto3.resource('s3')
output_bucket = client.Bucket(os.environ['OUTPUT_BUCKET'])

def handler(event, context):
    print('request: {}'.format(json.dumps(event)))

    print(event['url'])
    url = event['url']
    r = requests.get(url)
    
    fname = url.replace('http://', '')
    fname = fname.replace('https://', '')
    output_bucket.put_object(Body=r.content, Key=fname+ '.html')