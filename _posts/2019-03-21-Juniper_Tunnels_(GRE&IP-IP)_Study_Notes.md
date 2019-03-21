---
title:  "Juniper Tunnels (GRE & IP-IP) Study Notes"
date:   2019-03-21 19:22:00
categories: [Juniper]
tags: 
- Juniper 
- Routing
- JNCIS-ENT
---

When a network can't support a specific traffic type often the solution is to use tunnels. A tunnel is an overlay in that it encapsulates and decapsulates unsupported packets that in a packet type the underlying network can support. The tunnels in this post do not add security, despite some Juniper tech library articles saying otherwise (I hope I'm right). Tunnels also aren't stateful, this means that each tunnel end-point is unaware if the opposing point is reachable.

Tunnels can be thought of as path vector in a sense similar to BGP. This is because the two end-points must be able to communicate with each other to pass traffic through their tunnels. 

The two tunnels covered in JNCIS-ENT are:
<ol>
  <li> GRE </li>
  <li> IP-IP </li>
</ol>

###### **GRE** - Generic Routing Encapsulation.
Gre can be used to encapsulate and send packets over the internet that otherwise would be droped. Examples are RIP/OSPF and multicast traffic. 

Each router participating as GRE end points can't detect if the other side is down without another mechanism such as BFD. This is because as previously mentioned GRE is stateless in that it does not hold tunnel state/availability information. GRE encapsulation overhead takes up 24 Bytes, as a result the MTU on GRE links will/should be adjusted to 1476 or lower to avoid dropped packets. 

A GRE interface is identifable as it follows the gr-0/0/0 notation. There is also a gre interface that is created and managed by Junos.

###### **IP-IP** - IP-over-IP 
These tunnels can be identified by their ip-0/0/0 notation when configured by an admin. the ip-ip interface is created and managed by Junos.