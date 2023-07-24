     from PIL import Image
     from io import BytesIO
     s3_client = boto3.client('s3’)
     def process_image(event, context):   
      	 # Get the bucket name and key from the event 
       	bucket = event['Records'][0]['s3']['bucket']['name’]  
       	key = event['Records'][0]['s3']['object']['key']
                     response = s3_client.get_object(Bucket=bucket, Key=key)                                  
             image=Image.open(BytesIO(response['Body'].read()))  
            # Perform image processing (e.g., resize)  
            resized_image = image.resize((800, 600))  
           # Save the processed image  
           processed_buffer = BytesIO()         
           resized_image.save(processed_buffer, format='JPEG')   
           processed_buffer.seek(0)
                     # Upload the processed image to S3        
          s3_client.put_object(Bucket=bucket, Key='processed/' + key,
           Body=processed_buffer)       
           return {        
                    'statusCode': 200,       
                    'body': 'Image processed successfully!’   
           }


