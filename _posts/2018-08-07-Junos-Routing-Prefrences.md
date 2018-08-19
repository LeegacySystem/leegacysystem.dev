---
title:  "Junos Routing Notes"
date:   2018-08-16 17:00:00
categories: [Juniper]
tags: [Juniper Routing JNCIA]
---

## **Junos Default Route Prefrence Overview**

This is a short post on juniper default route prefrences for specific protcols seen in the routing table. Routes with a lower prefrence are preferred over higher.

<br/>

#### **Summary:**

| Route Protocol/Source      	| Default Preference 	| Statement to Modify Default Preference 	|
|----------------------------	|--------------------	|----------------------------------------	|
| Directly connected network 	| 0                  	| –                                      	|
| System routes              	| 4                  	| –                                      	|
| Static and Static LSPs     	| 5                  	| static                                 	|
| Static LSPs                	| 6                  	| –                                      	|
| OSPF internal route        	| 10                 	| OSPF                     			    	|
| RIP / RIPng                	| 100                	| RIP 			                         	|
| PIM                        	| 105                	| "Multicast Protocols Feature Guide"      	|
| Aggregate                  	| 130                	| aggregate                              	|
| OSPF AS external routes    	| 150                	| OSPF external-preference               	|
| BGP (EBGP/IBGP)            	| 170                	| BGP preference, export, import         	|


###### *source:https://www.juniper.net/documentation/en_US/junos/topics/reference/general/routing-protocols-default-route-preference-values.html*


<br/>

#### **Notes:**

* In Junos EBGP routes are always perfered of IBGP routes despite the fact they both have the same prefrence of 170.
* System routes and Kernel routes appear to be obsolete (need to verify).