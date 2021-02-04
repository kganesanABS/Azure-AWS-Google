import AWSFunction

AWSFunction.response()

response()
def lambda_handler(event, context):
    return response("Welcome to my python lambda function", 200)
