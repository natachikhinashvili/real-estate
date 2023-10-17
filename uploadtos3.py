import boto3

def uploadtos3():
    s3 = boto3.client("s3")
    
    bucket = "realestatedata123"
    filename = "data.txt"

    s3.upload_file("data.txt", bucket, filename)

    print("uploaded")