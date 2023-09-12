import json
import boto3
client = boto3.client('kms')
with open('crypted_info.txt', 'rb') as binary_file:
    crypted_info = binary_file.read()
# print(crypted_info)
response = client.decrypt(CiphertextBlob=crypted_info,
                          KeyId='arn:aws:kms:us-east-1:648254270796:key/7c020ad4-1831-4ace-b0d6-baf7f490e147',
                          EncryptionAlgorithm= 'RSAES_OAEP_SHA_256',
                          DryRun=True)
print(response)