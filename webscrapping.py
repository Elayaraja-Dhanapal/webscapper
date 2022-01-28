from itertools import count
import botocore
import boto3
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime


AWS_HEALTH_STATUS_WEB_URL = 'https://status.aws.amazon.com/'

def lambda_handler(event, context):
    article_list = []
    r = requests.get(AWS_HEALTH_STATUS_WEB_URL)        
    soup = BeautifulSoup(r.content, 'html5lib')
    table = soup.find('div', attrs= {'id':'NA_block'})        
    for tr in table.find_all('tr'):        
        print(type(tr))
        print(tr)              
        # article = {
        #             'region': 'North America',
        #             'service': td[1].string,
        #             'health': td[2].string,                
        #             'published': datetime.now
        #         }
        # article_list.append(article)
    return {
        'statusCode': 200,
        'body': json.dumps(article_list)
    }


print(lambda_handler(event=None, context=[]))