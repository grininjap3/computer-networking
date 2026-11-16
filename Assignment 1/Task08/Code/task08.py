def hamming74_decode(bits):
 b=[0]+[int(x) for x in bits]
 s1=b[1]^b[3]^b[5]^b[7]; s2=b[2]^b[3]^b[6]^b[7]; s4=b[4]^b[5]^b[6]^b[7]
 syndrome=s1+2*s2+4*s4; corrected=b[:]
 if syndrome: corrected[syndrome]^=1
 return syndrome,''.join(map(str,corrected[1:])),''.join(str(corrected[i]) for i in (3,5,6,7))
received='0110111'
syndrome,corrected,data=hamming74_decode(received)
print('Received:',received); print('Error position:',syndrome)
print('Corrected codeword:',corrected); print('Decoded data:',data)
print('For 16 data bits, r=5 check bits; total length=21 bits.')
