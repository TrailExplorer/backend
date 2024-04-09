import boto3
from boto3.dynamodb.conditions import Attr, Key
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table= dynamodb.Table("trails")

def sort_items(items,key,reverse):
    items.sort(key=lambda item: item.get(key, 0), reverse=reverse)
    return items

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

def get_trails_by_difficulty_rating(data):
    difficulty_rating = int(data.get('difficulty_rating', 7))
    response = table.scan(
        FilterExpression=Attr('difficulty_rating').lte(difficulty_rating)
    )
    items = response.get('Items', [])
    items=sort_items(items,'difficulty_rating',True)
    return items[:15]

def get_trails_by_length(data):
    max_length =  Decimal(data.get('length', 339570.74))
    response = table.scan(
        FilterExpression=Attr('length').lte(max_length)
    )
    items = response.get('Items', [])
    items=sort_items(items,'length',True)
    return items[:15]

def get_trails_by_rating(data):
    state = data.get('state', None)
    rating = data.get('rating', None)

    if state is None and rating is None:
        response = table.scan(
            FilterExpression=Attr('avg_rating').gte(Decimal(5))
        )
    elif state is None:
        response = table.scan(
            FilterExpression=Attr('avg_rating').gte(Decimal(rating))
        )
    elif rating is None:
        response = table.query(
            KeyConditionExpression=Key('state_name').eq(state)
        )
    else:
        response = table.query(
            KeyConditionExpression=Key('state_name').eq(state),
            FilterExpression=Attr('avg_rating').gte(Decimal(rating))
        )
    items = response['Items']
    return sort_items(items, 'avg_rating', True)[:15]




