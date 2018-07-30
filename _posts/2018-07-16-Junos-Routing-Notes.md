---
layout: default
---

## Junos Routing Notes

This post is a review of Juniper Static Routing statements, mainly focusing on these three types:

1. Discard
2. Reject
3. Forwarding (next-hop)

<br/>

#### **1. Discard**

In Cisco Terms this is a null route with no ICMP reject notification, this is typically used for advertising summary/aggregate routes to neighboring devices. An example of this would be:

Local routes: <br> **10.10.0.0/25** <br> **10.10.0.128/25** | Aggregate discard route: <br> **10.10.0.0/24**  

Both /25 local routes can be aggregated into a single /24.

In the example above the aggregate discard route can be given to a routing protocol (ospf/bgp) to advertise to neighbours. This works because it exists in the routing table and packets match the longer local prefixes with valid next-hops before being discarded. An important note is that this type of aggregated advertisement only works when combining smaller subnets. For example, if you had 10.10.0.0/24 in your local routing table and tried to create smaller discard routes, traffic in those networks would be discarded as the /25 prefixes takes precedence over the /24:

discard routes: <br> **10.10.0.0/25** <br> **10.10.0.128/25** <br> Longest prefix match, packets discarded | local valid route: <br> **10.10.0.0/24** <br>  <br> Valid prefix ignored due to /25s

<br/>

#### **2. Reject**

This type is similar to a discard however, instead sends an ICMP reject. A different type value may be used in the ICMP message depending on if the Network or Host is unavailable for the router.

<br/>



#### **3. Forward**
This type of next hop determines where traffic should be forwarded. In a LAN (multi-access) network the next-hop IP address will be resolved to a physical mac address via arp however, in a point-to-point link the next-hop can be an interface.

###### **Next-hop modifiers** <br/>
__*Resolve*__
This qualifier can be used with a next hop to allow Junos to take indirect next-hop addresses and recursively resolve those addresses if possible. This is done in Cisco by default which would explain why it is a strange concept to grasp. I can imagine this being used in a multirouter scenario that has an IGP which is forming an interior network and a static route is needed on a local router to a remote next-hop which isn't a directly connected network, the example below;

```
          +--------------+                      +  R1+inet.0
          |              |                      |  10.10.10.4/30 [ospf]
          |   Router#1   |                      |  2^ *10.10.10.2
          |              |                      |  .6;
          +------+-------+                      |  static{
                 |                              |    route 192.168.0.0/24 {
              .1 |                              |     next+hop 10.10.10.6;
                 |                              |     resolve
                 |                              |    }
                 | 10.10.10.0/30                |  }
                 |                              +-------------------------+
              .2 |
                 |
          +------+-------+
          |              |
          |   Router#2   |
          |              |
          +------+-------+
                 |
              .5 |
                 |
                 |
                 | 10.10.10.4/30
                 |
              .6 |
                 |
          +------+-------+
          |              |
          |   Router#3   |
          |              |
          +------+-------+
                 | .1
                 |
                 |
          +------+-------+
           192.168.0.0/24


```
<br/>
__*Qualified Next-hop*__
This modifier allows for static routes to have a limited failover capability should there be more than one possible next-hop to the same network. There can be a list of qualified next-hops, with each destination having its own preference. Should a hop be present/resolved in the routing table, then it qualifies, route preference can be used for more control over the active route. A value of 5 is the default preference for a static route as defined by juniper and lower values are preferred. See the example below; 

````
                                          + Router#1 show routing+options
                                          |   static {
                                          |     route 0.0.0.0/0 {
                                          |       next hop 10.10.10.1;
           +--------------+               |       qualified next hop 10.10.10.5; {
        .2 |              | .6            |       preference 4;
       +---+   Router#1   +---+           |      }
       |   |              |   |           |     }
       |   +--------------+   |           +----------------------------------------
       |                      |
       |                      |
       | 10.10.10.0/30        | 10.10.10.4/30
       | 1Mbps                | 100Mbps
       |                      |
       |                      |
    .1 |                   .5 |
+------+-------+       +------+------+
|              |       |             |
|   Router#2   |       |   Router#3  |
|              |       |             |
+------+-------+       +------+------+
       |                      |
       |                      |
       |                      |
       |                      |
       |                      |
+------+----------------------+------+

                Internet

````

In the example router 1 will send all internet bound traffic out the 100Mbps link via **10.10.10.5**, this is because it has a lower preference than the default static route of 5. Should the 100Mbps link become disconnected for any reason, the *10.10.10.1* will become the active route as 10.10.10.4/30 network will no longer be directly connected.

