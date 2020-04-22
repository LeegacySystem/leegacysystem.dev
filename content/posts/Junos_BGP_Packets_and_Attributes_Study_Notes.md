---
title:  "Junos BGP Packets and Attributes Study Notes"
date:   2019-04-10 15:20:00
categories: [Juniper]
tags: 
- Juniper 
- Routing
- JNCIS-ENT
- BGP
---

This post will skim over BGP packets and attributes.

#### **BGP Packet Types:**

There are five types of packets in BGP:
 <ol>
   <li>Open </li>
   <li>Keepalive </li>  
   <li>Notification </li>
   <li>Update </li>   
   <li>Refresh </li>
</ol> 

#### **BGP Attributes:**

There are four categories of attributes with different types in each:

<ol>
    <li>Well-known Mandatory - These attributes must be present in any BGP update.</li>
    <ol>
        <li>Origin</li>
        <li>AS Path - Loop protection</li>
        <li>Next-Hop</li>
    </ol>
    <li>Well-known Discretionary - Must be in every BGP implementation but is not required in every BGP update.</li>
    <ol>
        <li>Local Prefrence</li>
        <li>Atomic Aggregator</li>
    </ol>
    <li>Optional Transitive - If present it should be passed long to the next peers.</li>
    <ol>
        <li>Aggregator</li>
        <li>Community (4 octets)</li>
        <li>Extended Community (8 octets)</li>
    </ol>
    <li>Optional Non-Transitive - Doesn't have to be updated to peers.</li>
    <ol>
        <li>Multi Exit Discriminator (MED)</li>
        <li>Originator ID</li>
        <li>Cluster List</li>
        <li>Multiprotocol Reachable NLRI</li>
        <li>Multiprotocol Unreachable NLRI</li>
    </ol>
</ol>


#### **BGP Route Selection:**
<ol>
    <li>Highest Local Preference First</li>
    <li>Shortest AS Path</li>
    <li>Lowest Origin Value</li>
    <li>Lowest MED value</li>
    <li>Lowest IGP metric as AS exit</li>
    <li>Longest uptime of eBGP peer or lowest router ID</li>
    <li>Lowest Peeer IP Address</li>
</ol>