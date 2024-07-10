# Deploying HAProxy frontends

This documentation explains each steps necessary to successfully deploy HAProxy frontends for your deployment, using the ednz_cloud.hashistack ansible collection.

## Prerequisites

You should, before attempting any deployment, have read through the [Quick Start Guide](./quick_start.md). These steps are necessary in order to ensure smooth operations going forward.

## Variables

### Basics

First, in order to deploy the HAproxy frontends, you need to enable the deployment.

```yaml
enable_haproxy: "yes"
```

You can also configure the version of haproxy you would like to use. This has very little impact, and should most likely be left untouched to whatever the collection version is defaulting to (which is the version that it is tested against).

```yaml
haproxy_version: "2.8"
```
This version can either be `latest`, or any `X`, `X.Y`, `X.Y.Z` tag of the [haproxytech/haproxy-debian](https://hub.docker.com/r/haproxytech/haproxy-debian) docker image.

For production deployment, it is recommended to use the `X.Y.Z` syntax.

The `deployment_method` variable will define how to install vault on the nodes.

By default, it runs haproxy inside a docker container, but this can be changed to `host` to install haproxy from the package manager.

Note that not all versions of haproxy are available as a package on all supported distributions. Please refer to the documentation of [ednz_cloud.deploy_haproxy](https://github.com/ednz-cloud/deploy_haproxy) for details about supported versions when installing from the package manager.

```yaml
deployment_method: "docker"
```

### General settings

There aren't many settings that you can configure to deploy the HAProxy frontends. First you'll need to configure a Virtual IP, and pass it in the `globals.yml` configuration file.

```yaml
hashistack_external_vip_interface: "eth0"
hashistack_external_vip_addr: "192.168.121.100"
```

This is used to configure keepalived to automatically configure this VIP on one of the frontend, and handle failover.

You also need to configure the names that will resolve to your different applications (consul, nomad, vault). These names should resolve to your Virtual IP, and will be used to handle host-based routing on haproxy.

```yaml
consul_fqdn: consul.ednz.lab
vault_fqdn: vault.ednz.lab
nomad_fqdn: nomad.ednz.lab
```

With this configuration, querying `http://consul.ednz.lab` will give you the consul UI and API, through haproxy.

> Note: subpaths are not yet supported, so you cannot set the fqdn to `generic.domain.tld/consul`. This feature will be added in a future release.

### Enabling external TLS

To enable external TLS for your APIs and UIs, you will need to set the following variable.

```yaml
enable_tls_external: true
```

This will enable the https listener for haproxy and configure the http listener to be a https redirect only.

## Managing external TLS certificates

### Generating certificates with hashistack-ansible

If you don't care about having trusted certificates (e.g. for developement or testing purposes), you can generate some self-signed certificates for your applications using the `generate_certs.yml` playbook.

```bash
ansible-playbook -i multinode.ini ednz_cloud.hashistack.generate_certs.yml
```

This will generate self-signed certificates for each applications that has been enabled in your `globals.yml`, and for then respective fqdn (also configured in `globals.yml`).

These certificates are going to be placed in `etc/hashistack/certificates/external/`, and will be named after each fqdn. These files should be encrypted using something like ansible-vault, as they are sensitive.

### Managing your own TLS certificates

Similarly, you can manage your own TLS certificates, signed by your own CA. Your certificates should be placed in the `etc/hashistack/certificates/external/` directory, similar to the self-signed ones, and be named like:

`<your_fqdn>.pem` and `<your_fqdn>.pem.key`, for each application.

At the moment, setting all certificates in a single file is not supported, but will be added in a later release.

These certificates will be copied over to the `haproxy_servers` hosts, in `/var/lib/haproxy/certs/`.


### Managing certificates externally

In case you already have systems in place to deploy and renew your certificates, you can simply enable the options in `globals.yml` to not manage certificates directly in hashistack-ansible.

```yaml
external_tls_externally_managed_certs: true
```

Enabling this option will prevents the playbooks from trying to copy certificates over, but the HAProxy nodes will still expect them to be present. It is up to you to copy them over.
