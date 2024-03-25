import boto3

dynamodb = boto3.resource('dynamodb')
table= dynamodb.Table("trails")

def get_items(data):
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


    