install_docker
=========
> This repository is only a mirror. Development and testing is done on a private gitea server.

This role install and configure docker on **debian-based** distributions.

Requirements
------------

None.

Role Variables
--------------
Available variables are listed below, along with default values. A sample file for the default values is available in `default/install_docker.yml.sample` in case you need it for any `group_vars` or `host_vars` configuration.

```yaml
install_docker_edition: ce # by default, set to ce
```
This variable sets the edition of docker to install. It can be either `ce` (community edition) or `ee` (enterprise edition).

```yaml
install_docker_auto_update: false # by default, set to false
```
This variable allows you to choose to automatically update docker if a newer version is available whenever the role is replayed. Updating docker is usually pretty safe if done on a regular basis.

```yaml
install_docker_start_service: true
```
This variable defines whether or not to start the docker service after installing it. This can be turned off in case you're building golden images, so that your golden image does not start the docker service during it's build process.

```yaml
install_docker_compose: false # by default, set to false
```
This variables defines whether or not to install docker-compose on the host.

```yaml
install_docker_compose_version: latest # by default, set to latest
```
This variable defines the version of docker-compose to install. It support either `latest`, or the version number (`vX.Y.Z`). Officially, only versions `>=v2.0.1` are supported, as the naming for most packages changed at this release.

```yaml
install_docker_python_packages: false # by default, set to false
```
This variable defines whether or not to install the python packages for managing docker with ansible. This package is required if you plan to perform docker operations with ansible, and should be installed if that is your goal.

```yaml
install_docker_python_packages_version: latest # by default, set to latest
```
This variable defines the version of the python docker package that should be installed. Refer to [ednxzu/manage_pip_packages](https://github.com/ednxzu/manage_pip_packages) for documentation.

```yaml
install_docker_users: [] #by default, set to []
```
This variable is a list of users to add to the docker group, so that they can perform docker related tasks, without requiring privilege escalation.

```yaml
install_docker_daemon_options: {} # by default, set to {}
```
This variable defines the parameters to append to the daemon.json file (in `/etc/docker/daemon.json`). For more details, check out the [documentation](https://docs.docker.com/config/daemon/).

Dependencies
------------

`ednxzu.manage_pip_packages` to install docker python packages for using the `community.docker` modules.
`ednxzu.manage_repositories` to configure the docker apt repository.
`ednxzu.manage_apt_packages` to install docker.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:
```yaml
# calling the role inside a playbook with either the default or group_vars/host_vars
- hosts: servers
  roles:
    - ednxzu.install_docker
```

License
-------

MIT / BSD

Author Information
------------------

This role was created by Bertrand Lanson in 2023.
