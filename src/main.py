
import json

print('Hello, World!')

def lambda_handler(event, context):
    print('Testing artifacts!')
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
