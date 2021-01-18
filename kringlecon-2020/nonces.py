fp = open("nonces_hex.txt")
fp2 = open("nonces_split.txt", "w")

for line in fp:
    line = line.strip("\n")
    print(line)
    if line:
        nonce2, nonce1 = line[:int(len(line)/2)], line[int(len(line)/2):]
        print(nonce1 +"  : " + nonce2)
        print(int(nonce1, 16))
        print(int(nonce2, 16))
        fp2.write(str(int(nonce1, 16)) + "\n"+ str(int(nonce2, 16)) + "\n")

fp.close() ; fp2.close()
