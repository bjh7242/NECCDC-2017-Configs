# Docker Web Server

### How to build docker image from Dockerfile
* Make sure you're in the same directory as the Dockerfile.
```
1) docker build .
2) docker tag "hash of build" ccdc:www
```

### How to export a docker container into an image.
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

###  What is in DO_DNS?
A series of janky Python/Bash scripts that take in input
from other DevOps tools to update DNS records.
I **really** need to clean up the code.


<br />
### TODO
* Web admin panel for docker administration.
* Get custom webapp from Chaim to put in container.
