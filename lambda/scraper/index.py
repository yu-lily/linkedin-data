import json
import boto3
import requests
import os
import undetected_chromedriver as uc
driver = uc.Chrome()


client = boto3.resource('s3')
output_bucket = client.Bucket(os.environ['OUTPUT_BUCKET'])

def handler(event, context):
    print('request: {}'.format(json.dumps(event)))
    

    print(event['url'])
    url = event['url']
    r = requests.get(url)
    driver.get('https://nowsecure.nl')
    
    fname = url.replace('http://', '')
    fname = fname.replace('https://', '')
    fname = fname.replace('/', '')
    output_bucket.put_object(Body=driver.page_source, Key=fname+ '.html')