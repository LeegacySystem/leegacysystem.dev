---
title:  "Junos DAI and IP Source Guard Study Notes"
date:   2019-04-1 17:00:00
categories: [Juniper]
tags: 
- Juniper 
- Routing
- JNCIS-ENT
- DAI
- IP Source Guard
- L2SEC
---

This will looking into Dynamic Arp Insepction and IP Source Guard for Junos.

#### **Dynamic APR Inspection:**
DAI is intended as a security solution for possible ARP spoofing or also referred to as ARP poisoning MITM attacks within a LAN/VLAN. Using the previously covered DHCP snooping binding database DAI examines each ARP request and response packet on LAN when coming from untrusted (access ports).  Trusted (trunk) ports bypass the DAI check much like the DHCP snooping check. If an arp packet goes through DAI inspection and the DHCP snooping database does not contain a IP-to-MAC mapping the ARP packet will be droped by DAI. 

DAI is configured on a per VLAN basis and not per port, it is disabled by default in Junos. One important note is that if an access port has a static IP address, it must either be configured as a trusted port to bypass DAI or have a static DHCP snooping binding, if neither of these rules have been followed then any ARP packets will be dropped by DAI. As DAI involves sending ARP packets to the RE for inspection there is a built in rate-limit on ARP packets sent to the RE.  

Like DHCP snooping again DAI is configured under the "edit ethernet-switching-options secure-access-port" hierarchy. The keyword to enable DAI is "arp-inspection" as previously mentioned configured per VLAN. The main operation commands are "show dhcp snooping binding" which has come up before and "show arp inspection statistics" which is new but self-explanatory. 

#### **IP Source Guard:**
A possibility when running a network is that some malicous user will come along and try to change/spoof their IP and MAC addresses. This can be difficult for a network admin to trace back to the source and remedy, while the spoofed IP is in play another machine may be DOS'd. IP Source Guard is intended prevent spoofing or unintended changes from happening by using the DHCP binding table. 

With IP Source Guard enabled if a packet enters an untrusted access port it will be examined against the DHCP snooping database. If the source IP or mac is invalid the switch will discard the offending packet or packets, thus preventing any spoof/changes. Like DAI IP Source Guard is enabled at a VLAN level on one or more VLANs. With a fully populated DHCP binding database IP Source will derive its own database for packet validation. For any static IPs assigned to hosts the switch must have a static DHCP binding for the IP address otherwise packets will be dropped.

Much like DAI, IP Source Guard is enabled in the edit "ethernet-switching-options secure-access-ports" using the keyword ip-source-guard or the reverse no-ip-source-guard to disable. The two main operational commands are "show dhcp snooping binding" and "show ip-source-guard".

As a note if IP Source Guard is used with 802.1x only one of the three modes can be used with IP Soure Guard. Single Supplicant mode can be used but not single-secure supplicant or multiple supplicant.  