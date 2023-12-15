renew_consul_certificates
=========
> This repository is only a mirror. Development and testing is done on a private gitea server.

This role install consul-template and configure a service to automate renewal of TLS certificates for Hashicorp Consul on **debian-based** distributions.

Requirements
------------

This role assume that you already have installed a consul server on the host, and is only here to assist in automating the certificate renewal process.

Role Variables
--------------
Available variables are listed below, along with default values. A sample file for the default values is available in `default/renew_consul_certificates.yml.sample` in case you need it for any `group_vars` or `host_vars` configuration.

```yaml
renew_consul_certificates_config_dir: /etc/consul-template.d/consul # by default, set to /etc/consul-template.d/consul
```
This variable defines where the files for the role are stored (consul-template configuration + templates).

```yaml
renew_consul_certificates_consul_user: consul # by default, set to consul
```
This variable defines the user that'll be running the certificate renewal service. Defaults to `consul`, and should be present on the host prior to playing this role (ideally when installing consul).

```yaml
renew_consul_certificates_consul_group: consul # by default, set to consul
```
This variable defines the group that'll be running the certificate renewal service. Defaults to `consul`, and should be present on the host prior to playing this role (ideally when installing consul).

```yaml
renew_consul_certificates_service_env_variables:
  consul_http_addr: http://127.0.0.1:8500
  # consul_http_token:
```
This variable sets the environment variables for the consul-certs services (notably the address and token to use for the `consul reload` command).

```yaml
renew_consul_certificates_vault_addr: https://vault.example.com # by default, set to https://vault.example.com
```
This variable defines the address the consul-template service will query to get the new certificates. Defaults to localhost, but can be changed if vault isnt reachable on localhost.

```yaml
renew_consul_certificates_vault_token: mysupersecretvaulttokenthatyoushouldchange # by default, set to a dummy string
```
This variable defines the vault token top use to access vault and renew the certificate. Default is a dummy string to pass unit tests.

```yaml
renew_consul_certificates_vault_token_unwrap: false # by default, set to false
```
Defines whether or not the token is wrapped and should be unwrapped (this is an enterprise-only feature of vault at the moment).

```yaml
renew_consul_certificates_vault_token_renew: true # by default, set to true
```
This variable defines whether or not to renew the vault token. It should probably be `true`, and you should have a periodic token to handle this.

```yaml
renew_consul_certificates_ca_dest: /opt/consul/tls/ca.pem # by default, set to /opt/consul/tls/ca.pem
```
This variable defines where to copy the certificate authority upon renewal. Default to `/opt/consul/tls/ca.pem` but should be changed depending on where you store the certificate authority.

```yaml
renew_consul_certificates_cert_dest: /opt/consul/tls/cert.pem # by default, set to /opt/consul/tls/cert.pem
```
This variable defines where to copy the certificates upon renewal. Default to `/opt/consul/tls/cert.pem` but should be changed depending on where you store the certificates.

```yaml
renew_consul_certificates_key_dest: /opt/consul/tls/key.pem # by default, set to /opt/consul/tls/cert.pem
```
This variable defines where to copy the private keys upon renewal. Default to `/opt/consul/tls/key.pem` but should be changed depending on where you store the keys.

```yaml
renew_consul_certificates_info: # by default, set to:
  issuer_path: pki/issue/your-issuer
  common_name: consul01.example.com
  ttl: 90d
  is_server: false
  include_consul_service: false
```
This variable defines the path on vault to retrieve the certificates, as well as the common name and TTL to use for it. It can also include consul aliases in case you have registered consul services in itself (`consul.service.consul`). It also handles whether or not to append the server.yourdc.consul SAN, in case you're enforcing hostname checking.

```yaml
renew_consul_certificates_consul_dc_name: dc1.consul # by default, set to dc1.consul
```
In case you enforce hostname checking, set this variable to your desired dc and consul domain. This is used to forge the SAN that will be checked by consul to only allow specific nodes to be managers.

```yaml
renew_consul_certificates_consul_service_name: consul.service.consul # by default, set to consul.service.consul
```
This variable defines the consul service name in consul. Default is `consul.service.consul`

```yaml
renew_consul_certificates_start_service: false
```
This variable defines whether or not to start the service after creating it. By default, it is only enabled, but not started, in case you're building golden images (in which case you probably don't want a certificate generated during the build process).

Dependencies
------------

`ednxzu.manage_repositories` to configure hashicorp apt repository.
`ednxzu.manage_apt_packages` to install consul-template.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:
```yaml
# calling the role inside a playbook with either the default or group_vars/host_vars
- hosts: servers
  roles:
    - ednxzu.renew_consul_certificates
```

License
-------

MIT / BSD

Author Information
------------------

This role was created by Bertrand Lanson in 2023.
