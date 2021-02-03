import sys
sys.path.append('AWSFunction.py)              
import Lambda_function.py               
def lambda_handler(event, context):
    return response("Welcome to my python lambda function", 200)
