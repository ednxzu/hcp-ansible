# Architecture Guide

Hashistack-Ansible offers flexibility in deploying various environments, whether for development, testing, or production. This guide will help you understand the different architectures you can deploy with Hashistack-Ansible.

## Dev/Testing Deployment

If you're setting up a test environment, you can deploy each service on a single host. Here’s an example of a minimal inventory file:

```ini
[vault_servers]
test-server

[consul_servers]
test-server

[nomad_servers]
test-server

[nomad_clients]
test-server

[consul_agents]
```

In this setup, each service runs on a single host with no clustering and no redundancy. **This configuration is ONLY recommended for testing** as it provides no resiliency and will fail if any component goes down.

### Requirements

The only requirement for this setup is that the target host must have a network interface accessible via SSH from the deployment host.

### Dev/Testing Architecture

The architecture for this test setup looks like this:

```mermaid
graph LR;
  client[Client] -->|http| server{
    Vault Server
    Consul Server
    Nomad Server
  };
```

## Production Deployment

For production environments, it’s crucial to separate concerns and deploy services on different nodes. This ensures high availability and fault tolerance.

### Recommended Setup

- **Consul Servers:** An odd number (3 to 5) of nodes.
- **Vault Servers:** An odd number (3 to 5) of nodes.
- **Nomad Servers:** An odd number (3 to 5) of nodes.

A production-ready inventory file might look like this:

```ini
[vault_servers]
vaultnode1
vaultnode2
vaultnode3

[consul_servers]
consulnode1
consulnode2
consulnode3

[nomad_servers]
nomadnode1
nomadnode2
nomadnode3

[nomad_clients]
nomadclient1
nomadclient2
nomadclient3

[consul_agents]
...
```

### Production Architecture Diagram

Here’s what the architecture for a production setup might look like:

```mermaid
graph TD
subgraph c[ ]
direction LR
c1[<span style='min-width:40px;display:block;'><img src='../static/consul_500x500.png'width='40'height='40'/><span>] <--> c2 & c3 & c4 & c5
c2[<span style='min-width:40px;display:block;'><img src='../static/consul_500x500.png'width='40'height='40'/><span>] <--> c3 & c4 & c5
c3[<span style='min-width:40px;display:block;'><img src='../static/consul_500x500.png'width='40'height='40'/><span>] <--> c4 & c5
c4[<span style='min-width:40px;display:block;'><img src='../static/consul_500x500.png'width='40'height='40'/><span>] <--> c5
c5[<span style='min-width:40px;display:block;'><img src='../static/consul_500x500.png'width='40'height='40'/><span>]
end
subgraph v[ ]
direction LR
subgraph vn1[ ]
v1[<span style='min-width:40px;display:block;'><img src='../static/vault_500x500.png'width='40'height='40'/><span>] <--> cva1
cva1([<span style='min-width:40px;display:block;'><img src='../static/consul_white_500x500.png'width='40'height='40'/><span>])
end
subgraph vn2[ ]
v2[<span style='min-width:40px;display:block;'><img src='../static/vault_500x500.png'width='40'height='40'/><span>] <--> cva2
cva2([<span style='min-width:40px;display:block;'><img src='../static/consul_white_500x500.png'width='40'height='40'/><span>])
end
subgraph vn3[ ]
v3[<span style='min-width:40px;display:block;'><img src='../static/vault_500x500.png'width='40'height='40'/><span>] <--> cva3
cva3([<span style='min-width:40px;display:block;'><img src='../static/consul_white_500x500.png'width='40'height='40'/><span>])
end
vn1 <--> vn2
vn2 <--> vn3
vn3 <--> vn1
end
v -->|Service registration| c
subgraph ns[ ]
direction LR
subgraph ns1[ ]
n1[<span style='min-width:40px;display:block;'><img src='../static/nomad_500x500.png'width='40'height='40'/><span>] <--> nca1
nca1([<span style='min-width:40px;display:block;'><img src='../static/consul_white_500x500.png'width='40'height='40'/><span>])
end
subgraph nsn2[ ]
n2[<span style='min-width:40px;display:block;'><img src='../static/nomad_500x500.png'width='40'height='40'/><span>] <--> nca2
nca2([<span style='min-width:40px;display:block;'><img src='../static/consul_white_500x500.png'width='40'height='40'/><span>])
end
subgraph ns3[ ]
n3[<span style='min-width:40px;display:block;'><img src='../static/nomad_500x500.png'width='40'height='40'/><span>] <--> nca3
nca3([<span style='min-width:40px;display:block;'><img src='../static/consul_white_500x500.png'width='40'height='40'/><span>])
end
n1 <--> n2
n2 <--> n3
n3 <--> n1
end
ns -->|Service registration| c
subgraph nc[ ]
direction LR
subgraph ncn1[ ]
direction LR
nc1[<span style='min-width:40px;display:block;'><img src='../static/nomad_white_500x500.png'width='40'height='40'/><span>] <--> ncca1
ncca1([<span style='min-width:40px;display:block;'><img src='../static/consul_white_500x500.png'width='40'height='40'/><span>])
end
subgraph ncn2[ ]
direction LR
nc2[<span style='min-width:40px;display:block;'><img src='../static/nomad_white_500x500.png'width='40'height='40'/><span>] <--> ncca2
ncca2([<span style='min-width:40px;display:block;'><img src='../static/consul_white_500x500.png'width='40'height='40'/><span>])
end
subgraph ncn3[ ]
direction LR
nc3[<span style='min-width:40px;display:block;'><img src='../static/nomad_white_500x500.png'width='40'height='40'/><span>] <--> ncca3
ncca3([<span style='min-width:40px;display:block;'><img src='../static/consul_white_500x500.png'width='40'height='40'/><span>])
end
end
nc -->|Service registration| c
nc <--> ns
```
