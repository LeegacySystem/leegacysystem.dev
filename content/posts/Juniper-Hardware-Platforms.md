---
title:  "Juniper Hardware Platform Overview"
date:   2018-08-16 17:00:00
categories: [Juniper]
tags:
- Juniper
- Hardware
- EX
- QFX
- JNCIA
---

This post will look at the various juniper hardware platforms and summarise on each. The information presented is taken directly from the juniper product-services page. As there are comparisions of each platform this post will be table heavy.

#### **The Switching Platforms:**
1. EX Switches
2. QFX Switches

#### **The Routing Platforms:**
1. MX Routers
2. PTX Routers
3. ACX Routers
4. CTP Routers
5. T4000 Routers

#### **The Security Platforms:**
1. SRX series firewalls

<br/>

### **Overview of EX Switch Series:**

The EX series of swithces are junipers widest and most varied range. They cover from the lowest end fixed access switches to core aggregation chassis based switches.  


###### **_EX2200 Varients_** 

| Hardware Model            	| EX2200-24p            	| EX2200-48p            	| EX2200-C              	|
|---------------------------	|-----------------------	|-----------------------	|-----------------------	|
| **Form Factor**               	| 1 Node (4 VC Members) 	| 1 Node (4 VC Members) 	| 1 Node (4 VC Members) 	|
| **Resilency**                 	| no seconday psu       	| no seconday psu         	| no seconday psu       	|
| **System Throughput**         	| 56 Gbps               	| 104 Gbps              	| 28 Gbps               	|
| **Data Rate (pps)**           	| 42 Mpps (wire speed)  	| 77 Mpps (wire speed)  	| 21 Mpps               	|
| **Addition PIC slots**        	| n/a                   	| n/a                   	| n/a                   	|
| **Ipv4 Unicast/Mcast** 	| 6500/1000             	| 6500/1000             	| 6500/1000             	|
| **Ipv6 unicast/Mcast routes** 	| n/a                   	| n/a                   	| 2048 / 1024           	|
| **VLAN count**                	| 1,024                 	| 1,024                 	| 1,024                 	|
| **ARP Entries**               	| 2000                  	| 2,000                 	| 2,000                 	|

<br>

###### **_EX2300 Varients_** 

| Hardware Model            	| EX2300-24p            	| EX2300-48p            	| EX2300M-24p           	| EX2300M-48p           	| EX2300-C              	|
|---------------------------	|-----------------------	|-----------------------	|-----------------------	|-----------------------	|-----------------------	|
| **Form Factor**               	| 1 Node (4 VC Members) 	| 1 Node (4 VC Members) 	| 1 Node (4 VC Members) 	| 1 Node (4 VC Members) 	| 1 Node (4 VC Members) 	|
| **Resilency**                 	| no seconday psu       	| no seconday psu       	| no seconday psu       	| no seconday psu       	| no seconday psu       	|
| **System Throughput**         	| 128 Gbps              	| 176 Gbps              	| 208 Gbps              	| 264 Gbps              	| 64Gbps                	|
| **Data Rate (pps)**           	| 95 Mpps (ws)          	| 130 Mpps (ws)         	| 154 Mpps (ws)         	| 196 Mpps (ws)         	| 47 Mpps               	|
| **Addition PIC Slots**        	| n/a                   	| n/a                   	| 4x 10GBASE-X          	| 6x 10GBASE-X          	| n/a                   	|
| **Ipv4 Unicast/Mcast Routes** 	| 4096 / 2048           	| 4096 / 2048           	| 4096 / 2048           	| 4096 / 2048           	| 4096 / 2048           	|
| **Ipv6 unicast/Mcast Routes** 	| 2048 / 1024           	| 2048 / 1024           	| 2048 / 1024           	| 2048 / 1024           	| 2048 / 1024           	|
| **VLAN count**                	| 4093                  	| 4093                  	| 4093                  	| 4093                  	| 4093                  	|
| **ARP Entries**               	| 1500                  	| 1500                  	| 5000                  	| 5000                  	| 1500                  	

<br>

###### **_EX3300 Varients_** 

| Hardware Model            	| EX3300-24p     	| EX3300-48p     	| EX3400-24P                 	| EX3400-48P                 	|
|---------------------------	|----------------	|----------------	|----------------------------	|----------------------------	|
| **Form Factor**               	| 1 node (10 VC) 	| 1 node (10 VC) 	| 1 node (10 VC)             	| 1 node (10 VC)             	|
| **Resilency**                 	| n/a            	| n/a            	| redundanct replaceable PSU 	| redundanct replaceable PSU 	|
| **System Throughput**         	| 128 Gbps       	| 176 Gbps       	| 288 Gbps                   	| 336 Gbps                   	|
| **Data Rate (pps)**           	| 95 Mpps (ws)   	| 130 Mpps (ws)  	| 214 Mpps (ws)              	| 250 Mpps (ws)              	|
| **Additional PIC slots**        	| n/a            	| n/a            	| 2x QSFP+                   	| 2x QSFP+                   	|
| **Ipv4 Unicast/Mcast Routes** 	| 8000/4000      	| 8000/4000      	| 36,000/4,000               	| 36,000/4,000               	|
| **Ipv6 unicast/Mcast routes** 	| N/A            	| N/A            	| 18,000/2,000               	| 18,000/2,000               	|
| **VLAN count**                	| 4096           	| 4096           	| 4093                       	| 4093                       	|
| **ARP Entries**               	| 4000           	| 4000           	| 16000                      	| 16000                      	|

<br>

###### **_EX4200-4300 Varients_** 

| Hardware Model            	| EX4200-24P                 	| EX4200-48P                 	| EX4300-24P                 	| EX4300-48P                 	| EX4300-32P                 	|
|---------------------------	|----------------------------	|----------------------------	|----------------------------	|----------------------------	|----------------------------	|
| **Form Factor**               	| 1 node (10 VC)             	| 1 node (10 VC)             	| 1 node (10 VC)             	| 1 node (10 VC)             	| 1 node (10 VC)             	|
| **Resilency**                 	| redundanct replaceable PSU 	| redundanct replaceable PSU 	| redundanct replaceable PSU 	| redundanct replaceable PSU 	| redundanct replaceable PSU 	|
| **System Throughput**         	| 88 Gbps                    	| 136 Gbps                   	| 448 Gbps                   	| 496 Gbps                   	| 464 Gbps                   	|
| **Data Rate (pps)**           	| 65 Mpps (wire speed)       	| 101 Mpps (wire speed)      	| 333 Mpps (wire speed)      	| 369 Mpps (wire speed)      	| 345 Mpps (wire speed)      	|
| **Addition PIC slots**       	| 1 uplink module (built-in) 	| 1 uplink module (slot)     	| 1 uplink module (slot)     	| 1 uplink module (slot)     	| 1 uplink module (slot)     	|
| **Ipv4 Unicast/Mcast Routes** 	| 16,000/8000                	| 16,000/8000                	| 32,000/8000                	| 32,000/8000                	| 32,000/8000                	|
| **Ipv6 unicast/Mcast routes** 	| 4000/2000                  	| 4000/2000                  	| 18,000/4000                	| 18,000/4000                	| 18,000/4000                	|
| **VLAN count**                	| 4096                       	| 4096                       	| 4093                       	| 4093                       	| 4093                       	|
| **ARP Entries**               	| 16000                      	| 16000                      	| 64000                      	| 64000                      	| 64000                      	|

<br>

###### **_EX4300m-4650 Varients_** 

| Hardware Model            	| EX4300M                    	| EX4550                     	| EX4600                     	| EX4650                     	|
|---------------------------	|----------------------------	|----------------------------	|----------------------------	|----------------------------	|
| Form Factor               	| 1 node (10 VC)             	| 1 node (10 VC)             	| 1 node (10 VC)             	| 1 node                     	|
| Resilency                 	| redundanct replaceable PSU 	| redundanct replaceable PSU 	| redundanct replaceable PSU 	| redundanct replaceable PSU 	|
| System Throughput         	| n/a?                       	| 960 Gbps (full duplex)     	| 960 Gbps                   	| 2 Tbps                     	|
| Data Rate (pps)           	| n/a?                       	| 714 Mpps                   	| 1.07 Bpps                  	| 1.59 Bpps                  	|
| Addition PIC slots        	| 1 uplink module (built in) 	| 2 modules slots            	| 2 modules slots            	| 1 uplink module (built in) 	|
| Ipv4 Unicast/Mcast Routes 	| n/a?                       	| 14,000* / 4000             	| 128,000/104,000            	| 360,000/104,000            	|
| Ipv6 unicast/Mcast routes 	| n/a?                       	| 3400* / 1000               	| 64,000/52,000              	| 256,000/52,000             	|
| VLAN count                	| 4093                       	| 4096                       	| 4096                       	| 4093                       	|
| ARP Entries               	| 64000                      	| 8000                       	| 48000                      	| 48000                      	|

<br>

###### **_EX9200 Series Varients_** 

| Hardware Model            	| EX9204                  	| EX9208                  	| EX9214                  	| EX9251        	| EX9253                 	|
|---------------------------	|-------------------------	|-------------------------	|-------------------------	|---------------	|------------------------	|
| Form Factor               	| 4 Slot modular Chassis  	| 8 Slot modular Chassis  	| 16 Slot modular Chassis 	| 1 node        	| 2 slot modular chassis 	|
| Resilency                 	| 4 psu bays              	| 4 psu bays              	| 4 psu bays              	| Dual psu bays 	| 6 psu bays             	|
| System Throughput         	| 240 Gbps per slot       	| 240 Gbps per slot       	| 240 Gbps per slot       	| 800 Gbps      	| 4.8 Tbps               	|
| Data Rate (pps)           	| Up to 240 Gbps          	| Up to 240 Gbps          	| Up to 240 Gbps          	| 400 Gbps      	| 2.4 Tbps               	|
| Addition PIC slots        	| 45/28/48 4qs line cards 	| 45/28/48 4qs line cards 	| 45/28/48 4qs line cards 	| n/a           	| n/a                    	|
| Ipv4 Unicast/Mcast Routes 	| 256,000                 	| 256,000                 	| 256,000                 	| 256,000       	| 256,000                	|
| Ipv6 unicast/Mcast routes 	| 256,000                 	| 256,000                 	| 256,000                 	| 256,000       	| 256,000                	|
| VLAN count                	| 32000                   	| 32000                   	| 32000                   	| 32000         	| 32000                  	|
| ARP Entries               	| 256,000                 	| 256,000                 	| 256,000                 	| 512,000       	| 512,000                	|

<br>
<br>


### **Overview of QFX Switch Series:**

The QFX series was launched in 2013 and is targeted at data center networks. The platform uses the Broadcom Trident II chipset which is regarded as a low latency chip, however it is not the lowest. A paid for study (By Mellanox) showed that the Mellanox SX performaed the Trident II on the latency front, in addition to this the more recent AMD tomahawk is touted a having lower port-to-port latency.

QFX supports various control plane stacking technologies. Virtual Chassis (VC) is also found on the EX platform but QFX adds, Virtual Chassis Fabric and QFabric.


###### **_QFX 5100 Varients_** 

|  Hardware Model     	| QFX5100-48S        	| QFX5100-48T        	| QFX5100-24Q                  	| QFX5100-24Q-AA                                                           	| QFX5100-96S 	|
|---------------------	|--------------------	|--------------------	|------------------------------	|--------------------------------------------------------------------------	|-------------	|
| **Form Factor**         	| Single node        	| Single node        	| Single node                  	| Single node                                                              	| Single node 	|
| **System Throughput**   	| 1.44 Tbps          	| 1.44 Tbps          	| 2.56 Tbps                    	| 2.56 Tbps                                                                	| 2.56 Tbps   	|
| **Data Rate (pps)**     	| 1.08 Bpps          	| 1.08 Bpps          	| 1.44 Bpps                    	| 1.44 Bpps                                                                	| 1.44 Bpps   	|
| **Addition PIC slots**  	| 6 40GbE (built in) 	| 6 40GbE (built in) 	| 2 expansion slots for 4 x 40 	| 2 expansion slots for 4 x 40 or 1 double-wide slot for FPGA-based module 	| 8 40GbE     	|
| **Ipv4 Unicast Routes** 	| 144,000            	| 144,000            	| 144,000                      	| 144,000                                                                  	| 144,000     	|
| **Ipv6 unicast routes** 	| 104,000            	| 104,000            	| 104,000                      	| 104,000                                                                  	| 104,000     	|
| **VLAN count**          	| 4,096              	| 4,096              	| 4,096                        	| 4,096                                                                    	| 4,096       	|
| **ARP Entries**         	| 48,000             	| 48,000             	| 48,000                       	| 48,000                                                                   	| 48,000      	|

<br/>

###### **_QFX 5110-5120 Varients_** 

| Hardware Model      	| QFX5110-48S                   	| QFX5110-32Q                                                        	| QFX5200        	|
|---------------------	|-------------------------------	|--------------------------------------------------------------------	|----------------	|
| **Form Factor**         	| Single node                   	| Single node                                                        	| Single node    	|
| **System Throughput**   	| 1.76 Tbps                     	| 2.56 Tbps                                                          	| Up to 3.2 Tbps 	|
| **Data Rate (pps)**    	| 1.32 Bpps                     	| 1.44 Bpps                                                          	| Up to 2.4 Bpps 	|
| **Addition PIC slots**  	| 4 40GbE; 4 100GbE (built in?) 	| 104 10GbE (with breakout cable); 32 40GbE; 20 40GbE with 4 100GbE? 	| -              	|
| **Ipv4 Unicast Routes** 	| 144,000                       	| 144,000                                                            	| 104,000        	|
| **Ipv6 unicast routes** 	| 104,000                       	| 104,000                                                            	| 98,000         	|
| **VLAN count**          	| 4,096                         	| 4,096                                                              	| 4,096          	|
| **ARP Entries**         	| 48,000                        	| 48,000                                                             	| 32,000         	|

<br/>

###### **_QFX 10000 Varients_** 

| Hardware Model      	| QFX10002-36Q 	| QFX10002-72Q 	| QFX10008              	| QFX100016             	|
|---------------------	|--------------	|--------------	|-----------------------	|-----------------------	|
| **Form Factor**         	| single node  	| single node  	| Modular – 8 nodes     	| Modular –  16 nodes   	|
| **System Throughput**   	| 2.88 Tbps    	| 5.76 Tbps    	| 48 Tbps (6 Tbps/slot) 	| 96 Tbps (6 Tbps/slot) 	|
| **Data Rate (pps)**     	| Up to 2 Bpps 	| Up to 1 Bpps 	| Up to 16 Bpps         	| Up to 32 Bpps         	|
| **Ipv4 Unicast Routes** 	| 256,000      	| 256,000      	| 256,000               	| 256,000               	|
| **Ipv6 unicast routes** 	| 128,000      	| 128,000      	| 128,000               	| 128,000               	|
| **VLAN count**          	| 16,000       	| 16,000       	| 16,000                	| 16,000                	|
| **ARP Entries**         	| 144,000      	| 256,000      	| 256,000               	|                       	|

<br/>

<br/>
<br/>

TBD