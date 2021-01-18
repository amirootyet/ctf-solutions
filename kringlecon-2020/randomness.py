import random
from Crypto.Hash import MD5, SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from base64 import b64encode, b64decode
import binascii
import time
from mt19937predictor import MT19937Predictor


####  testing #####################

#nonce  = random.randrange(0xFFFFFFFFFFFFFFFF)
#print('%s\n' % ('%016.016x' % (nonce)))
# predictor = MT19937Predictor()
# for _ in range(624):
#     x = random.getrandbits(32)
#     predictor.setrandbits(x, 32)

# nonce = random.randrange(0xFFFFFFFFFFFFFFFF)
# print(nonce)
# nonce_pred = predictor.getrandbits(32)
# nonce_pred_second = predictor.getrandbits(32)
# print('CTF Nonce: %s\n' % ('%016.016x' % (nonce)))
# nonce1 = '%s' % ('%08x' % (nonce_pred))
# nonce2 = '%s' % ('%08x' % (nonce_pred_second))
# predicted_nonce = nonce2 + nonce1
# print("Predicted nonce:", predicted_nonce)
# #print(int("0x"+predicted_nonce, 0))

####  solving CTF #####################

predictorObj = MT19937Predictor()
#fp = open("624_nonces.txt")
fp = open("snowball_impossible.txt")

for i,line in zip(range(624), fp):
    line = line.strip("\n")
    #print(int(line))
    predictorObj.setrandbits(int(line), 32)

print("Next predicted nonce 1:", predictorObj.getrandbits(32))
#print("Next actual:", str(fp.readline()))

# for i in range(129996,130005):
#     secondNonce = hex(predictorObj.getrandbits(32))
#     firstNonce = hex(predictorObj.getrandbits(32))
#     predictedNonce = str(firstNonce).replace("0x", "") + str(secondNonce).replace("0x", "")
#     print("Next predicted nonce {}: {}".format(i, predictedNonce))

fp.close()
