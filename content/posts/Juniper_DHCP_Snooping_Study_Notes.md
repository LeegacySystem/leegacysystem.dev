---
title:  "Juniper DHCP Snooping Study Notes"
date:   2019-03-31 13:30:00
categories: [Juniper]
tags: 
- Juniper 
- Routing
- JNCIS-ENT
- DHCP
- L2SEC
---

This post will cover DHCP snooping in Junos, starting with the exchange of DHCP packets.

<a href="/images/posts/2019/01/capture.png"><img src="/images/posts/2019/06/DHCP_Exchange.png" width="720" >

As shown in the diagram above the process of obtaining an IP address through DHCP involves multiple broadcasts to the network segment. This can be abuses by attackers as they can by  default see and respond to those broadcast messages just as easily as the DHCP server can. If a rogue DHCP server was to assign a fake IP address it would essentially DOS that end host, or it could forward its traffic while capture in a MITM attack. 

#### **DHCP Snooping:**
In comes a DHCP snooping to ruin that attackers day by preventing any rogue DHCP servers from intercepting legitimate traffic. DHCP snooping works by building and maintaining a list of valid IP addresses based on the DHCP packets passing through the switch. The switch will snoop on any DHCP request or acknowledgement packets and update its database based on the lease information. Each database mapping contains the IP address, MAC address and related VLAN.  

The default behaviours for Junos is to treat every access port as untrusted and every trunk port as trusted. If you have a DHCP server on a access port you will have to manually configure it as trusted for DHCP to work. Likewise if you have a customer/end user machine as a trunk port for whatever reason you may want to manually set that as untrusted. 

#### **DHCP Option 82 (relay agent)**

When enabled if a switch intercepts and snoops a DHCP request packet it will add information to it before sending it to the DHCP server. The server then reads the information and uses it to assign an IP address and returns the DHCPAck back to the client including the option 82 information which is again intercepted by the switch and removed before being passed to the client device. There are three configurable sub options:  
<ol>
  <li><i>Circuit-ID:</i> By default contains the interface name, vlan or both. A prefix can also be added which is the hostname of the switch.</li>
  <li><i>Remote-ID:</i> Defaults to the MAC address of the switch but can be configured to be the host name or some string of choice.</li>
  <li><i>Vendor-ID:</i> Defaults to Juniper</li>
</ol>

All DHCP snooping is configured under "edit ethernet-switching options secure-access-port. By default DHCP bindings are lost after the switch reboots but a file can be specified for persistent storage of DHCP bindings. The key statements for configuration are: 

<ol>
  <li><i>No-dhcp-trusted:</i> Stops the port from recieveing DHCP server traffic (default for access ports)</li>
  <li><i>Dhcp-trust:</i> Allows the port to receive DHCP server traffic (default for trunk ports)</li>
  <li><i>examine-dhcp:</i> enables DHCP snooping on a vlan.</li>
  <li><i>Dhcp-snooping-file:</i> enables persistent storage of bindings.</li>
</ol>

For special use cases perhaps where arp is not supported or has to be disabled a static dhcp binding can be installed into a switchs snooping database. 