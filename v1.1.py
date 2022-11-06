'''***************************************************************************************************
*                   Copyright 2022-2023 corporation. All rights reserved.
*  THE SOFTWARE AND INFORMATION CONTAINED HEREIN ARE PROPRIETARY AND CONFIDENTIAL. THIS SOFTWARE IS FOR 
*   INTERNAL USE ONLY AND ANY REPRODUCTION TO ANY PARTY OUTSIDE IS IS STRICTLY PROHIBITED. 
*
*
*****************************************************************************************************'''

#---------------------------------------------Imports--------------------------------------------------
import imp
import rsa
(clientA_pubkey, clientA_privkey) = rsa.newkeys(512)  # Client A generates a key pair, and gives the public key to Client B
print(clientA_pubkey)



# Client B "Acknowledge" after reciving public key of Client A 
ackreceipt = 'Acknowledged, connection succeeded!'.encode('utf8')

crypto = rsa.encrypt(ackreceipt, clientA_pubkey)   # Client B Sends ack recepit



ackreceipt = rsa.decrypt(crypto, clientA_privkey) # Client A recives and decodes ack recipt msg using "utf"
print(ackreceipt.decode('utf8'))

