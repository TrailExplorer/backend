import os
import boto3
from boto3.dynamodb.conditions import Attr, Key
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table= dynamodb.Table("trails")

def sort_items(items,key,reverse):
    items.sort(key=lambda item: item.get(key, 0), reverse=reverse)
    return items

def get_trail_details(state_name, trail_id):
    try:
        response = table.get_item(
            Key={
                'state_name': state_name ,
                'trail_id': int(trail_id)
            }
        )
        return response['Item']
    except:
        return  {"error": "Item not found."}

def get_trails_by_difficulty_rating(difficulty_rating, state_name=None):
    if difficulty_rating is None:
        difficulty_rating = '7'
    
    if state_name is None:
        response = table.scan(
            FilterExpression=Attr('difficulty_rating').lte(int(difficulty_rating))
        )
    else:
        response = table.query(
            KeyConditionExpression=Key('state_name').eq(state_name),
            FilterExpression=Attr('difficulty_rating').lte(int(difficulty_rating))
        )
    items = response.get('Items', [])
    return sort_items(items,'difficulty_rating',True)[:15]

def get_trails_by_length(data):
    max_length =  Decimal(data.get('length', 339570.74))
    response = table.scan(
        FilterExpression=Attr('length').lte(max_length)
    )
    items = response.get('Items', [])
    return sort_items(items,'length',True)[:15]

def get_trails_by_rating(data):
    state = data.get('state', None)
    rating = data.get('rating', 5)
    if state is None:
        response = table.scan(
            FilterExpression=Attr('avg_rating').gte(Decimal(rating))
        )
    else:
        response = table.query(
            KeyConditionExpression=Key('state_name').eq(state),
            FilterExpression=Attr('avg_rating').gte(Decimal(rating))
        )
    items = response['Items']
    return sort_items(items, 'avg_rating', True)[:15]




