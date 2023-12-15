docker_systemd_service
=========
> This repository is only a mirror. Development and testing is done on a private gitea server.

This role lets you configure a docker container and run it as a systemd service on **debian-based** distributions. This role is heavily sourced from [mhutter.docker-systemd-service](https://github.com/mhutter/ansible-docker-systemd-service), but aims at providing some of the missing features of said role.

Requirements
------------

This roles assumes you have docker installed on the target host. You can use [ednxzu.install_docker](https://github.com/ednxzu/install_docker) to do so.

Role Variables
--------------
Available variables are listed below, along with default values. A sample file for the default values is available in `default/docker_systemd_service.yml.sample` in case you need it for any `group_vars` or `host_vars` configuration.

```yaml
docker_systemd_service_container_name: "My-Service" # by default, set to "My-Service"
```
The name that will be assigned to the container.

```yaml
docker_systemd_service_image: # by default, not defined
```
The image (and optionally tag) to use for the service.

```yaml
docker_systemd_service_container_env: {} # by default, set to {}
```
A list of key/value pairs, that will be written to the environment file for the container. the key NEEDS TO BE CAPTIALIZED, it will not be done automatically. Example: `MY_ENV_VAR: foobar`.

```yaml
docker_systemd_service_container_pull_image: true # by default, set to true
```
Whether or not the role should pull the image during its run.

```yaml
docker_systemd_service_container_pull_force_source: true # by default, set to true
```
If `docker_systemd_service_container_pull_image: true`, whether the pull you be executed at every run. See [`docker_image.force_source`](https://docs.ansible.com/ansible/latest/collections/community/docker/docker_image_module.html#parameter-force_source)

```yaml
docker_systemd_service_flags: [] # by default, set to []
```
This variable lets you pass whatever flags you need to the docker run command. It is a list, to which you can add multiple types of flags:
 - ```yaml
    - key: value
    # will pass the flag --key "value" to the container.
    Example:
      - network: host
 - ```yaml
    - simple_key
    # will pass the flag --simple_key to the container.
    Example:
      - privileged
 - ```yaml
    - key:
        - value1
        - value2
    # will pass the flags --key "value1" --key "value2" to the container.
    Example:
      - volume:
          - /path/on/host:/path/on/container
          - /var/run/docker.sock:/var/run/docker.sock:ro

```yaml
docker_systemd_service_name: "{{ docker_systemd_service_container_name }}_container"  # by default, set to "{{ docker_systemd_service_container_name }}_container"
```
The name of the systemd service to register.

```yaml
docker_systemd_service_systemd_options: []  # by default, set to []
```
Extra options to include in systemd service file.

```yaml
docker_systemd_service_enabled: true  # by default, set to true
```
Whether the service should be enabled during the role's run.

```yaml
docker_systemd_service_masked: false  # by default, set to false
```
Whether the service should be marked as masked.

```yaml
docker_systemd_service_state: started  # by default, set to started
```
The state the service should be put in. Valid options are: `reloaded`, `restarted`, `started`, `stopped`, and `absent`. Realistically, you probably want to use `started` or `stopped`. `absent` can be used to remove the service and all associated files from the host.

```yaml
docker_systemd_service_restart: true  # by default, set to true
```
Whether the role should restart the service if changes are made to any of the files (when service is already runing).

Dependencies
------------

None.

Example Playbook
----------------

```yaml
# calling the role inside a playbook with either the default or group_vars/host_vars
- hosts: servers
  roles:
    - ednxzu.docker_systemd_service
```

License
-------

MIT / BSD

Author Information
------------------

This role was created by Bertrand Lanson in 2023.
