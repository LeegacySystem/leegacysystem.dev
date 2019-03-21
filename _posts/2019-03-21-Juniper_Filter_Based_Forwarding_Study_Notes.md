---
title:  "Juniper Filter Based Forwarding Study Notes"
date:   2019-03-21 19:09:00
categories: [Juniper]
tags: 
- Juniper 
- Routing
- JNCIS-ENT
---

This is another cool one! To set the scene, Filter Based Forwarding in Juniper is essentially Policy Based Routing in Cisco. As a note I will skip over the details of firewall filters in this post.

In junos as well as permit/deny a firewall filter can be used to direct matching traffic to totally seperate routing instance or RIB group. This gives amazing control of the routing decision that would normally be taken and can be used to override dynamic routing protocols or load balancers where needed. For example the default action of a packet being routed based on its destination IP address can totally be flipped, the firewall filter can match the source address or destination port and forward to a routing table based on that!

This might be better exampled with example:

A network has two links, WAN1 and WAN2 with the WAN1 having lower latency but higher cost per mb. A network engineer can write a firewall filter that says if traffic is being sent to a known VOIP destination port, then forward traffic to the lower latency WAN1 link.

