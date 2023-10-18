import boto3

def uploadtos3():
    s3 = boto3.client("s3")
    
    bucket = "realestatedata123"
    filename = "data.txt"
    mapfilename = "map.html"

    s3.upload_file("./data.txt", bucket, filename, ExtraArgs={'ContentType': 'text/plain'})
    s3.upload_file("./map.html", bucket, mapfilename,  ExtraArgs={'ContentType': 'text/html'}) 