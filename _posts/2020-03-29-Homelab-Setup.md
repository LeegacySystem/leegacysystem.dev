
---
title:  "CoreDNS Homelab Setup"
date:   2020-03-29 14:40:00
categories: [Docker]
tags: 
- Docker
- DNS
- Homelab
---

# CoreDNS Homelab Setup
Well it turns out Coronavirus is great studying as there's literally nothing else to do, apart from play games and watching tv....

Anyway this post will go over my notes on setting up CoreDNS for DNS resolution within my home network. The post will focus on Docker along with DNS principles.

**super important tldr** The hardest thing about using CoreDNS is not typing or saying CoreOS, super annoying habbit. 

## CoreDNS
CoreDNS is designed to be a lightweight, DNS Server written the Go programming language. CoreDNS graduated from the Cloud Native Computing Foundation in 2019 following Promethues and Kubernetes, which relies heavily on CoreDNS as a default DNS provider. 

### CoreDNS Configuration
Three default zone files:
1) CoreDNS corefile
2) Forward lookup zone
3) Reverse lookup Zone

A zone file is simply the file which defines each record, a mapping of IP address to host names.


#### Basic Configuration Tests
I don't require anything complicated so for now I will focus on the Corefile. Looking over the documentation there are some config snippets provided which I;ve used to verify basic operations.

**corefile**
```
. {
   chaos CoreDNS-001
}

```

I used this corefile with the following compose:

**docker-compose**
```
version: "3.7"
services:
  coredns:
    image: coredns/coredns
    container_name: lab_coredns
    hostname: coredns
    ports:
      - 53:53/udp
      - 53:53/tcp
    volumes:
      - ./coredns:/root/
    command: "-conf /root/corefile"
    networks:
      homelab:
        aliases:
        - "coreDNS"
```

**Testing**
```
⇒  docker-compose up coredns                         
Starting lab_coredns ... done
Attaching to lab_coredns
lab_coredns       | .:53
lab_coredns       | CoreDNS-1.6.9
lab_coredns       | linux/amd64, go1.14.1, 1766568


--

⇒  dig CH txt version.bind @localhost

; <<>> DiG 9.11.14-RedHat-9.11.14-2.fc31 <<>> CH txt version.bind @localhost
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 58270
;; flags: qr rd; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 4096
; COOKIE: d14a96c110ad8ef1 (echoed)
;; QUESTION SECTION:
;version.bind.                  CH      TXT

;; ANSWER SECTION:
version.bind.           0       CH      TXT     "CoreDNS-001"

;; Query time: 0 msec
;; SERVER: 127.0.0.1#53(127.0.0.1)
;; WHEN: Sun Mar 29 13:00:40 BST 2020
;; MSG SIZE  rcvd: 89
````

#### Global zone
As the previous configuration doesn't really do much but return a string for a specific query its time to move on. One thing to note that everything between {} brackets counts as a zone. I need to modify this root zone for it to allow non-defined zone queries be forwarded to external DNS servers.

```
.:53 {
    forward . 8.8.8.8 9.9.9.9
    log
    errors
}
```
This global zone file will for all matching queries forward them to the public Goggle DNS servers. Along with logging errors. 

#### Private zone
Next up is to add a second zone which defines the homelab enviroment.

```
.:53 {
    forward . 8.8.8.8 9.9.9.9
    log
    errors
}

⇒ homelab.host:53 {
    file /root/homelab.db
    log
    errors
}
```
The private zone defined here is actually very similar to the global zone with only two real diferences. Now any query that comes in relating to a host which belongs in the ⇒ homelab.host zone will trigger a lookup in the homelab.db file, which doesn't exist yet. 

#### Defining zone records
Creating the homelab.db and defining the records as below:
```
⇒ homelab.host.        IN  SOA coredns.⇒ homelab.host. dummy-email.⇒ homelab.host. 1585484552 7200 3600 1209600 3600
```
```
1) *⇒ homelab.host.* 				- Zone
2) *SOA*  								- Start Of Authority record type
3) *coredns.⇒ homelab.host.* 		- SOA server for zone (this server)
4) *dummy-email.⇒ homelab.host.* 	- fake email
5) *1585484552* 						- Unique serial (unix timestamp)
6) *7200* 								- SOA Refresh Rate
7) *3600* 								- SOA Retry Rate
8) *1209600* 							- SOA Expiration hold time
9) *3600* 								- Records default TTL
```
There are some interesting values in here, a quick Google of recommended times ([RFC 2308](https://tools.ietf.org/html/rfc2308)) shows that the defaults for SOA refresh/retry/expiry rates are: 30m/15m/7d/20m. However this is a dated document and for homelab usage those defaults are a little extreme, I don't want to wait 20 minutes just for TTLs to expire.

Next up is to define the rest of the host file, you can see its structure in the previously linked RFS.
**homelab.db**
```
⇒ homelab.host.        IN  SOA coredns.⇒ homelab.host. dummy-email.⇒ homelab.host. 1585484552 7200 3600 1209600 3600

future_stuff.⇒ homelab.host.    IN  A   192.168.0.22
desktop.⇒ homelab.host.    IN  A   127.0.0.1
*.⇒ homelab.host. IN  A   127.0.0.1

#*.⇒ homelab.host. IN  CNAME   desktop.⇒ homelab.host
```

My homelab.db file only has three entires in it, the first indicates and queries to "*future_stuff.⇒ homelab.host*" should go to *192.168.0.22*. This is just an example as for now all my services live on my desktop in seperate containers, although this will change in future. The second entry defines a mapping for *desktop.⇒ homelab.host* to *127.0.0.1*. Lastly the final CNAME entry maps everything else to the previously defined A record host name.

##### Testing each zone:
After starting the contianer I should be able to run dig commands from my host command prompt:
```
# Showing the global zone works
⇒  dig @127.0.0.1 google.com | grep google     
; <<>> DiG 9.11.14-RedHat-9.11.14-2.fc31 <<>> @127.0.0.1 google.com
;google.com.                    IN      A
google.com.             58      IN      A       172.217.169.14

# Showing the desktop record
⇒  dig @127.0.0.1 desktop.⇒ homelab.host | grep commit
; <<>> DiG 9.11.14-RedHat-9.11.14-2.fc31 <<>> @127.0.0.1 desktop.⇒ homelab.host
;desktop.⇒ homelab.host.   IN      A
desktop.⇒ homelab.host. 0  IN      A       127.0.0.1

# Showing the place holder record
⇒  dig @127.0.0.1 future_stuff.⇒ homelab.host | grep future
; <<>> DiG 9.11.14-RedHat-9.11.14-2.fc31 <<>> @127.0.0.1 future_stuff.⇒ homelab.host
;future_stuff.⇒ homelab.host. IN   A
future_stuff.⇒ homelab.host. 0 IN  A       192.168.0.22
```


### Summary
This has been a very basic coverage of CoreDNS going over my usecase. In future I'll likely build on this using CoreDNS and Kubernetes together, possibly with other provider types such as Git and other modules. 

## Note
The CNAME wildcard entry didn't work, and I couldn't be bothered spending time on it so I change the wildcard CNAME to an A record