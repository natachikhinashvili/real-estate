import boto3
from boto3.dynamodb.conditions import Attr


def insert_data(data):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table_name = 'selling-real-estate'

    try:
        table = dynamodb.Table(table_name)
        response = table.scan(FilterExpression=Attr("address").eq(data["address"]))

        if response['Count'] == 0:
            try:
                table.put_item(
                    Item={
                        "id": data["id"],
                        "name_last_name": data["name_last_name"],
                        "post_date": data["post_date"],
                        "price": data["price"],
                        "real_estate_type": data["real_estate_type"],
                        "address": data["address"]
                    }
                )
                print("Item inserted successfully.")
            except Exception as e:
                print("Error:", str(e))
    except Exception as e:
        print("Error:", str(e))
