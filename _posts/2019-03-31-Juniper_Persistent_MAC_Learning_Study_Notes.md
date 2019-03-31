---
title:  "Juniper Persistent MAC Learning Study Notes"
date:   2019-03-31 12:30:00
categories: [Juniper]
tags: 
- Juniper 
- Routing
- JNCIS-ENT
- MAC_Sec
- L2SEC
---

This will be a very short port looking into persistent MAC learning.

Persistent MAC learning (also known as sticky MAC) allows for a switch to retain dynamically learned MACs and their associated interfaces after a reboot of the system. Persistent learning has to be enabled as by default it is disabled. When coupled with MAC limiting methods covered previously persistent learning ensures that only trusted devices are connected to a switch port even after a reboot when any counters would have cleared.

It is important to clear any persistent MACs before moving them within your network. If you repatch a server to a new unused switch port it may come up, but should its previously active port turn back up its sticky entry will overide the current and would knock the server offline.

There are four main considerations when using persistent learning:
<ol>
  <li><i>Only access ports can be configured with stick MACs</i></li>
  <li><i>The interface cannot be part of a redundant trunk group</i></li>
  <li><i>The interface must not be configured with no-mac-learning</i></li>
  <li><i>The interface must not be configured with 802.1x auth</i></li>
</ol>

Persistent MAC learning is configured under "edit ethernet-switching-options secure-access-port interface ge-0/0/0.0" with the persistent-learning statement. To verify the MAC is persistent the "show ethernet-switching table" command can be used to display the type of entry in the forwarding table.