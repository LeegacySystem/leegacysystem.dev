---
title:  "Juniper Static, Aggregated and Generated Routes Study Notes"
date:   2019-03-21 17:21:00
categories: [Juniper]
tags: 
- Juniper 
- Routing
- JNCIS-ENT
---

The aim of this post is to cover personal study notes on a subsection of the Protocol Independent Routing <a href="https://www.juniper.net/uk/en/training/certification/certification-tracks/ent-routing-switching-track?tab=jncis-enterprise">JNCIS-ENT</a> exam objective.

So lets start by skipping ahead by a reasonable amount. The table below shows the default global routing preferences for the three types of routes. For my complete list (thus far) see <a href="https://commit-confirm.github.io/2018/Junos-Routing-Prefrences/">Here</a>


| Route Protocol/Source      	| Default Preference 	| Statement to Modify Default Preference 	|
|----------------------------	|--------------------	|----------------------------------------	|
| Static and Static LSPs     	| 5                  	| static                                 	|
| Aggregate                  	| 130                	| aggregate                              	|
| Generated                  	| 130                	| Generated                              	|


###### **Static Routes (SR)** 
You don't get much simpler than a good old static route, but in the name of completeness. A static route consists of a prefix to be routed and a next-hop action. For traffic to be forwarded the next-hop must be a valid next-hop, in that the hop exists as an active route in the routing table. A qualified next-hop or floating next hop has been covered previously in the JNCIA-Junos notes. But this is a secondary next-hop that depending on the routing preferences will become active immediately or if the current valid next-hop becomes unavailable by dropping from the routing table.

There are four options for the next-hop, excluding a valid IP address:

<ul style="list-style-type:disc">
  <li> Reject - Packet is dropped with an ICMP notification returned to sender </li> 
  <li> Discard- Packet is dropped with NO ICMP notification. </li>
  <li> Qualified Next-hop - Secondary next-hop</li>
  <li> No-readvertise - Prevents the route from being advertised in dynamic routing protocols </li>
</ul>  

###### **Aggregated Routes (AR)** 
ARs can be installed into the routing table to summarise smaller "contributing routes". An example would be:

Contributing Routes - 10.0.0.0/24, 10.0.1.0/24, 10.0.2.0/24, 10.0.3.0/24 <br>
Aggregate Route - 10.0.0.0/22

The condition for an AR to be valid is that at least one of the contributing routes must exist in the routing table as an active route. The benefit of ARs is to reduce routing table sizes across a network as dynamic routing protocols only advertise/recieve the summarised routes. An important not for ARs is that in the routing table they are installed with the next-hop as rejected, this is because the smaller contributing routes will match first in the routing decision due to their smaller prefix/preference. 

ARs can be installed into the routing table with the following information:

<ul style="list-style-type:disc">
  <li> Reject - This can be modified to discard. </li> 
  <li> Metric configured as aggregate statement. </li>
  <li> AS Path configured as aggregate statement. TBC</li>
  <li> Community configured as aggregate statement. </li>
</ul>  


###### **Generated Routes (GR)** 
GRs are very similar to ARs in that they both summarise routes. The difference is that with a GR the next-hop is actually valid as opposed to the AR reject action. This does mean that contributing routes must have a valid next-hop before being summarised in a GR. A common usecase for a GR would be the default gateway of a network stub.

An important and misleading note, both aggregate and genereated routes appear the same when looked at with the "show route" command. Both appear as aggregate routes ([Aggregate/130]), it is important to look at the next-hop to determine if the route is a GR or AR 