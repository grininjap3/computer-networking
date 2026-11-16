import math
def utilisation(window,frame_bytes,rate_bps,distance_m):
 tx=frame_bytes*8/rate_bps; prop=distance_m/2e8; a=prop/tx
 return tx,prop,a,min(1.0,window/(1+2*a))
tx,prop,a,u=utilisation(1,1500,1e9,400000)
print(f'Transmission time: {tx*1e6:.2f} microseconds')
print(f'One-way propagation: {prop*1e3:.2f} ms')
print(f'a = {a:.2f}')
print(f'Stop-and-wait utilisation: {u*100:.3f}%')
print('Window for full utilisation:',math.ceil(1+2*a),'frames')
