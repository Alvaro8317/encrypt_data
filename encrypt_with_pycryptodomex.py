from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

##########################GENERATE CERTIFICATE PAIR########################

# new_key = RSA.generate(2048)

# private_key = new_key.exportKey("PEM")
# public_key = new_key.publickey().exportKey("PEM")

# fd = open("private_key.pem", "wb")
# fd.write(private_key)
# fd.close()

# fd = open("public_key.pem", "wb")
# fd.write(public_key)
# fd.close()

################ENCRYPT/DECRYPT DATA WITH CERTIFICATE#######################

message = b'CODE EVERYDAY TO GET BETTER'

key = RSA.import_key(open('public_key.pem').read())
print(f'Here is the key: {key}')

cipher = PKCS1_OAEP.new(key)
print(f'Here is the cipher: {cipher}')
ciphertext = cipher.encrypt(message)
print(ciphertext)
fd = open("crypted_info.txt", "wb")
fd.write(ciphertext)
fd.close()
print("\n\n")