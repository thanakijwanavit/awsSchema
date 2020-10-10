# AWS_SCHEMA
> dataclass for aws dictionaries


This library aims to parse aws dictionaries and json strings into dataclass objects

## Install

`pip install awsSchema`

## How to use

extract data from aws classes eg apigateway lambda input/output
this library uses jsondataclass, and dataclass

```
from awsSchema.apigateway import Response, Event
```

## parsing event

```
dummyEvent = { "message": "Hello me!", "input": { "resource": "/{proxy+}", "path": "/hello/world", "httpMethod": "POST", "headers": { "Accept": "*/*", "Accept-Encoding": "gzip, deflate", "cache-control": "no-cache", "CloudFront-Forwarded-Proto": "https", "CloudFront-Is-Desktop-Viewer": "true", "CloudFront-Is-Mobile-Viewer": "False", "CloudFront-Is-SmartTV-Viewer": "False", "CloudFront-Is-Tablet-Viewer": "False", "CloudFront-Viewer-Country": "US", "Content-Type": "application/json", "headerName": "headerValue", "Host": "gy415nuibc.execute-api.us-east-1.amazonaws.com", "Postman-Token": "9f583ef0-ed83-4a38-aef3-eb9ce3f7a57f", "User-Agent": "PostmanRuntime/2.4.5", "Via": "1.1 d98420743a69852491bbdea73f7680bd.cloudfront.net (CloudFront)", "X-Amz-Cf-Id": "pn-PWIJc6thYnZm5P0NMgOUglL1DYtl0gdeJky8tqsg8iS_sgsKD1A==", "X-Forwarded-For": "54.240.196.186, 54.182.214.83", "X-Forwarded-Port": "443", "X-Forwarded-Proto": "https" }, "multiValueHeaders":{ 'Accept':[ "*/*" ], 'Accept-Encoding':[ "gzip, deflate" ], 'cache-control':[ "no-cache" ], 'CloudFront-Forwarded-Proto':[ "https" ], 'CloudFront-Is-Desktop-Viewer':[ "true" ], 'CloudFront-Is-Mobile-Viewer':[ "False" ], 'CloudFront-Is-SmartTV-Viewer':[ "False" ], 'CloudFront-Is-Tablet-Viewer':[ "False" ], 'CloudFront-Viewer-Country':[ "US" ], '':[ "" ], 'Content-Type':[ "application/json" ], 'headerName':[ "headerValue" ], 'Host':[ "gy415nuibc.execute-api.us-east-1.amazonaws.com" ], 'Postman-Token':[ "9f583ef0-ed83-4a38-aef3-eb9ce3f7a57f" ], 'User-Agent':[ "PostmanRuntime/2.4.5" ], 'Via':[ "1.1 d98420743a69852491bbdea73f7680bd.cloudfront.net (CloudFront)" ], 'X-Amz-Cf-Id':[ "pn-PWIJc6thYnZm5P0NMgOUglL1DYtl0gdeJky8tqsg8iS_sgsKD1A==" ], 'X-Forwarded-For':[ "54.240.196.186, 54.182.214.83" ], 'X-Forwarded-Port':[ "443" ], 'X-Forwarded-Proto':[ "https" ] }, "queryStringParameters": { "name": "me", "multivalueName": "me" }, "multiValueQueryStringParameters":{ "name":[ "me" ], "multivalueName":[ "you", "me" ] }, "pathParameters": { "proxy": "hello/world" }, "stageVariables": { "stageVariableName": "stageVariableValue" }, "requestContext": { "accountId": "12345678912", "resourceId": "roq9wj", "stage": "testStage", "requestId": "deef4878-7910-11e6-8f14-25afc3e9ae33", "identity": { "cognitoIdentityPoolId": None, "accountId": None, "cognitoIdentityId": None, "caller": None, "apiKey": None, "sourceIp": "192.168.196.186", "cognitoAuthenticationType": None, "cognitoAuthenticationProvider": None, "userArn": None, "userAgent": "PostmanRuntime/2.4.5", "user": None }, "resourcePath": "/{proxy+}", "httpMethod": "POST", "apiId": "gy415nuibc" }, "body": "{\r\n\t\"a\": 1\r\n}", "isBase64Encoded": False } }
event = Event.from_dict(dummyEvent['input'])
event
```




    {'body': {'a': 1}, 'header': {}}



```
event.getBody()
```




    {'a': 1}



## creating response dict

```
Response.getReturn(body={'hello':'world'})
```




    {'body': '{"hello":"world"}', 'statusCode': 200, 'header': {}}



## Use in lambda function

```
def lambda_handler(event, *args):
  # parsing event body
  e = Event.from_dict(event)
  body = e.getBody()
  
  
  # submitting output
  return Response.getReturn(
    body = body, statusCode= 200, header = {'hello':'hello'}
  )

lambda_handler(dummyEvent['input'])
```




    {'body': '{"a":1}', 'statusCode': 200, 'header': {'hello': 'hello'}}


