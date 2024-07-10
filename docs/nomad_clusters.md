# Deploying a Nomad cluster

This documentation explains each steps necessary to successfully deploy a Nomad cluster using the ednz_cloud.hashistack ansible collection.

## Prerequisites

You should, before attempting any deployment, have read through the [Quick Start Guide](./quick_start.md). These steps are necessary in order to ensure smooth operations going forward.

## Variables

### Basics

First, in order to deploy a nomad cluster, you need to enable it.

```yaml
enable_nomad: "yes"
```

Selecting the nomad version to install is done with the `nomad_version` variable.

```yaml
nomad_version: latest
```

The vault version can either be `latest` or `X.Y.Z`.

For production deployment, it is recommended to use the `X.Y.Z` syntax.

### General settings

First, you can change some general settings for nomad, like the dc and region options.

```yaml
nomad_datacenter: dc1
nomad_region: global
```

### ACLs settings

By default, ACLs are enabled on nomad, and automatically bootstrapped.
You can change this by editing the `nomad_acl_configuration` variable:

```yaml
nomad_acl_configuration:
  enabled: true
  token_ttl: 30s
  policy_ttl: 60s
  role_ttl: 60s
```

### Consul integration settings

By default, if consul if also enabled, nomad will use it to register itself as a consul service and also use consul to automatically join the cluster.

```yaml
nomad_enable_consul_integration: "{{ enable_consul | bool }}"
nomad_consul_integration_configuration:
  address: "127.0.0.1:{{ hashicorp_consul_configuration.ports.https if consul_enable_tls else hashicorp_consul_configuration.ports.http }}"
  auto_advertise: true
  ssl: "{{ consul_enable_tls | bool }}"
  token: "{{ _credentials.consul.tokens.nomad.server.secret_id if nomad_enable_server else _credentials.consul.tokens.nomad.client.secret_id}}"
  tags: []
```

Optionally, you can add tags to you nomad services, or disable the consul integration if you don't plan on using it.

### Vault integration settings

Vault integration for nomad is by default disabled, as it requires some vault configuration that is out of the scope of this collection.

You can, once you have deployed and configured vault (or if you are using an external vault not managed by the collection), enable the integration

```yaml
nomad_enable_vault_integration: false
nomad_vault_integration_configuration: {}
```

For configuration options, please refer to the [Official Documentation](https://developer.hashicorp.com/nomad/docs/configuration/vault)

### Drivers settings

### Internal TLS
