robot=40*(1/0.002)*200*8/1e6
sensors=600*50*8/1e6
cctv=24*4
office=150*2*0.10
line_total=robot+sensors+cctv+office
print(f"Robots: {robot:.2f} Mbps")
print(f"Sensors: {sensors:.2f} Mbps")
print(f"CCTV: {cctv:.2f} Mbps")
print(f"Office: {office:.2f} Mbps")
print(f"One line: {line_total:.2f} Mbps")
print(f"Eight-line plant: {8*line_total:.2f} Mbps")
print(f"Motion-triggered plant: {8*(32+0.24+4.8+30):.2f} Mbps")
