---
title:  "Juniper Routing Instances and RIB Groups Study Notes"
date:   2019-03-21 18:35:00
categories: [Juniper]
tags: 
- Juniper 
- Routing
- JNCIS-ENT
---

Just to get it out there, routing instances are awesome! An instance is a container that can have its own routing table, routing options/policies and interfaces. They essentially break a switch or router down into segments that can be used for difference customers or traffic types etc. There are different types of instances each with their own usecases and caveats. On every junos device the default routing instance is the master instance. Additionally an instances can have multiple tables for ipv4, ipv6 etc. An example is the master.inet0 table for ipv4 and the master.inet6 table for ipv4. An important not is that one routing instance can only have one instance of each protocol (BGP/OSPF etc). 

The coolest instance type imo has to be the virtual router instace. This type has a direct 1:1 mapping of the interfaces, which means any associated interfaces and their directly connect networks are placed into the custom instance. This allows for totally segmented topologies to exist on the same hardware, with filter based forwarding able to route between the master and custom instance.

However not all instance types are equal. The forwarding instance type doesn't have the 1:1 mapping of interfaces and relies on RIB groups along with filter based forwarding to pass traffic. 

A RIB group can use routing policies to import routes between one or more grouped routing tables. When configuring RIB groups the first table specified takes the primary table role and any subsequent groups are secondaries. 

The twelve routing instance types:
<ol>
  <li> Ethernet VPN (EVPN MX Series only) </li>
  <li> Forwarding  </li>
  <li> Internet MCast over MPLS  </li>
  <li> Layer 2 Backhaul VPN (MX Series only) </li>
  <li> Layer 2 Control (MX Series only) </li>
  <li> Layer 2 VPN </li>
  <li> MPLS Forwarding </li>
  <li> Non-forwarding </li>
  <li> Virtual-Router </li>
  <li> Virtual Switch </li>
  <li> VPLS </li>
  <li> VRF </li>
</ol>