import math
def nyquist(bandwidth_hz,levels): return 2*bandwidth_hz*math.log2(levels)
def shannon(bandwidth_hz,snr_db):
 snr=10**(snr_db/10)
 return bandwidth_hz*math.log2(1+snr)
for db in (40,15): print(f'Shannon at {db} dB: {shannon(250e6,db)/1e6:.2f} Mbps')
required=2**(56000/3100)-1
print(f'SNR for 56 kbps over 3100 Hz: {10*math.log10(required):.2f} dB')
print(f'Nyquist at 3100 Hz, 16 levels: {nyquist(3100,16)/1000:.2f} kbps')
