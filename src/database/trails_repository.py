import boto3
from boto3.dynamodb.conditions import Attr
from decimal import Decimal


class TrailRepository:
    def _initialize(self):
        self.dynamodb = boto3.resource('dynamodb')
        self.table = self.dynamodb.Table("trails")

    def sort_items(items,key,reverse):
        items.sort(key=lambda item: item.get(key, 0), reverse=reverse)
        return items

    def get_trail_details(self, data):
        try:
            response = self.table.get_item(
                Key={
                    'state_name': data['state_name'] ,
                    'trail_id': data['trail_id'],
                }
            )
            return response['Item']
        except:
            return  {"error": "Item not found."}

    def get_trails_by_difficulty_rating(self, data):
        difficulty_rating = int(data.get('difficulty_rating', 7))
        response = self.table.scan(
            FilterExpression=Attr('difficulty_rating').lte(difficulty_rating)
        )
        items = response.get('Items', [])
        items = self.sort_items(items,'difficulty_rating',True)
        return items[:15]

    def get_trails_by_length(self, data):
        max_length =  Decimal(data.get('length', 339570.74))
        response = self.table.scan(
            FilterExpression=Attr('length').lte(max_length)
        )
        items = response.get('Items', [])
        items = self.sort_items(items,'length',True)
        return items[:15]
