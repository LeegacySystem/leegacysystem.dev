---
layout: default
---

## Junos Routing Notes

This post is a review of Juniper Static Routing.
Types:

	1. Discard
	   In Cisco Terms this is a null route with no ICMP reject notification, this is typically used for advertising summary/aggergate routes to neighboring devices. An example of this would be:

	   Local routes: 10.10.0.0/25 & 10.10.0.128/25 <<- Traffic matches and is passed to relevant next hops
	   Aggregate discard route: 10.10.0.0/24 <<- Routing policy matched

	   In the example above the aggregate discard route can be given to a routing protocol (ospf/bgp) to advertise to neighbours as it exists in the routing table but packets match the longer prefixes before being discarded. An important note is that this type of aggregated advertisement only works when combining smaller subnets. For example if you had 10.10.0.0/24 in your local routing table and tried to create smaller discard routes, traffic in those networks would be discarded as the /25 prefixes takes precidance over the /24:

	   Discard route: 10.10.0.0/25 & 10.10.0/128/25 <<- Matched with traffic being discared
	   Local route: 10.10.0.0/24 <<- Routing policy matched but traffic being blacked holed.

	2. Reject
		This type is similar to a discard but instead sends an ICMP reject

	3. Forwarding
		This type of next hop determines where traffic should be forwarded. In a LAN (multiaccess) network the next-hop IP address will be resolved to a physical mac address via arp however in a point-to-point link the next-hop can be an interface.

Forwarding next-hop qualified:

	1. Resolve
		This qualifier can be used with a next hop to allow Junos to take indirect next-hop addresses and recursively resolve those addresses if possible. This is done in Cisco by default which would explain why it is a strange concept to grasp. I can see this being used in a multirouter scenario that has an IGP forming an interior network but and a static route is needed on a local router to a remote next-hop which isn't a directly connected network, example below;

````
		R1-inet.0
		10.10.10.4/30 [ospf]
		 > *10.10.10.2

		+--------------+                          +--------------+                         +--------------+                  +
		|              |10.10.10.1      10.10.10.2|              |10.10.10.5     10.10.10.6|              |.1                |
		|   Router#1   +-------------------------->   Router#2   +-------------------------+   Router#3   +------------------+
		|              |      10.10.10.0/30       |              |      10.10.10.4/30      |              |   192.168.0.0/24 |
		+--------------+                          +--------------+                         +--------------+                  +

		static{
		  route 192.168.0.0/24 {
		   next-hop 10.10.10.6;
		   resolve
		  }
		}
````

	2. Qualified next-hop
		This qualifier allows for static routes to have limited failover capability should there be more than one possible next-hop to the same network. There can be a list of quallified next-hops with each destination having its own prefrence. Should a hop be present/resolved in the routing table then it qualifies, the prefrence can be used for more control over the active route. A value of 5 is the default prefrence for a static route as defined by juniper, see the example below; 
````
                                                     | Router#1 show routing-options
                                                     |   static {
                                                     |     route 0.0.0.0/0 {
                                                     |       next-hop 10.10.10.1;
                      +--------------+               |       qualified-next-hop 10.10.10.5; {
                   .2 |              | .6            |       prefrence 4;
              +-------+   Router#1   +-------+       |      }
              |       |              |       |       |     }
              |       +--------------+       |       +-------------------------------------------+
              |                              |
              |                              |
10.10.10.0/30 |                              | 10.10.10.4/30
              |                              |
    1Mbps     |                              |    100Mbps
              |                              |
              |.1                            |.5
      +-------v------+                +------v-------+
  	  |              |                |              |
  	  |   Router#2   |                |   Router#3   |
  	  |              |                |              |
  	  +-------+------+                +------+-------+
  		      |                              |
              |                              |
              |                              |
              |                              |
              |                              |
              |                              |
              |                              |
      +-------v------------------------------v-------+

                         Internet
````

		In the example router 1 will send all internet bound traffic out the 100Mbps link via **10.10.10.5**, this is because it has a lower prefrence than the default static route of 5. Should the 100Mbps link be disconnected for any reason, the *10.10.10.1* will become the active route as 10.10.10.4/30 network will no longer be directly connected.

To Be Continued!