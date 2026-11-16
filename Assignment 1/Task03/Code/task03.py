LAYERS=[('Application','HTTP'),('Transport','TCP'),('Network','IP'),('Data Link','ETH')]
def send(message):
 pdu=message
 for layer,tag in LAYERS:
  pdu='['+tag+'|'+pdu+('|FCS]' if tag=='ETH' else ']')
  print(f'{layer} adds {tag} -> {len(pdu)} bytes')
 return pdu
if __name__=='__main__':
 message='GET /results'
 frame=send(message)
 print('Frame:',frame)
 print('Delivered:',message)
 print('Overhead:',len(frame)-len(message),'bytes')
