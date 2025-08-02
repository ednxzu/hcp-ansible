### Global Options

This section defines the overarching settings for the deployment:

```yaml
enable_vault: "yes"
enable_consul: "yes"
enable_nomad: "yes"

nomad_version: "1.8.1"
consul_version: "1.18.1"
vault_version: "1.16.2"
```
These variables let you choose which solutions you want to enable, and their respective versions. You can enable any combination of these.


```yaml
api_interface: "eth0"
api_interface_address: "{% raw %}{{ ansible_facts[api_interface]['ipv4']['address'] }}{% endraw %}"
```
The api interface is the interface on which the servers/agents on each node will bind their listener for incoming requests. This can be adjusted on a per-group or per-host configuration, following the [general documentation](general-informations.md/#sub-configuration-directories)


```yaml
enable_log_to_file: true
```
This variable let you configure logging to file for all services at once. It is by default enabled.

```yaml
enable_tls_internal: false
internal_tls_externally_managed_certs: false
```
These variables let you enable cluster-wide internal TLS for all the services. It is disabled by default, as we do not enforce the generation of TLS certificates.

The `internal_tls_externally_managed_certs`, if set to true, let you manage your TLS certificates as you wish it. The deploy playbook will not attempt to copy certificates from the local path, and it is up to you to correctly place the certificates on the target hosts.
