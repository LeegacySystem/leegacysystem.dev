---
title:  "IEEE 802.1D-2004 Broke My Lab :("
date:   2019-01-14 20:22:23
categories: [Firewall]
tags: 
- IEEE
- Linux 
---

Okay so slightly misleading title as 802.1D-2004 didn't actually break my lab but it did cause a bit of head scratching as to why my lab wasn't working as expected. 

To summarise, I wanted to view all RSTP packets exchange in a small three switch topology. I didn't want to set up loads of port mirroring so I thought it would be best to create a LAB that connecting three Juniper vQFXs together through a single linux node with three bridges for each 'physical connection'; this would give me a single place to capture all traffic.

So an hour later (20 minute vQFX boot time = yay) I had configured very basic vQFXs to allow LLDP on all interfaces and enabled bridging on the Linux box. I was sure that I had configured Linux correctly as I had done this before but I wasn't seeing LLDP on either switch. After some captures on the Linux box I noticed DHCP traffic was making it to the bridg interface but LLDP wasn't getting past the two physical interfaces. The screenshot below shows first DHCP on br1 and then LLDP on eth0.

<div style="text-align:center;"><a href="/images/posts/2019/01/capture.png"><img src="/images/posts/2019/01/capture.png" width="720" ></a></div>

After some looking around I found an explanation and fix (<a href="https://thenetworkway.wordpress.com/2016/01/04/lldp-traffic-and-linux-bridges/">Shout-out</a>). To summarise LLDP packets weren't being forwarded because any Bridge should if following standards drop certain traffic as those destination MAC addresses are never intended to leave a LAN segment, and since bridges bridge LAN segments it makes sense that my LLDP packets were being dropped at the linux box. 

However this was a lab and not a LAN, so I quickly disabled this function after which lo and behold LLDP packets now appeared in my br1 capture.

<div style="text-align:center;"><a href="/images/posts/2019/01/capture2.png"><img src="/images/posts/2019/01/capture2.png" width="720" ></a></div>

I knew my next problem would likely be that I would have to do something similar to allow RSTP across br1 however as the capture shows this was already happening thanks to enabling LLDP. After having a very quick look into why this was, it turns out both LLDP and RSTP destination mac addresses were in the same restriction.

STP BPDU frames are sent to 01:80:c2:00:00:00 <br >
LLDP Frames are sent to 	01:80:c2:00:00:0E

Both of these addresses are covered by the reserved addresses list defined in 802.1D-2004 as shown below. And that is how the IEEE broke my lab, which is fair considering this standard is instrumental in how LANs actually work.

<div style="text-align:center;"><a href="/images/posts/2019/01/restrictions.png"><img src="/images/posts/2019/01/restrictions.png" width="520" ></a></div>

Hopefully I'll follow up in a couple of days with the lab and configurations used.