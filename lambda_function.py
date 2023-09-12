import Crypto
import base64
import json
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

# PEM-formatted RSA public key copied over from AWS KMS or your own public key.
RSA_PUBLIC_KEY = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA0d7rGziSUxF6kq4lJNa8
8JCIO5gCNMfGZIFzQpRIyM6LmsfoP/1FVfvjx6G4+PNL+Qs2zNG6Au0cgS4enZND
/XZ7QfI4mEZyQ14Rc3rVohA9M2Ez8193/phMXQsqHYUPGIbPLO658yHJV0IDwqQJ
Trrnq96n/dqNfmmIEmcWfu7WR7iPbIicBuCa7YZTZNwkB0la/0H1IP9bJt5wxWXs
+i9NIw9OBdW9QtFAEP9pKTrbnf28/yF47Q1zjMM6kcx5kHMJR4FwJDWipoQFUSTy
EUD28+zz7/DN76seaUcBwvQISfpmPhyMgjL6ZwSTiv8bfCYj83XC68cpWR60KNV0
eQIDAQAB
-----END PUBLIC KEY-----"""
RSA_PUBLIC_KEY_OBJ = RSA.importKey(RSA_PUBLIC_KEY)
RSA_CIPHER_OBJ = PKCS1_OAEP.new(RSA_PUBLIC_KEY_OBJ, Crypto.Hash.SHA256)

# Example sensitive data field names in a JSON object. 
PII_SENSITIVE_FIELD_NAMES = ["fname", "lname", "email", "ssn", "dob", "phone"]

CIPHERTEXT_PREFIX = "#01#"
CIPHERTEXT_SUFFIX = "#10#"


def lambda_handler(event, context):
    # Extract HTTP request and its body as per documentation:
    # https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-event-structure.html
    http_request = event['Records'][0]['cf']['request']
    body = http_request['body']
    print('Aquí')
    org_body = base64.b64encode(body['data'])
    print(org_body)
    mod_body = protect_sensitive_fields_json(org_body)
    body['action'] = 'replace'
    body['encoding'] = 'text'
    body['data'] = mod_body
    return http_request


def protect_sensitive_fields_json(body):
    # Encrypts sensitive fields in sample JSON payload shown earlier in this post.
    # [{"fname": "Alejandro", "lname": "Rosalez", … }]
    person_list = json.loads(body.decode("utf-8"))
    for person_data in person_list:
        for field_name in PII_SENSITIVE_FIELD_NAMES:
            if field_name not in person_data:
                continue
            plaintext = person_data[field_name]
            ciphertext = RSA_CIPHER_OBJ.encrypt(bytes(plaintext, 'utf-8'))
            ciphertext_b64 = base64.b64encode(ciphertext).decode()
            # Optionally, add unique prefix/suffix patterns to ciphertext
            person_data[field_name] = CIPHERTEXT_PREFIX + ciphertext_b64 + CIPHERTEXT_SUFFIX
    return json.dumps(person_list)


test_event = {
    "Records": [
        {
            "cf": {
                "config": {
                    "distributionId": "EXAMPLE"
                },
                "request": {
                    "uri": "/test",
                    "method": "GET",
                    "clientIp": "2001:cdba::3257:9652",
                    "headers": {
                        "user-agent": [
                            {
                                "key": "User-Agent",
                                "value": "test-agent"
                            }
                        ],
                        "host": [
                            {
                                "key": "Host",
                                "value": "d123.cf.net"
                            }
                        ]
                    },
                    "body": 'ewogICAgICAgICAgICAiZGF0YSI6IHsKICAgICAgICAgICAgICAibWVzc2FnZSI6ICJPSyIKICAgICAgICAgICAgfQogICAgICAgICAgfQ=='
                }
            }
        }
    ]
}

# lambda_handler(test_event,'no')
import base64

# Cadena Base64 que deseas decodificar
encoded_str = 'SG9sYSwgdGVzdG8gZXMgdW4gZXNwZWphbSBkZSBjb2Rlw7NuY2lhcyBCYXNlNjQu'

# Decodifica la cadena Base64 en datos binarios
decoded_data = base64.b64decode(encoded_str)

# Convierte los datos binarios en una cadena de texto
decoded_str = decoded_data.decode('utf-8')

print(decoded_str)
