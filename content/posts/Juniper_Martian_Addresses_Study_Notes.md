---
title:  "Juniper Martian Addresses Study Notes"
date:   2019-03-21 18:13:00
categories: [Juniper]
tags: 
- Juniper 
- Routing
- JNCIS-ENT
---

Martian addresses are actually very simple. They are simply addresses that will never be installed into a Juniper routing table as doing so wouldn't make sense. An example of this would be the loopback addresses or multicast addresses. The one thing to note is that a network administartor can add prefixes to the martian list if they had any usecase to do so.

To view all martian addresses the command "show route martians table inet" can be used. The addresses for the default ipv4 table are listed below:

 <ol>
   <li>0.0.0.0/0 exact </li>
   <li>0.0.0.0/8 orlonger </li>  
   <li>127.0.0.0/8 orlonger </li>
   <li>192.0.0.0/24 orlonger </li>   
   <li>240.0.0.0/4 orlonger </li>
   <li>224.0.0.0/4 exact </li>   
   <li>224.0.0.0/24 exact </li>  
</ol> 


If you are more observant than I am; which to be honest would not be difficult, you may have noticed the default route 0.0.0.0/0 is included here. Even though the default route is considered a martian address, it is the exception to the rule as it is flagged as allowed. If you were to run the previous command you would 0.0.0.0/0 as allowed.
