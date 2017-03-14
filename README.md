# Docker Web Server

### How to export a Docker container into an image.
```
docker export 6c2209c66168 -o Docker_www_ccdc.tar.gz                                    
```

### How to import pre-build Docker image.
```
docker import Docker_www_ccdc.tar.gz
```

### How to mount directory into container.
```
docker run -v /absolute/path/:/internal/docker/directory/ container:tag /executable/
```

### How to build Docker container.

```
docker build -t ccdc\www .
```

<br />

## Testing Playbooks
### Vagrant Playbook testing
* Change VagrantFile to be provisioned via Ansible.

```
config.vm.provision "ansible" do |ansible|
    ansible.verbose = "v"
    ansible.playbook = "YOUR_PLAYBOOK_HERE.yml"
end
```

### TODO
* Get custom webapp from Chaim to put in container.
