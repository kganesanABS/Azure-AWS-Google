import json
import sys
sys.path.append('./HttpFunction1/aws.py)
                
import aws.py

def response(message, status_code):
    return {
        'isBase64Encoded': False,
        'statusCode': status_code,
        'body': json.dumps(message),
        'headers': {'Content-Type': 'application/json'}
    }
