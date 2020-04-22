---
title:  "Junos BGP States Study Notes"
date:   2019-04-10 12:59:00
categories: [Juniper]
tags: 
- Juniper 
- Routing
- JNCIS-ENT
- BGP
---

This post will take a quick look into the BGP Finite State model.


<a href="/images/posts/2019/07/BGP_States.png"><img src="/images/posts/2019/07/BGP_States.png" width="720" >

#### **IDLE:**
This is the first state and essentially means a session is inactive waiting for a start event which can be manual or automatic. I'll need to look into Junipers definitions of a start event.

#### **Connect:**
After a start event BGP will try to establish a TCP connection. A session will remain in the Connect state until either a TCP session is formed or the TCP handshake failed.

#### **Active:**
Should the TCP handshake fail BGP will transition the session into the Active state and reattempt to form a TCP session. If this again fails BGP will pass the session back to the connect state, this process will repeat until a TCP handshake is established or the BGP session is set back to IDLE.

#### **OpenSent:**
Once the TCP session is established BGP will send an Open packet detailing some BGP information that should be negatiated between peers.

#### **OpenConfirm:**
A keepalive message is follow the Open message to confirm the peer recieved the Open packet. Once the keepalive packet is recieved it will transition to established.

#### **Established:**
All systems are go! The final and steady state for BGP is established. In this state routing information can be exchanged between peers. This is often the state to monitor for via SNMP or your other choice of monitoring poision. 