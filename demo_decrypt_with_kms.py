import boto3
client = boto3.client('kms', region_name='us-east-1')


def decrypt_with_kms(cipher_text: bytes, key_id):
    response = client.decrypt(CiphertextBlob=cipher_text,
                              KeyId=key_id, EncryptionAlgorithm='RSAES_OAEP_SHA_256')
    print(response['Plaintext'])
