---
title:  "Juniper IS-IS Study Notes"
date:   2019-03-12 17:41:23
categories: [Juniper]
tags: 
- Juniper 
- IS-IS
- JNCIS-ENT
---

## **First draft notes, likely to be messy/missing information**

IS-IS or Intermediate System to Intermediate System is an exam objective in the <a href="https://www.juniper.net/uk/en/training/certification/certification-tracks/ent-routing-switching-track?tab=jncis-enterprise">JNCIS-ENT</a> curriculum and a routing protocol I had never actually come across before. At the time when I studied the CCNA and CCNP IS-IS was mentioned but never looked at in detail, this may have changed by now.

The interesting thing about IS-IS is that was inteded to superceed OSPF once the OSI model became widely adopted. As IS-IS was originally developed a long time ago and the OSI model never really overtook TCP/IP there are some legacy concepts in IS-IS that newer engineers like myself wont understand/recognise. One being CLNP or Connectionless-Mode Network Protocol which when looking at the name was the OSI model replacement for UDP in TCP/IP. CLNP traffic was also intended to be sent across ISO addressing another largely forgotten concept.

One of the reasons IS-IS is still used today and wasn't largely left behind like the bulk of the OSI model is that it is comparatively easy to expand on due to TLVs which I'll cover. 

As IS-IS was inteded to replace OSPF they both have lots in common with each other. Firstly IS-IS is an interor gate protcol (IGP) intended to route insde an autonoumous system. Both protocols are considered link-state based and form adjacenies to build their link state databases evne using the same shortest path first algorithm. Both protocols elected a designated router based on prorities to reduce protocol chatter. Additionally both protocols have the concept of Areas with IS-IS adding the concept of levels. While the similarities sound great from a learning perspective, there are some big differences between the two which are covereted below.

###### **ISO Addressing** 
ISO addresses can be difficult to look at but actually aren't hugely complicated. Each ISO address points to a unique Network Service Access Point (NSAP). In addition to this each Network Entity has a "Network Entity Title", a special address broken down blow.

<div style="text-align:center;"><a href="/images/posts/2019/02/ISO_Address.png"><img src="/images/posts/2019/02/ISO_Address.png" width="320" ></a></div> 

<ul style="list-style-type:disc">
  <li>AFI - Autority and Format ID: In the past an authority such as ARIN/RIPE would hand out NSAP addresses however this doesn't happen anymore. The 49.* is the ISO equivalent to a private address. </li> 
  <li>Area ID: This is a similar concept to OSPF, the example area ID would be 1 here.</li>
  <li>System ID:  This is a unique identified, common practice is to use the loopback IP address (192.168.1.1). </li>
  <li>Selctor:  Also known as the NSEL, it is similar to a port/socket in IP. 00 address identifies the device itself. </li>
</ul>  

It is important to note I did not include the Domain ID in my example. The domain ID is mentioned in the Juniper configuration I haven't come across it in my studies so I don't belive it will be in the JNCIS-ENT exam.

###### **IS-IS Area & Levels** 
One of the major differences between OSPF and IS-IS is Levels. IS-IS autonoumous systems can be broken down into either a Level 1 or Level 2 domain. Areas are also used in IS-IS and can increment continually as long a the areas are contigous. Level 1 domains are like totally stubby areas in OSPF. A Level 1 router can only route within the area while a Level 2 router will have an "attached bit" set that will cause Level 1 routers to generate a default route via the Level 2 router.

A router can operate a Level 1 and Level 2 router at the same time. These devices act as level boundaries routing between areas. Level 2 can be thought of like area 0 in OSPF as it is the backbone performing inter-area routing were as level 1 is doing intra-area routing.

Level 1 paths are preferred over Level 2 paths. 

###### **IS-IS Packet Types** 

1) Link State PDUs (LSP) - 
These packets are flooded perodically *within* an area to ensure link-state database information refreshes. A Link-State PDU consists of the System ID (6 Bytes), Circuit ID (1 Byte) and a Link-State PDU Number (1 Byte). These PDUs describe reachable addresses and identify Adjacencies and their states.

2) Hello PDU (IIH) -
Also known as the IIH packet, these are used for neighbor discovery and to maintain adjacencies. OSPF forces the dead/hold timer to match between two neighbors but IS-IS does not, each router will adhere to its neighbors timer. There are seperate hello types for broadcast and P2P networks.

The default Hello/Hold times in Juniper is 9/27 seconds for standard routers and 3/9 for the DIS router.

3) Complete Sequence Number PDU (CSNP) -
This PDU type contains a description or the headers of all the link-state PDUs in the database and is sent periodically on LANs. If a router recieves and comapres a CSNP to its own database and notices missing information it will request the missing LSPs using the next PDU type.

4) Partial Sequence Number PDU (PSCP) -
These types of PDU are sent for two reason; firstly to acknowledge receipt of an LSP. Secondly to request a missing LSP to fill in a gap within the senders routing tables


###### **IS-IS DIS** 
TBC

The Designated Intermediate System or DIS is similar to DR in OSPF. Unlike a DR there is no backup of the DIS, and it is simply a psuedonode that advertises to all attached routers. In IS-IS every router forms an adjacency with every other router, not just the DIS. Every router will advertise a single link to the pseudonode, including the DIS device itself.

The DIS is elected based first on prority (high preferred default is 64). The prority can be set between 0 and 127 and when tied the higher MAC address wins. If a router with a higher prority comes into the network it will become the DIS.

###### **IS-IS TLVs** 
TBC 

TLV = Type, Length, Value.



###### **IS-IS Metrics** 
TBC 

The default behaviour for IS-IS metrics is to have a maximum interface metric value of 63 and a maximum path metric of 1023. 
Wide metrics were later added to increase the values available.

Rather than set every interface metric a reference metric can be used on speed. IS-IS is also capable of factoring in Delay, Cost and something else?