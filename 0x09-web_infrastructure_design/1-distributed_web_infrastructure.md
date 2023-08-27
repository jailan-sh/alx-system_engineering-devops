# Distributed web infrastructure
- As the master-servers are going to be working based on a Active-Active set up, their configuration must be identical, therefore we need to add every additional element as the simple web infrastructure we had in the previous point. 
- The load is going to be managed through a load-balancer, which distributes the queries according to a Robin-Round algorithm.
- an additional server will be needed to serve a replica or slave server, helping to unload the masters servers reading queries.

-load-balancer is using a Round Robin algorithm distribution. Meaning the queries requested are distributed to every server sequentially one after another, after reaching the last one it will begin again from the first. and it isn't the best algorithm distribution.

- load-balancer is enabling an Active-Active set up.

- in order all users share the same level of information, database Primary-Replica (Master-Replica) is a mechanism which enables data of one database server (the master) to be replicated or to be copied to one or more computers or database servers (the slaves), replication process can either be synchronous or asynchronous.

- the primary node and the replica node, regarding the application, is that the primary database is regarded as the authoritative source, while the replica database is synchronized to it.
