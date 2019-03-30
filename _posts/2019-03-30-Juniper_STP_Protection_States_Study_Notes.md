---
title:  "Juniper STP Protection States Study Notes"
date:   2019-03-30 19:02:00
categories: [Juniper]
tags: 
- Juniper 
- Routing
- JNCIS-ENT
- STP
- L2SEC
---

This post will take a quick look into the three types of STP Protection available in Juniper including an example diagram of where to use each.

#### **BPDU Protection:**
The first and arguably most important protection will prevent unexpected BPDUs from influencing the topology and SPF calulations. When enabled (typically on STP edge ports) BPDU protection will monitor an interface and when it sees a BPDU it will disable that interface to prevent malicous or unitentional network outages. 

To further explain an edge port is typically a server or end host, which typically wouldn't send BPDUs anyway so the edpe port status gives them the ability to shortcut the SPF process. If a user or attacked was to attached a switch to an edge port they could potentially cause loops.

As mentioned the default action for BPDU protect is to disable the offending interface until a network admin clears the error. The alternative is to havethe disable-timeoute statement is configured and once this timer expires, the port will be unblocked (FACT CHECK NEEDED).

BPDU protection can be used in STP, RSTP, VSTP and MSTP deployments, some key statements for STP configuration are:
<ul>
  <li><i>bpdu-block</i> – Enables BDPU protection on a switch not running spanning tree </li>
  <li><i>bpdu-block-on-edge</i> – Enable BDPU projection on a switch running spanning tree </li>
  <li><i>disable-timeout</i> – Change the timeout of a port being down after BDPU breach </li>
  <li><i>clear error bpdu interface</i> – Manually clear BPDU breach </li>
</ul>

#### **Loop Protection:**
LP is intrusive to the normal operations of STP for the sake of security. On a non-root bridge switch if a designated port changes state to down, the non-designated port would normally transition to designated and come up. With LP enabled this doesn't automatically happen, instead the  switch will alert that a non-designated port is trying to become designated for the admin to allow or disallow. LP should be used on non-designated ports that have a chance of becoming designated or root ports. 

If a port that should be receiving BPDUs and is in a loop protection state stops receiving BPDUs, it will go into **loop-inconsistent** until a BPDU is received again. 

#### **Root Protection:**
Protects against an unexpected switch with a higher root priority coming into the topology and taking the designated root bridge role. RP should be enabled on interfaces which should not receive superior BPDUs and not be elected as root ports. 

If a breach of RP is detected the offending port will be placed into a **root-prevented STP state (inconsistency state)** and block traffic. Once the superior BPDU stops being received the port automatically transitions back through listening, learning and finally forwarding. 

#### **Example Topology:**
Using the example below I will review which ports from the perspective of switch D should be configured with each protection under Juniper recommendation.

<a href="{{ site.url }}/images/posts/2019/01/capture.png"><img src="{{ site.url }}/images/posts/2019/05/STP_Protections.png" width="720" >

**BPDU Protect:** As mentioned previously edge ports should be configured for BPDU protection. This would result in ports 2, 3 in the example being BPDU protected.

**Loop Protect:** As previously mentioned LP should be configured on any port that has a chance of being a root or designated port. For switch 4 the only port that this may happen for is Port 1.

**Loop Protect:** As previously mentioned RP should be configured on any port that should not recieve a superior BPDU. In this example again ports 2 and 3 should not recieve any superior BPDUs. (FACT CHECK)

| Protection | Port |
| BPDU | 2,3 |
| Loop | 4 |
| Root | 2,3 | 