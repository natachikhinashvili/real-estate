import boto3

def insert_data(data):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table_name = 'selling-real-estate'

    try:
        table = dynamodb.Table(table_name)


        response = table.get_item(Key={'id': data["id"]})

        if 'Item' not in response:
            response = table.put_item(
                Item={
                    "id": data["id"],
                    "name_last_name": data["name_last_name"],
                    "post_date": data["post_date"],
                    "price": data["price"],
                    "real_estate_type": data["real_estate_type"]
                }
            )
            print("New record inserted into DynamoDB.")
        else:
            print("Data already exists in DynamoDB. Not inserting.")

    except Exception as e:
        print("Error:", str(e))
