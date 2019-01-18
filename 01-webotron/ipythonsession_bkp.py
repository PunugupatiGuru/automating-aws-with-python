# coding: utf-8
import boto3
session = boto3.Session(profile_name='gurup')
s3 = session.resource('s3')
for bucket in s3.buckets.all():
    print(bucket)

for bucket in s3.buckets.all():
    print(bucket)

new_bucket = s3.create_bucket(Bucket='guruauromation-boto3')
for bucket in s3.buckets.all():
    print(bucket)

new_bucket = s3.create_bucket(Bucket='guruauromation-boto3' , CreateBucketConfiguration={'LocationConstraint': 'eu-west-1'})
new_bucket = s3.create_bucket(Bucket='guruauromations1-boto3' , CreateBucketConfiguration={'LocationConstraint': 'eu-west-1'})
new_bucket = s3.create_bucket(Bucket='guruauromations3-boto3' , CreateBucketConfiguration={'LocationConstraint': 'eu-west-2'})
for bucket in s3.buckets.all():
    print(bucket)

get_ipython().run_line_magic('history%', '')
get_ipython().run_line_magic('history', '')
get_ipython().run_line_magic('save', 'ipythonautomation.py')
