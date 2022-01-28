import requests
from bs4 import BeautifulSoup


AWS_HEALTH_STATUS_WEB_URL = 'https://status.aws.amazon.com/'

def lambda_handler(event, context):
    article_list = []
    r = requests.get(AWS_HEALTH_STATUS_WEB_URL)        
    soup = BeautifulSoup(r.content)    
    div = soup.find('div', attrs= {'id':'NA_block'})    
    tables = div.find_all('table')    
    service_table = tables[1]
    rows = service_table.tbody.find_all('tr')
    for row in rows:
        cells = row.find_all('td')
        if 'Amazon DynamoDB' in cells[1].string:
            article = {
                'service': cells[1].string,
                'health': cells[2].string
                }
            article_list.append(article)
        if 'Amazon ECR' in cells[1].string:
            article = {
                'service': cells[1].string,
                'health': cells[2].string
                }
            article_list.append(article)
        if 'Amazon API Gateway' in cells[1].string:
            article = {
                'service': cells[1].string,
                'health': cells[2].string
                }
            article_list.append(article)
        if 'Amazon Elastic Kubernetes' in cells[1].string:
            article = {
                'service': cells[1].string,
                'health': cells[2].string
                }
            article_list.append(article)
        if 'Amazon Route 53' in cells[1].string:
            article = {
                'service': cells[1].string,
                'health': cells[2].string
                }
            article_list.append(article)
        if 'AWS CodeCommit' in cells[1].string:
            article = {
                'service': cells[1].string,
                'health': cells[2].string
                }
            article_list.append(article)
    return {
        'statusCode': 200,
        'body': article_list
    }


print(lambda_handler(event=None, context=[]))