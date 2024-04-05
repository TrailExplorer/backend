import boto3
from boto3.dynamodb.conditions import Attr

dynamodb = boto3.resource('dynamodb')
table= dynamodb.Table("trails")

def get_trail_details(data):
    try:
        response = table.get_item(
            Key={
                'state_name': data['state_name'] ,
                'trail_id': data['trail_id'],
            }
        )
        return response['Item']
    except:
        return  {"error": "Item not found."}

def get_trails_on_difficulty_rating(difficulty_rating):
    response = table.scan(
        FilterExpression=Attr('difficulty_rating').eq(difficulty_rating)
    )
    return response['Items'][:15]