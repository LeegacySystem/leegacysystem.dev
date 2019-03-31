---
title:  "Juniper MAC Limiting Study Notes"
date:   2019-03-31 12:04:00
categories: [Juniper]
tags: 
- Juniper 
- Routing
- JNCIS-ENT
- MAC_Sec
- L2SEC
---

This post will take a quick look into the three types of MAC Limiting available in Juniper.

This post will take a quick look into the three types of STP Protection available in Juniper including an example diagram of where to use each.

#### **MAC Limit (mac-limit):**
Allows for the admin to define the maximum number of expected MAC addresses for a specific port. If that value is set to 2 and a third MAC arrives at the interface, traffic from that MAC is subject to later action conditions but by default will be dropped and logged. 

#### **Allowed MAC (allowed-mac):**
This option allows the admin to define the exact MAC addresses that should arrive at the interface rather than the number of them. Again if an unexpected MAC address arrives at the interface traffic from that MAC is subject to later action conditions but by default will be dropped and logged. The down side of doing allowed MACs is that it requires more administrative effort as the MAC must be known and configured. 

#### **MAC move limiting (mac-move-limit):**
This option will limit the amount of times that a specific MAC address can move within the network and is configured on a per vlan basis. Again if an unexpected MAC address arrives at the interface traffic from that MAC is subject to later action conditions but by default will be dropped and logged. MAC limiting protects against MAC flooding and spoofing that can be used as a DOS attack.  

When using MAC limiting in any form it is important to think about the needs of the environment as well as security. For example if your environment has IP phones hooked up to computers both sharing the same physical access port, then the MAC limit will have to be at least two for both devices to work. 

All three types of limiting share the same three (excluding the off action) configurable actions: 
<ol>
  <li><i>Syslog</i> – Forwards the packet but generates a system alarm.</li>
  <li><i>Drop & Syslog</i> – Drops the offending MAC packet and generates an alarm.</li>
  <li><i>Shutdown (& Syslog)</i> – Shutdown the interface and generates an alarm.</li>
  <li><i>None</i> – Turns off MAC limiting for a specific port if it has been enabled on all interfaces.</li>
</ol>

#### **Auto recovery:**
If desired a timer can be configured between 10 and 3600 seconds at "edit ethernet-switching-options port-error-disable disable-timeout" that will roll back the configured action after the timeout expires.  The alternative and default is for the action to apply until the admin manually clears the port error.  