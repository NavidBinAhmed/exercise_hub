'''pre-requisite'''
# Ensure you have the AWS credentials configured on your system.
# You can configure AWS credentials using the AWS CLI by running `aws configure` and 
# providing your access key, secret key, and region.

# Install the boto3 library if you haven't already:
# pip install boto3

# Make sure the AWS S3 bucket names and file extensions are correct.

# Run the script by executing the Python file:

# python /H:/AWS_S3_extension.py

# The script will iterate over all objects in the specified S3 bucket, 
# convert the file extensions, and move them to the new bucket.

# You do not need to remain logged in to AWS for the script to run. 

# However, you need to ensure that your AWS credentials are correctly configured and 
# have the necessary permissions to access the S3 buckets.

'''import boto3
def convert_image_extension(bucket_name, new_bucket_name, old_extension, new_extension):
    s3 = boto3.client('s3')
    s3_resource = boto3.resource('s3')
    bucket = s3_resource.Bucket(bucket_name)
    
    for obj in bucket.objects.all():
        if obj.key.endswith(old_extension):
            new_key = obj.key.replace(old_extension, new_extension)
            copy_source = {'Bucket': bucket_name, 'Key': obj.key}
            s3.copy_object(CopySource=copy_source, Bucket=new_bucket_name, Key=new_key)
            s3.delete_object(Bucket=bucket_name, Key=obj.key)
            print(f"Converted {obj.key} to {new_key}")

bucket_name = 'raw_images'
new_bucket_name = 'revised_image'
old_extension = '.PNG'
new_extension = '.JPG'

convert_image_extension(bucket_name, new_bucket_name, old_extension, new_extension)'''


'''import re
def rename_images(bucket_name, new_bucket_name):
    s3 = boto3.client('s3')
    s3_resource = boto3.resource('s3')
    bucket = s3_resource.Bucket(bucket_name)
    
    for obj in bucket.objects.all():
        match = re.match(r'KGF_(\d{8})\d{6}\.JPEG', obj.key)
        if match:
            date_part = match.group(1)
            new_key = f"ABC_{date_part}.JPG"
            copy_source = {'Bucket': bucket_name, 'Key': obj.key}
            
            # Check if the new key already exists in the new bucket
            try:
                s3.head_object(Bucket=new_bucket_name, Key=new_key)
                print(f"File {new_key} already exists in {new_bucket_name}. Skipping...")
            except:
                s3.copy_object(CopySource=copy_source, Bucket=new_bucket_name, Key=new_key)
                s3.delete_object(Bucket=bucket_name, Key=obj.key)
                print(f"Renamed {obj.key} to {new_key}")

bucket_name = 'incoming images'
new_bucket_name = 'renamed images'

rename_images(bucket_name, new_bucket_name)'''






















