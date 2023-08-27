# Simple web stack
- The user would type the domain name, www.foobar.com, into their web browser.
- The DNS server would resolve the domain name to the IP address of the server.
- The user's web browser would connect to the server's IP address.
- The web server would send the website's files to the user's web browser.
- The user's web browser would render the website's files and display them to the user.

- A server: is Servers are physical machines (as hardwares), virtual machines or softwares (computer programs) that serve or provide functionality to other programs or devices called “clients”.
- A domain name server: is a server that translates domain names into IP addresses.
- A web server: is a software program that delivers web pages to users.
- A database: is a software program that stores data for the website.
- DNS record of www belongs to : a subdomain of the www.foobar.com.

## Issues with the simple web infrastructure
- One of the issues of having a simple web infrastructure, has to do with the SPOF (Single Point of Failure) where if component of the system fails, there is no backup that can support the continuity of the functionality of the system, bringing the whole system to a collapse by being unable to operate.

- Also, whenever some structure or node in the system needs to be repaired, the whole system has to be shut down, while the maintenance is done. Then, client requests cannot be attended during this period of time.

- Overload of traffic can be a risk to the server capacity. This, because there is no possibility to scale the service with additional servers as backup. Leading to a possible breakdown of the web page and client requests, as traffic surpasess servers capacity.
