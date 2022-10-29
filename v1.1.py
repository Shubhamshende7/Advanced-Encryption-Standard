import rsa
(clientA_pubkey, clientA_privkey) = rsa.newkeys(512)  # Client A generates a key pair, and gives the public key to Client B
print(clientA_pubkey)



# Client B "Acknowledge" after reciving public key of Client A 
message = 'Acknowledged'.encode('utf8')

crypto = rsa.encrypt(message, clientA_pubkey)   # Client B Sends ack recepit



message = rsa.decrypt(crypto, clientA_privkey) # Client A recives and decodes ack recipt msg using "utf"
print(message.decode('utf8'))
