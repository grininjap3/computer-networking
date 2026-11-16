# Task 11 – Defend the Network Design

Hybrid design: fixed robot cells use Cat6A S/FTP, full duplex, own VLAN and strict-priority 802.1p; AGVs use private 5G URLLC with HARQ/FEC and make-before-break; office/ERP/phones use wired Cat6/fibre and Wi-Fi 6 with voice VLAN; slow temperature sensors use LoRa, vibration sensors use wired/Wi-Fi/5G mMTC; CCTV uses local motion-triggered recording, separate storage VLAN and 10G fibre; shop-floor/data-centre uses redundant 10G single-mode fibre; 400 km head-office link uses 1–2 Gbps and Selective Repeat window≥335 plus diverse backup.

Risks: single head-office circuit and mobility determinism. Five plants need 2.68 Gbps motion-triggered aggregate; use 10G. Pure 5G is unsuitable because continuous CCTV uplink alone is 768 Mbps for 8 lines, above assumed cell uplink.

## Source note
Organized from the supplied Computer Networks Assignment 1 PDF.
