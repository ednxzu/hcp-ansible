manage_repositories
=========
> This repository is only a mirror. Development and testing is done on a private gitea server.

This role enables you to manage repositories on **debian-based** distributions. It can be used on its own , or be called by other roles the configure repositories on demand.

Requirements
------------

None.

Role Variables
--------------
Available variables are listed below, along with default values. A sample file for the default values is available in `default/manage_repositories.yml.sample` in case you need it for any `group_vars` or `host_vars` configuration.

```yaml
manage_repositories_enable_default_repo: true # by default, set to true
```
This variable enable or disable the configuration of the main distribution repositories (useful when calling this role to configure repo for another role like installing docker).

```yaml
manage_repositories_enable_custom_repo: false # by default, set to false
```
This variable enable of disable the configuration of custom repositories

```yaml
manage_repositories_main_repo_uri: # by default, this variable has the following values
  ubuntu: "http://fr.archive.ubuntu.com/ubuntu"
  debian: "http://deb.debian.org/debian"
```
This variable sets the mirror URLs for the main repositories. You can optionally remove the distribution you don't want (ex. `remove manage_repositories_main_repo_uri[debian]` if you're only using ubuntu).

```yaml
manage_repositories_custom_repo: # by default, this variable is not defined
  - name: docker
    uri: "https://download.docker.com/linux/{{ ansible_distribution|lower }}"
    comments: "{{ ansible_distribution|lower }} docker repository"
    types:
      - deb
    suites:
      - "{{ ansible_distribution_release }}"
    components:
      - stable
    options:
      Signed-By: "https://download.docker.com/linux/{{ ansible_distribution|lower }}/gpg"
  - name: ...
```
This variable contains a list (1 to N) of custom repositories to install. IT HAS  TO BE SET if `manage_repositories_enable_custom_repo == true`, or else the role might fail. The `options` entries are optional, and you can add pretty much all standard options. The `Signed-By` option expects a URL to download the gpg key. If no options are needed, the `options` key can be removed completely.

Dependencies
------------

None.

Example Playbook
----------------

```yaml
# calling the role inside a playbook with either the default or group_vars/host_vars
- hosts: servers
  roles:
    - ednxzu.manage_repositories
```

```yaml
# calling the role inside a playbook and injecting variables (in another role for example)
- hosts: servers
  tasks:
    - name: "Configure hashicorp repository"
      ansible.builtin.include_role:
        name: ednxzu.manage_repositories
      vars:
        manage_repositories_enable_default_repo: false
        manage_repositories_enable_custom_repo: true
        manage_repositories_custom_repo:
          - name: docker
            uri: "https://download.docker.com/linux/{{ ansible_distribution|lower }}"
            comments: "{{ ansible_distribution|lower }} docker repository"
            types:
              - deb
            suites:
              - "{{ ansible_distribution_release }}"
            components:
              - stable
            options:
              Signed-By: "https://download.docker.com/linux/{{ ansible_distribution|lower }}/gpg"
```

License
-------

MIT / BSD

Author Information
------------------

This role was created by Bertrand Lanson in 2023.
