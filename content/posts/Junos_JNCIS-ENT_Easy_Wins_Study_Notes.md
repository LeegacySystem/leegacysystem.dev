---
title:  "Junos JNCIS-ENT Easy Wins Study Notes"
date:   2019-04-10 15:50:00
categories: [Juniper]
tags: 
- Juniper 
- Routing
- JNCIS-ENT
---

This post will look over some areas I think will be easy wins for the JNCIS-ENT Exame.

#### **IEEE Standards:**
<ul>
	<li>802.1D - Spanning Tree</li>
	<li>802.1w - Rapid Spanning Tree (w = wapid)</li>
	<li>802.1ad - LACP</li>
</ul>

#### **IP Protocols:**
<ul>
	<li>6 - TCP</li>
	<ul>
		<li>Port 179 - BGP</li>
	</ul>
	<li>89 - OSPF</li>
	<li>124 - IS-IS over IP</li>
</ul>

#### **Preferred Preferences:**

STP Bridge Prority - Lower
Routing Preference - lower
OSPF DIR priority/RID - Higher
IS-IS DIS priority - Higher?
BGP local pref - Higher

#### **Default TTLs:**
iBGP TTL - 255
eBGP TTL - 1
VRRP TTL - 255?

#### **Random Bits:**

Ethernet switching - Learning, Forwarding, Filtering, Flooding, Aging

STP States - Blocking, Listening, Learning, Forwarding
RSTP States - Discarding, Learning, Forwarding

#### **Routing Preferences:**

| Route Protocol/Source      	| Default Preference 	| Statement to Modify Default Preference 	|
|----------------------------	|--------------------	|----------------------------------------	|
| Directly connected network 	| 0                  	| –                                      	|
| System routes              	| 4                  	| –                                      	|
| Static and Static LSPs     	| 5                  	| static                                 	|
| Static LSPs                	| 6                  	| –                                      	|
| OSPF internal route        	| 10                 	| OSPF                     			    	|
| IS-IS Level 1 Internal Router | 15                    | IS-IS
|
| IS-IS Level 2 Internal Router | 18                    | IS-IS
|
| RIP / RIPng                	| 100                	| RIP 			                         	|
| PIM                        	| 105                	| "Multicast Protocols Feature Guide"      	|
| Aggregate                  	| 130                	| aggregate                              	|
| Generated                  	| 130                	| Generated                              	|
| OSPF AS external routes    	| 150                	| OSPF external-preference               	|
| IS-IS Level 1 External Router | 160                   | IS-IS
|
| IS-IS Level 2 External Router | 165                   | IS-IS
|
| BGP (EBGP/IBGP)            	| 170                	| BGP preference, export, import         	|

