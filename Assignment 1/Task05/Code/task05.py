import math
distance_m,speed_mps=1200,2
trip_s=distance_m/speed_mps
print('AGV trip time:',trip_s,'seconds')
print('Wi-Fi interruption:',39*0.150,'seconds')
print('Private 5G interruption:',3*0.020,'seconds')
demand=600*50*8/1000
print('600-sensor LoRaWAN demand:',demand,'kbps')
print('Gateways at 5 kbps each:',math.ceil(600*50*8/5000))
