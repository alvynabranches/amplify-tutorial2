import json

# import requests


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    try:
        first_name = event["first_name"]
    except KeyError as e:
        print(e)
        first_name = None
    try:
        last_name = event["last_name"]
    except KeyError as e:
        print(e)
        last_name = None
    try:
        message = event["message"]
    except KeyError as e:
        print(e)
        message = None

    if first_name is None or last_name is None:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": "Invalid body (first_name | last_name)!"
            })
        }
    if message is None:
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": f"{first_name} {last_name}"
            })
        }
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": f"{message} {first_name} {last_name}",
            # "location": ip.text.replace("\n", "")
        }),
    }
