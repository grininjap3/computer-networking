def mod2_division(dividend,divisor):
 bits=list(map(int,dividend)); div=list(map(int,divisor))
 for i in range(len(bits)-len(div)+1):
  if bits[i]:
   for j in range(len(div)): bits[i+j]^=div[j]
 return ''.join(map(str,bits[-(len(div)-1):]))
data,generator='1101011011','1011'
remainder=mod2_division(data+'0'*(len(generator)-1),generator)
frame=data+remainder
print('Data:',data); print('Generator:',generator)
print('CRC remainder:',remainder); print('Transmitted codeword:',frame)
print('Corrupted last-bit remainder:',mod2_division(frame[:-1]+('1' if frame[-1]=='0' else '0'),generator))
