---
title:  "Juniper Spanning Tree - Key STP Terms"
date:   2019-01-14 15:41:23
categories: [Juniper]
tags: 
- Juniper 
- STP 
---


It has been a while since I've last proepry studied Juniper which in turn also explains the lack of posting notes. Hopefully the gap between this post and the next will not be as long. 

The reason for this is post is to drill in key STP terms by giving more information than is probably required for the JNCIS-ENT. This is inteded to the be first chapter/post of the many that I will have to write to memorise STP and its flavours. 

<!-- Using the HTML List below as Jekyll list formating doesn't work as expected, need to fix at some point. -->

<ul style="list-style-type:disc">
  <li>Chapter 1: <a href="http://127.0.0.1:4000/2019/Juniper-Spanning-Tree-Key-STP-Terms/">Key STP Terms</a> </li> 
  <li>Chapter 2: TBC</li>
  <li>Chapter 3: TBC</li>
</ul>  

###### **Bridge ID** - A Unique identifier for a switch.

A unique bridge ID Is used to identify all switches participating in an STP topology. It is used to elect the root bridge (lowest bridge ID preferred) and is formed by combining the system MAC address and a configurable priority (default value 32k).

If all switches in a spanning tree topology have the same default Bridge ID priority this can cause a common problem. As the next tie braking metric is the lowest MAC address, typically the older/oldest switch in the network will become the root bridge as it  is likely to have the lowest MAC address. This should be a consideration and avoided.

```
Show spanning-tree bridge | match "Bridge ID"
```

###### **Root Bridge** - The elected switch with the lowest Bridge ID.  

There will only be one Root Bridge in a spanning tree topology. Any other bridges are considered non-root and each will build a shortest path to the Root Bridge blocking of any redundant ports.  As previously mentioned setting a bridge priority is the best way to influence the elected Root Bridge.
	
Root Protection is a spanning tree feature that can be used to protect the STP topology from being hijacked by a non-authorised bridges with a lower Bridge ID. When configured on interfaces which should not receive lower-priority/preferred BPDUs, the bridges will ignore them or perform the requested action.
```
Show spanning-tree bridge | match "Root ID"
```

###### **Root Path Cost** - The calculated cost to get to the Root Bridge.  

This value is a cumulative cost of all the links leading to the root bridge across a given path. Each bridge will add its own cost to the BPDU before sending further down the path (received path cost + port cost).

###### **Port Cost** - Every interface on a bridges as an assigned and configurable cost value.

This value is used as mentioned in the Root Path Cost calculation, it is added to the received path cost to form the root path cost (received path cost + port cost).  The value is configurable with a range from 1 to 200000000 with 1Ge being 20000. There are two iterations of the speed to cost values 802.1D-2004 defines the newer standard to account for faster interface speeds.

###### **Root Port** - A single port on every non-root bridges which is the closest to the Root Bridge.

After the root path costs have been calculated, each bridges designates the interface with the lowest cost as the root port.  There can only be one root port but in RSTP an alternate ports can exist, which is a path to the root bridges but with a calculated higher cost.
```
Show spanning-tree interfaces | match "root"
```
If no root port exists then that bridges is the Root Bridge. This is because the Root Bridge will not have any interfaces in the Root role.

###### **Bonus Round** - Checking the current switch to verify its root bridge status

```
show spanning-tree bridge | grep "Bridge|Root"
```

If the returned values are the same then the current Bridge is the Root Bridge of the topology