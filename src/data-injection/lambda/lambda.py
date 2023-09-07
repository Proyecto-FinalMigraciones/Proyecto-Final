import boto3

def handler(event, context):
    print("🐍 File: lambda/lambda.py | Line: 4 | undefined ~ event",event)
    # Crea un cliente de S3
    s3_client = boto3.client('s3')
    
    # Nombre del bucket
    bucket_name = 'csvdatainjection'
    
    try:
        # Lista los objetos en el bucket
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        
        # Imprime la lista de objetos
        if 'Contents' in response:
            for obj in response['Contents']:
                print(f'Objeto: {obj["Key"]}')
    except Exception as e:
        print(f'🐍 Error al listar objetos en el bucket: {str(e)}')
