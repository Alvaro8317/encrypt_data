import boto3
import logging
from fernet import Fernet
from Crypto.PublicKey import RSA
client = boto3.client('kms', region_name='us-east-1')
key_arn = 'arn:aws:kms:us-east-1:648254270796:key/7c020ad4-1831-4ace-b0d6-baf7f490e147'


def encrypt_file(filename, cmk_id):
    """Encrypt a file using an AWS KMS CMK

    A data key is generated and associated with the CMK.
    The encrypted data key is saved with the encrypted file. This enables the
    file to be decrypted at any time in the future and by any program that
    has the credentials to decrypt the data key.
    The encrypted file is saved to <filename>.encrypted
    Limitation: The contents of filename must fit in memory.

    :param filename: File to encrypt
    :param cmk_id: AWS KMS CMK ID or ARN
    :return: True if file was encrypted. Otherwise, False.
    """

    # Read the entire file into memory
    try:
        with open(filename, 'rb') as file:
            file_contents = file.read()
        with open('public_key.pem', 'r') as key:
            public_key = key.read()
    except IOError as e:
        logging.error(e)
        return False

    # Generate a data key associated with the CMK
    # The data key is used to encrypt the file. Each file can use its own
    # data key or data keys can be shared among files.
    # Specify either the CMK ID or ARN
    
    # This cost money
    
    # data_key_encrypted, data_key_plaintext = create_data_key(cmk_id)
    # if data_key_encrypted is None:
    #     return False
    # logging.info('Created new AWS KMS data key')

    # Encrypt the file
    print(public_key.encode('utf-8'))
    f = Fernet(public_key.encode('utf-8'))
    print(f)
    file_contents_encrypted = f.encrypt(file_contents)
    
    # Write the encrypted data key and encrypted file contents together
    try:
        with open(filename + '.encrypted', 'wb') as file_encrypted:
            file_encrypted.write(len(data_key_encrypted).to_bytes(NUM_BYTES_FOR_LEN,
                                                                  byteorder='big'))
            file_encrypted.write(data_key_encrypted)
            file_encrypted.write(file_contents_encrypted)
    except IOError as e:
        logging.error(e)
        return False

    # For the highest security, the data_key_plaintext value should be wiped
    # from memory. Unfortunately, this is not possible in Python. However,
    # storing the value in a local variable makes it available for garbage
    # collection.
    return True


encrypt_file('requirements.txt', key_arn)
