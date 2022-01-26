import requests
from bs4 import BeautifulSoup


AWS_REGION_RSS_FEEDS = {'us-east-1': ['https://status.aws.amazon.com/rss/ecr-us-east-1.rss',
                                      'https://status.aws.amazon.com/rss/dynamodb-us-east-1.rss',
                                      'https://status.aws.amazon.com/rss/apigateway-us-east-1.rss',
                                      'https://status.aws.amazon.com/rss/eks-us-east-1.rss',
                                      'https://status.aws.amazon.com/rss/route53-us-east-1.rss',
                                      'https://status.aws.amazon.com/rss/codecommit-us-east-1.rss'], 'us-east-2': ['https://status.aws.amazon.com/rss/ecr-us-east-2.rss',
                                                                                                                   'https://status.aws.amazon.com/rss/dynamodb-us-east-2.rss',
                                                                                                                   'https://status.aws.amazon.com/rss/apigateway-us-east-2.rss',
                                                                                                                   'https://status.aws.amazon.com/rss/eks-us-east-2.rss',
                                                                                                                   'https://status.aws.amazon.com/rss/route53-us-east-2.rss',
                                                                                                                   'https://status.aws.amazon.com/rss/codecommit-us-east-2.rss'], 'us-west-1': ['https://status.aws.amazon.com/rss/ecr-us-west-1.rss',
                                                                                                                                                                                                'https://status.aws.amazon.com/rss/dynamodb-us-west-1.rss',
                                                                                                                                                                                                'https://status.aws.amazon.com/rss/apigateway-us-west-1.rss',
                                                                                                                                                                                                'https://status.aws.amazon.com/rss/eks-us-west-1.rss',
                                                                                                                                                                                                'https://status.aws.amazon.com/rss/route53-us-west-1.rss',
                                                                                                                                                                                                'https://status.aws.amazon.com/rss/codecommit-us-west-1.rss'], 'us-west-2': ['https://status.aws.amazon.com/rss/ecr-us-west-2.rss',
                                                                                                                                                                                                                                                                             'https://status.aws.amazon.com/rss/dynamodb-us-west-2.rss',
                                                                                                                                                                                                                                                                             'https://status.aws.amazon.com/rss/apigateway-us-west-2.rss',
                                                                                                                                                                                                                                                                             'https://status.aws.amazon.com/rss/eks-us-west-2.rss',
                                                                                                                                                                                                                                                                             'https://status.aws.amazon.com/rss/route53-us-west-2.rss',
                                                                                                                                                                                                                                                                             'https://status.aws.amazon.com/rss/codecommit-us-west-2.rss']}

article_list = []
for aws_region, feeds in AWS_REGION_RSS_FEEDS.items():
    for url in feeds:
        r = requests.get(url)        
        soup = BeautifulSoup(r.content, features='xml')
        articles = soup.findAll('item')
        aws_service = soup.find('title')
        # print(articles)
        for a in articles:            
            title = a.find('title').text
            link = a.find('link').text
            published = a.find('pubDate').text
            article = {
                'region': aws_region,
                'service': aws_service,
                'health': title,                
                'published': published
            }
            article_list.append(article)
            break


print(article_list)
