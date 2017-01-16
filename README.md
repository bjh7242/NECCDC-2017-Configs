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

<br />
### TODO
* Web admin panel for docker administration.
* Get custom webapp from Chaim to put in container.
