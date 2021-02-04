from AWSFunction import response

response(message, status_code)
def lambda_handler(event, context):
    return response("Welcome to my python lambda function", 200)
