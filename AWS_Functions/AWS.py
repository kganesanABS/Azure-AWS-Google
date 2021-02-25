import json
import sys
#sys.path.append('HttpFunction1/AWSFunction')
#from AWSFunction import response
from AWS_Functions.AWSFunction import response

def lambda_handler(event, context):
    return response("Welcome to my python lambda function", 200)
