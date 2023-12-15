manage_apt_packages
=========
> This repository is only a mirror. Development and testing is done on a private gitea server.

This role enables you to manage packages on **debian-based** distributions. It can be used on its own , or be called by other roles the install/remove packages on demand.

Requirements
------------

None.

Role Variables
--------------
Available variables are listed below, along with default values. A sample file for the default values is available in `default/manage_apt_packages.yml.sample` in case you need it for any `group_vars` or `host_vars` configuration.

```yaml
manage_apt_packages_list: # by default, not defined
  - name: nginx
    version: latest # Leaving empty or setting '' will be considered as latest
    state: absent
  - name: ...
```
This variable is a list of packages, with their name, desired version and state. Note that the role allows version rollbacks, so unless you absolutely need a specific version, it is usualy advised to keep the version on `latest` or empty (which is considered the same).

Dependencies
------------

None.

Example Playbook
----------------

```yaml
# calling the role inside a playbook with either the default or group_vars/host_vars
- hosts: servers
  roles:
    - ednxzu.manage_apt_packages
```

```yaml
# calling the role inside a playbook and injecting variables (in another role for example)
- hosts: servers
  tasks:
    - name: "Install consul package"
      ansible.builtin.include_role:
        name: ednxzu.manage_apt_packages
      vars:
        manage_apt_packages_list:
          - name: consul
            version: 1.13.1-1
            state: present
```

License
-------

MIT / BSD

Author Information
------------------

This role was created by Bertrand Lanson in 2023.
