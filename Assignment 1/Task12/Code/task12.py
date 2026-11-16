agvs=50
per_agv_mbps=4.24
print(f"50 AGVs total traffic: {agvs*per_agv_mbps:.2f} Mbps")
print(f"Commands + status: {agvs*(0.16+0.08):.2f} Mbps")
print(f"Wi-Fi interruption per trip: {39*0.150:.2f} s")
print(f"5G interruption per trip: {3*0.020:.2f} s")
print("Recommendation: private 5G URLLC with dual connectivity, local core and watchdog.")
