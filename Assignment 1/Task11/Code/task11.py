design={"Robot cells":"Cat6A S/FTP, full duplex, VLAN and strict priority","AGVs":"Private 5G URLLC with make-before-break / packet duplication","Office and phones":"Wi-Fi 6 or wired Ethernet; voice VLAN","Vibration sensors":"Wired, Wi-Fi 6 or 5G mMTC by location","CCTV":"Local motion-triggered recording; separate storage VLAN; 10G fibre","Head-office link":"1–2 Gbps plus a diverse backup path"}
for area,recommendation in design.items(): print(f"{area}: {recommendation}")
print("Five-plant motion-triggered estimate:",5*536.32,"Mbps")
