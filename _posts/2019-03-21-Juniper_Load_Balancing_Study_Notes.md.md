---
title:  "Juniper Load Balancing Study Notes"
date:   2019-03-21 18:55:00
categories: [Juniper]
tags: 
- Juniper 
- Routing
- JNCIS-ENT
---

By default in Junos when two equal cost paths exist a hash algorithm is used to determing which route will become the active FIB route and which will be come inactive. However if the links are equal cost there is the negative effect of having an used link, load balancing allows for both links to be utilise at the same time. 

A routing policy can be used to allow all equal cost paths to be load balanced or only specific equal cost paths. A system wise prefix lenght also has to be defined in fowarding-options. 

Network vendors typically implement load balancing as in a per-packet or per-flow approach. This is one area where Juniper is really rather confusing. Historically LB in Junos was per-packet and as such the configuration statement is per-packet. However presumably for backwards compatability the statement is still per-packet but in the background its actually doing per-flow. Per-flow is the modern standard approach as it reduces the chance the destination recieving out-of-order packets.


A flow is defined by default in Junos as the source and destination IP addresses, port inforamtion is ignored. Junos lets you modify this definition to include layer 4 port information in the hash. An important not is that every ICMP packet is trated as a new flow which may cause odd results and cause confusion when troubleshooting.  
