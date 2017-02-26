FROM ubuntu
MAINTAINER NECCDC
EXPOSE 23 21 80 443 3306 8080
RUN apt-get update -y
RUN apt-get install git vim nginx openssh-server mysql-client net-tools python2.7 -y

# Python Requirements.
RUN apt-get install python-pip -y
RUN pip install --upgrade pip
RUN pip install mysql-connector
RUN pip install numpy

RUN apt-get install git vim nginx openssh-server mysql-client net-tools python-pip -y
RUN pip install flask flask-socketio
RUN mkdir /var/run/sshd
RUN echo 'root:Password*' | chpasswd
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login.
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile
RUN echo "container-www" > /etc/hostname


### Start Nginx
RUN service nginx start

### Add vulnerabilities.

### To mount host dir into container run cmd below:
# docker run -v /Users/<path>:/<container path> 
# docker run -d ccdc\www /usr/sbin/nginx
