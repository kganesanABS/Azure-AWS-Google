import sys
sys.path.append('AWSFunction.py)              
import AWSFunction.py               
def aws(event, context):
    return response("Welcome to my python lambda function", 200)
