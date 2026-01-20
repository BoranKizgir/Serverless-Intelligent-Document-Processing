Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import boto3
... import json
... import urllib.parse
... 
... def lambda_handler(event, context):
...     textract = boto3.client('textract', region_name='eu-west-2')
...     dynamodb = boto3.resource('dynamodb', region_name='eu-west-2')
...     table = dynamodb.Table('BelgeMetadata')
... 
...     # Dosya adını güvenli bir şekilde al
...     bucket = event['Records'][0]['s3']['bucket']['name']
...     raw_key = event['Records'][0]['s3']['object']['key']
...     document_name = urllib.parse.unquote_plus(raw_key)
...     
...     print(f"Islem basliyor: Bucket={bucket}, Key={document_name}")
... 
...     try:
...         response = textract.analyze_document(
...             Document={'S3Object': {'Bucket': bucket, 'Name': document_name}},
...             FeatureTypes=["FORMS"]
...         )
...         
...         print("Textract analizi basarili.")
...         
...         # Basit metin birlestirme
...         detected_text = " ".join([b['Text'] for b in response['Blocks'] if b['BlockType'] == 'LINE'])
...         
...         table.put_item(Item={
...             'DocumentID': document_name,
...             'FullText': detected_text
...         })
...         
...         print("DynamoDB yazma basarili.")
...         return {"status": "success"}
... 
...     except Exception as e:
...         print(f"HATA DETAYI: {str(e)}")
