---
title:  "Juniper Virtual Labs - Ethernet-switching"
categories: [jekyll]
tags: [jekyll]
---

## **Juniper Virtual Labs - Ethernet-switching**

I wanted to write up a quick post on getting a virtual lab up and running for studying towards the JNCIS-ENT exam. I was lucky enough to go on the in-person juniper training course for JEX & JIR so I have physical lab examples that I wanted to run at home. To do this I choose to use Eve-NG as it seems to be gaining popularity and covers a reasonable amount of [supported images](http://www.eve-ng.net/documentation/supported-images). I'm not going to cover the installation/configuration of eve-ng as their documentation is very good. However, as a caution, the main downside to Eve vs GNS3 that I have found is simply there is less community discussion around Eve-ng.

#### **The problem**

In the JEX syllabus there is a section on Ethernet-switching. The very first lab covers this section and expects some switching functionality to work. I had originally configured two vSRXs to do this lab and got most of the way through. However as soon as I tried to run "show ethernet-switching table" I got no result.

<div style="text-align:center;"><a href="{{ site.url }}/images/posts/2018/01/vsrx-output.png"><img src="{{ site.url }}/images/posts/2018/01/vsrx-output.png" width="520" ></a></div>

<br>

After looking over the Juniper feature explorer I found that ethernet-switching is not available to the vSRX. I had seen discussions saying it was possible with the 17 code base, though the image I downloaded did not seem to work on Eve so I haven't tested this. 


#### **The solution**

I ended up spending more time than I would care to admit on this, I resorted to using the vQFX evaluation image provided by juniper (specifically: 15.1X53-D60.4). The trick here is to use both the VRE and VPFE in conjunction by connecting the em1. I was caught out here as I had originally tried this but I had not waited long enough for the RE and PFE to sync.

<div style="text-align:center;"><a href="{{ site.url }}/images/posts/2018/01/vqfx-topology.png"><img src="{{ site.url }}/images/posts/2018/01/vqfx-topology.png" width="520" ></a></div>

<br>

If your RE and PFE are connected as shown above, all you have to do is power them up and wait. On my home server they both powered up fairly fast (compared to vsrx), however it took another 10/15 minutes before they both started to work as expected. On your first attempt if you power them up and go for a 30 minute coffee/youtube mini binge, by the time you come back "show interface terse" should include xe-0/0/X interfaces. 

In order to test that basic switching was working as expected I created a test VLAN on both REs, put the connecting interface between REs (xe-0/0/2) into the vlan and created a L3 interface with an IP assigned at each end. I've included both full configurations below along with my test output. 

<div style="text-align:center;"><a href="{{ site.url }}/images/posts/2018/01/vqfx-testing.png"><img src="{{ site.url }}/images/posts/2018/01/vqfx-testing.png" width="630" ></a></div>

<br>

<div style="text-align:center;"><a href="{{ site.url }}/images/posts/2018/01/vqfx-output.png"><img src="{{ site.url }}/images/posts/2018/01/vqfx-output.png" width="630" ></a></div>

<br>

##### **_vQFX-RE1 configuration_**
```
root@vQFX-RE1# show configuration | display set | except "dhcp"
set version 15.1X53-D60.4
set system host-name vQFX-RE1
set system root-authentication encrypted-password "$1$VarABIj2$69bMxK8kQ/hdkAbUdIiam/"
set system root-authentication ssh-rsa "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA6NF8iallvQVp22WDkTkyrtvp9eWW6A8YVr+kz4TjGYe7gHzIw+niNltGEFHzD8+v1I2YJ6oXevct1YeS0o9HZyN1Q9qgCgzUFtdOKLv6IedplqoPkcmF0aYet2PkEDo3MlTBckFXPITAMzF8dJSIFo9D8HfdOV0IAdx4O7PtixWKn5y2hMNG0zQPyUecp4pzC6kivAIhyfHilFR61RGL+GPXQ2MWZWFYbAGjyiYJnAmCP3NOTd0jMZEnDkbUvxhMmBYSdETk1rRgm+R4LOzFUGaHqHDLKLX+FIPKcF96hrucXzcWyLbIbEgE98OHlnVYCzRdK8jlqm8tehUc9c9WhQ== vagrant insecure public key"
set system login user vagrant uid 2000
set system login user vagrant class super-user
set system login user vagrant authentication ssh-rsa "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA6NF8iallvQVp22WDkTkyrtvp9eWW6A8YVr+kz4TjGYe7gHzIw+niNltGEFHzD8+v1I2YJ6oXevct1YeS0o9HZyN1Q9qgCgzUFtdOKLv6IedplqoPkcmF0aYet2PkEDo3MlTBckFXPITAMzF8dJSIFo9D8HfdOV0IAdx4O7PtixWKn5y2hMNG0zQPyUecp4pzC6kivAIhyfHilFR61RGL+GPXQ2MWZWFYbAGjyiYJnAmCP3NOTd0jMZEnDkbUvxhMmBYSdETk1rRgm+R4LOzFUGaHqHDLKLX+FIPKcF96hrucXzcWyLbIbEgE98OHlnVYCzRdK8jlqm8tehUc9c9WhQ== vagrant insecure public key"
set system services ssh root-login allow
set system services netconf ssh
set system services rest http port 8080
set system services rest enable-explorer
set system syslog user * any emergency
set system syslog file messages any notice
set system syslog file messages authorization info
set system syslog file interactive-commands interactive-commands any
set system extensions providers juniper license-type juniper deployment-scope commercial
set system extensions providers chef license-type juniper deployment-scope commercial
set interfaces xe-0/0/2 unit 0 family ethernet-switching vlan members test
set interfaces em1 unit 0 family inet address 169.254.0.2/24
set interfaces irb unit 99 family inet address 192.168.7.1/30
set forwarding-options storm-control-profiles default all
set protocols igmp-snooping vlan default
set vlans default vlan-id 1
set vlans test vlan-id 99
set vlans test l3-interface irb.99
```

<br>

##### **_vQFX-RE2 configuration_**
```
root@vQFX-RE2# show configuration | display set | except "dhcp"

set version 15.1X53-D60.4
set system host-name vQFX-RE2 
set system root-authentication encrypted-password "$1$VarABIj2$69bMxK8kQ/hdkAbUdIiam/"
set system root-authentication ssh-rsa "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA6NF8iallvQVp22WDkTkyrtvp9eWW6A8YVr+kz4TjGYe7gHzIw+niNltGEFHzD8+v1I2YJ6oXevct1YeS0o9HZyN1Q9qgCgzUFtdOKLv6IedplqoPkcmF0aYet2PkEDo3MlTBckFXPITAMzF8dJSIFo9D8HfdOV0IAdx4O7PtixWKn5y2hMNG0zQPyUecp4pzC6kivAIhyfHilFR61RGL+GPXQ2MWZWFYbAGjyiYJnAmCP3NOTd0jMZEnDkbUvxhMmBYSdETk1rRgm+R4LOzFUGaHqHDLKLX+FIPKcF96hrucXzcWyLbIbEgE98OHlnVYCzRdK8jlqm8tehUc9c9WhQ== vagrant insecure public key"
set system login user vagrant uid 2000 
set system login user vagrant class super-user
set system login user vagrant authentication ssh-rsa "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA6NF8iallvQVp22WDkTkyrtvp9eWW6A8YVr+kz4TjGYe7gHzIw+niNltGEFHzD8+v1I2YJ6oXevct1YeS0o9HZyN1Q9qgCgzUFtdOKLv6IedplqoPkcmF0aYet2PkEDo3MlTBckFXPITAMzF8dJSIFo9D8HfdOV0IAdx4O7PtixWKn5y2hMNG0zQPyUecp4pzC6kivAIhyfHilFR61RGL+GPXQ2MWZWFYbAGjyiYJnAmCP3NOTd0jMZEnDkbUvxhMmBYSdETk1rRgm+R4LOzFUGaHqHDLKLX+FIPKcF96hrucXzcWyLbIbEgE98OHlnVYCzRdK8jlqm8tehUc9c9WhQ== vagrant insecure public key"
set system services ssh root-login allow
set system services netconf ssh
set system services rest http port 8080
set system services rest enable-explorer
set system syslog user * any emergency
set system syslog file messages any notice
set system syslog file messages authorization info
set system syslog file interactive-commands interactive-commands any
set system extensions providers juniper license-type juniper deployment-scope commercial
set system extensions providers chef license-type juniper deployment-scope commercial
set interfaces xe-0/0/2 unit 0 family ethernet-switching vlan members test
set interfaces em1 unit 0 family inet address 169.254.0.2/24
set interfaces irb unit 99 family inet address 192.168.7.2/30
set forwarding-options storm-control-profiles default all
set protocols igmp-snooping vlan default
set vlans default vlan-id 1
set vlans test vlan-id 99
set vlans test l3-interface irb.99



```