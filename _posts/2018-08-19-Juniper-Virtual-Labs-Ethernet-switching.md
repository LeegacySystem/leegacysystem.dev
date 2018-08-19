---
layout: default
---

## **Juniper Virtual Labs - Ethernet-switching**

I wanted to write up a quick post on getting a virtual lab up and running for studying towards the JNCIS-ENT exam. I was lucky enough to go on the in-person juniper training course for JEX & JIR so I have physical lab examples that I wanted to run at home. To do this I choose to use Eve-NG as it seems to be gaining popularity and covers a reasonable amount of [supported images](http://www.eve-ng.net/documentation/supported-images). I'm not going to cover the installation/configuration of eve-ng as their documentation is very good. However, as a caution, the main downside to Eve vs GNS3 that I have found is simply there is less community discussion in Eve-ng.

</br>

#### **The problem**

In the JEX syllabus there is a section on Ethernet-switching. The very first lab looks at this section and expects some switching functionality to work. I had originally configured two vSRXs to do this lab and got most of the way through. However as soon as I tried to run "show ethernet-switching table" I got no result, after some digging around I also noticed "family ethernet-switching" was not available. 

IMAGE 1 
IMAGE 2

After looking at the feature explorer I found that ethernet-switching is not available to the vSRX 15 code base. I had seen discussions saying it was possible with the 17 code base, though the image I downloaded did not seem to work on Eve.


#### **The solution**

I ended up spending more time than I would care to admit on this, in the end I resorted to using the vQFX evaluation image provided by juniper (specifically: 15.1X53-D60.4). The trick here is to use both the VRE and VPFE in conjunction by connecting the em1, I was caught out here as I had originally tried this but not waited long enough for the RE and PFE to sync.

IMAGE 3

<div style="text-align:center;"><a href="{{ site.url }}/images/posts/2018/01/vqfx-topology.png"><img src="{{ site.url }}/images/posts/2018/01/vqfx-topology.png" width="150" ></a></div>


If your RE and PFE are connected as shown, all you have to do is power them up and wait. On my home server they both powered up fairly fast (compared to vsrx), however it took another 10/15 minutes before they both started to work as expected. On your first attempt if you power them up and go for a 30 minute coffee/youtube mini binge, by the time you come back "show interface terse" should include xe-0/0/X interfaces. 

To test basic switching was working as expected I created a test VLAN on both REs, put the connecting interface between REs into the vlan and created a L3 interface with an IP assigned at each end. I've included both full configurations below along with my test output. 
