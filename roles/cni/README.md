**CNI**
=========

This role configures [Container Networking Interface (CNI)](https://github.com/containernetworking/plugins) plugins on the target host, enabling networking capabilities for containerized applications.

**Requirements**
------------

This role does not have any specific software requirements. However, it assumes that the target host has the necessary dependencies installed to manage containers.

**Role Variables**
--------------

### Plugin Configuration

```yaml
cni_plugins_version: "latest"
```
Specifies the version of the CNI plugins to install. The default is `latest`, which installs the latest stable version. It is recommended to pin the CNI version to prevent unexpected changes. Pinned versions should be in the format `X.Y.Z`, based on the GitHub tags from the [CNI GitHub repository](https://github.com/containernetworking/plugins).

```yaml
cni_plugins_install_path: /opt/cni/bin
```
Defines the directory where the CNI plugins will be installed. This path is where the binaries will reside for container runtime access.

```yaml
cni_plugins_install_consul_cni: false
```
Indicates whether to install the Consul CNI plugin in addition to the standard CNI plugins. If set to `true`, the role will download and install the Consul CNI plugin from the HashiCorp releases repository, matching the version of the other CNI plugins.

### User and Group Configuration

```yaml
cni_user: nomad
```
Specifies the user under which the CNI plugins will be executed. Default is `nomad`, which is commonly used for applications managed by HashiCorp Nomad.

```yaml
cni_group: nomad
```
Defines the group under which the CNI plugins will be executed. Default is `nomad`, ensuring that permissions are correctly set for the user and group running the plugins.

**Note on Permissions:**

The specified user and group are used to set the appropriate permissions for the installed plugins, ensuring that only the designated user has the required access to execute the binaries.

**Dependencies**
------------

None.

**Example Playbook**
----------------

```yaml
# Example playbook for installing CNI plugins
- hosts: servers
  roles:
    - ednz_cloud.hashistack.cni
```

**License**
-------

MIT / BSD

**Author Information**
------------------

This role was created by Bertrand Lanson in 2024.
