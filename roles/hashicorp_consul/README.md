hashicorp_consul
=========
> This repository is only a mirror. Development and testing is done on a private gitea server.

This role install and configure consul on **debian-based** distributions.

Requirements
------------

None.

Role Variables
--------------
Available variables are listed below, along with default values. A sample file for the default values is available in `default/hashicorp_consul.yml.sample` in case you need it for any `group_vars` or `host_vars` configuration.

```yaml
hashi_consul_install: true # by default, set to true
```
This variable defines if the consul package is to be installed or not before configuring. If you install consul using another task, you can set this to `false`.

```yaml
hashi_consul_auto_update: false # by default, set to false
```
This variable allows you to choose to automatically update consul if a newer version is available. Updating consul is usually pretty safe if done on a regular basis, but for better control over the upgrade process, see `hashi_consul_version`.

```yaml
hashi_consul_start_service: true
```
This variable defines if the consul service should be started once it has been configured. This is usefull in case you're using this role to build golden images, in which case you might want to only enable the service, to have it start on the next boot (when the image is launched)

```yaml
hashi_consul_version: latest # by default, set to latest
```
This variable specifies the version of consul to install when `hashi_consul_install` is set to `true`. The version to specify is the version of the package on the hashicorp repository (`1.14.1-1` for example). This can be found by running `apt-cache madison consul` on a machine with the repository installed.

```yaml
hashi_consul_deploy_method: host # by default, set to host
```
This variable defines the method of deployment of consul. The `host` method installs the binary directly on the host, and runs consul as a systemd service. The `docker` method install consul as a docker container.
> Currently, only the `host` method is available, the `docker` method will be added later.

```yaml
hashi_consul_env_variables: # by default, set to {}
  env_var: value
```
This value is a list of key/value that will populate the `consul.env` file. You do not have to capitalize the KEYS, as it will be done automatically.

```yaml
hashi_consul_data_dir: "/opt/consul" # by default, set to /opt/consul
```
This value defines the path where consul data will be stored on the node. Defaults to `/opt/consul`.

```yaml
hashi_consul_extra_files: false # by default, set to false
```
This variable defines whether or not there is extra configuration files to copy to the target. If there are, these extra files are expected to be jinja2 templates located all in the same directory, and will be copied to the specified directory on the target machine.

```yaml
hashi_consul_extra_files_src: /tmp/extra_files # by default, set to /tmp/extra_files
```
This variable defines the source directory (without the trailing /) for the extra files to be copied in case there are some.

```yaml
hashi_consul_extra_files_dst: /etc/consul.d/extra_files # by default, set to /etc/consul.d/extra_files
```
This variable defines the destination directory (without the trailing /) for the extra files to be copied.

```yaml
hashi_consul_envoy_install: false # by default, set to false
```
This variable allows you to install the envoy binary on the consul node, in case you need to deploy connect proxies. This feature is usefull when deploying consul agents that will handle services in the service mesh. It is NOT required on server nodes (since they most likely wont have services running in service mesh).
```yaml
hashi_consul_envoy_version: latest # by default, set to latest
```
This variable defines which version of envoy to install in case `hashi_consul_envoy_install` is set to true. **IMPORTANT:** The `latest` version set by default is not guaranteed to work, please refer to the [documentation](https://developer.hashicorp.com/consul/docs/connect/proxies/envoy#supported-versions) for informations about the support matrix for consul and envoy.

```yaml
hashi_consul_configuration: {} # by default, set to a simple configuration
```
This variable sets all of the configuration parameters for consul. For more information on all of them, please check the [documentation](https://developer.hashicorp.com/consul/docs/agent/config/config-files). This variable is parsed and converted to json format to create the config file, so each key and value should be set according to the documentation. This method of passing configuration allows for compatibility with every configuration parameters that consul has to offer. The defaults are simply here to deploy a simple, single-node consul server without much configuration, and should NOT be used in production. You will want to edit this to deploy production-ready clusters.

Dependencies
------------

`ednxzu.manage_repositories` to configure the hashicorp apt repository.
`ednxzu.manage_apt_packages` to install consul.

Example Playbook
----------------

```yaml
# calling the role inside a playbook with either the default or group_vars/host_vars
- hosts: servers
  roles:
    - ednxzu.hashicorp_consul
```

License
-------

MIT / BSD

Author Information
------------------

This role was created by Bertrand Lanson in 2023.
