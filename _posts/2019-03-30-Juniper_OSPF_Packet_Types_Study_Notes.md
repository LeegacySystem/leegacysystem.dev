---
title:  "Juniper OSPF Packet Types Study Notes"
date:   2019-03-30 15:05:00
categories: [Juniper]
tags: 
- Juniper 
- Routing
- JNCIS-ENT
- OSPF
---

This post will take a quick look into the five types of OSPF packets. 

OSPF is a dynamic routing protocol used as an interior gateway protocol (IGP). Unlinke BGP which is implemented over TCP, OSPF is its own IP protocol (89) different from TCP or UDP. As such the protocol has its own packet formats which are all reviewed below. 

#### **OSPF Common Header:**
Each of the five OSPF packet types start with a common 24 byte header as shown below. This header identifies the OSPF version and packet type, along with the router and area ID of the sender. If implemented authentication will also be handled by the common header. 

<a href="{{ site.url }}/images/posts/2019/01/capture.png"><img src="{{ site.url }}/images/posts/2019/03/OSPF_Packets-Common Header.png" width="720" >

#### **OSPF Hello Packet (type 1):**
The hello packet is used for discover adjancies and form neighbours. The Network Mask, Hellow/Dead Intervals and options must all match for a neighbour relationship to form. These packets are sent periodcally out all interfaces including virtual links. In a multiaccess broadcast network hello packets will be sent to the multicast address of 224.0.0.5 which translates to all OSPF routers, 224.0.0.6 is all DR routers.

The diagram below shows the structure of a hello packet including the OSPF common header with dotted lines. Note how the common header defines the following packet as type 1.

<a href="{{ site.url }}/images/posts/2019/01/capture.png"><img src="{{ site.url }}/images/posts/2019/03/OSPF_Packets-Hello Packet.png" width="720" >

#### **OSPF Database Description Packet (type 2):**
The DDP is the second type of OSPF packet and are exchanged between two OSPF routers when the adjacency is forming. One or more of these packets will be sent to define and synchronise the link-state database between OSPF routers. THE DDP excahnge process involves one router acting as the master and the other as a slave for the exchange. The OSPF router with the higest Router ID will take the mastership role in the exchange.

<a href="{{ site.url }}/images/posts/2019/01/capture.png"><img src="{{ site.url }}/images/posts/2019/03/OSPF_Packets-DDP-Packet.png" width="720" >

#### **OSPF Link State Request (type 3):**
LSR packets are sent by an OSPF router after the DDP exchange when the router detects it is missing information from its link-state database. The LSR is sent to neighbours requesting the missing or more up-to-date inforamtion. An LSR can contain multiple requests for LSA inforamtion.

<a href="{{ site.url }}/images/posts/2019/01/capture.png"><img src="{{ site.url }}/images/posts/2019/03/OSPF_Packets-LSR_Packet.png" width="720" >

#### **OSPF Link State Update (type 4):**
LSUs are the flooding mechanism used to send Link-State Advertisements. Each LSU can carry on or mora LSAs one hop further than the origin. The follow OSPF packet type is used to acknowledge the reciept of an LSU, if no ack is recieved the LSU is sent again directly to the neighbour to ensure reliable transmission and a converged link-state database between all OSPF devices.

<a href="{{ site.url }}/images/posts/2019/01/capture.png"><img src="{{ site.url }}/images/posts/2019/03/OSPF_Packets-LSU_Packet.png" width="720" >

#### **OSPF Link State Acknowledgement (type 5):**
As previously mentioned an Acknowledgement has to be sent in response to an LSU to acknowledge that the reciever obtained all LSAs within the LSU. One packet can be used to acknowledge multiple LSAs.

<a href="{{ site.url }}/images/posts/2019/01/capture.png"><img src="{{ site.url }}/images/posts/2019/03/OSPF_Packets-LSA_(Ack)_packet.png" width="720" >

