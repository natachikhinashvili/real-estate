import boto3

def uploadtos3():
    s3 = boto3.client("s3")
    
    bucket = "realestatedata123"
    filename = "data.txt"
    mapfilename = "index.html"

    s3.upload_file("data.txt", bucket, filename)
    s3.upload_file("map.html", bucket, mapfilename,  ExtraArgs={'ContentType': 'text/html'}) 