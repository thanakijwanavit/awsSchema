# AUTOGENERATED! DO NOT EDIT! File to edit: apigateway.ipynb (unless otherwise specified).

__all__ = ['Response', 'Event', 'Product', 'Products']

# Cell
from dataclasses import field
from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, Undefined
from pprint import pformat
from typing import Optional, List, Callable, Any
import ujson as json

@dataclass_json
@dataclass
class Response:
  '''
    parse response from apigateway
  '''
  body: Optional[str]
  statusCode: int = 200
  headers: dict = field(default_factory = dict)
  @classmethod
  def parseBody(cls, dictInput:dict):
    response = cls.fromDict(dictInput)
    return response.body
  @classmethod
  def parseHeaders(cls, dictInput:dict):
    response = cls.fromDict(dictInput)
    return response.headers

  @classmethod
  def fromDict(cls, dictInput:dict):
    '''
      output object from Dict,
      dictInput should follow apigateway proxy integration
    '''
    body = dictInput.pop('body')
    return cls(
      body = json.loads(body),
      **dictInput
    )
  @classmethod
  def getReturn(cls, body:dict, headers:dict = {
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': '*',
        },
        statusCode:int = 200)->dict:
    '''
      output dictionary which is suitable for apigateway proxy integration return
    '''
    returnObj = cls(
      body = json.dumps(body),
      headers = headers,
      statusCode = statusCode
                   ).to_dict()
    return returnObj
  @classmethod
  def returnError(cls, message:str, statusCode:int = 400, **kwargs)->dict:
    '''add override statusCode Here by putting in the values directly'''
    return cls.getReturn(statusCode = statusCode, body = {'error': message})
  @classmethod
  def returnSuccess(cls, body:dict = {}, statusCode:int = 200, **kwargs)->dict:
    '''add override statusCode Here'''
    return cls.getReturn(statusCode = statusCode, body = body, **kwargs)

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class Event:
  '''
    parse event from apigateway
  '''
  body: str

  httpMethod: Optional[str] = None
  multiValueHeaders: Optional[dict] = None
  multiValueQueryStringParameters: Optional[dict] = None
  path: Optional[str] = None
  pathParameters: Optional[dict] = None
  queryStringParameters: Optional[dict] = None
  requestContext: Optional[dict] = None

  headers: dict = field(default_factory = dict)
  statusCode: int = 200
  isBase64Encoded: bool = False

  def getBody(self,*args):
    try:
      return json.loads(self.body)
    except:
      return Event.parseBody(self,*args)
  def getProducts(self):
    return Products.from_json(self.body)
  def getKey(self, key='product'):
    return self.body.get(key)

  key = lambda self: json.loads(self.body)['key']
  firstKey = lambda self: next(iter(json.loads(self.body).items()))
  @classmethod
  def parseBody(cls, event, *args):
    return cls.from_dict(event).getBody()
  @classmethod
  def parseHeaders(cls, event, *args):
    return cls.from_dict(event).headers
  @classmethod
  def parseQuery(cls, event, *args):
    return cls.from_dict(event).queryStringParameters
  @classmethod
  def parsePath(cls, event, *args):
    return cls.from_dict(event).path
  @classmethod
  def getInput(cls, body={},headers={},statusCode=200):
    return cls(body=json.dumps(body),headers=headers,statusCode=statusCode).to_dict()
  @classmethod
  def parseDataClass(cls, customClass, event):
    body = cls.getBody(event)
    try:
      return customClass.from_dict(body)
    except Exception as e:
      raise Exception(f'unable to parse input{e}, should have the schema {customClass.__doc__},\
        but the current input is {body}')

@dataclass_json
@dataclass
class Product:
  cprcode: str
  iprcode: str
  oprcode: str
  ordertype: str
  pr_abb: str
@dataclass_json
@dataclass
class Products:
  products: List[Product]