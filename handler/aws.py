import sys

sys.path.append('Lambda_function.py)
                
import Lambda_function.py
                
def lambda_handler(event, context):
    return response("Welcome to my python lambda function", 200)
