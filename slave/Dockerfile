FROM ubuntu:16.04

RUN apt-get update && apt-get install -y apt-transport-https ca-certificates
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
RUN echo "deb [arch=amd64] https://download.docker.com/linux/ubuntu xenial stable" > /etc/apt/sources.list.d/docker.list
RUN apt-get update && apt-get install -y docker-ce --allow-unauthenticated
 
RUN apt-get update && apt-get install -y openjdk-8-jre curl python python-pip git
RUN easy_install jenkins-webapi
 
RUN curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && chmod +x /usr/local/bin/docker-compose
RUN mkdir -p /home/jenkins
RUN mkdir -p /var/lib/jenkins
 
ADD slave.py /var/lib/jenkins/slave.py
 
WORKDIR /home/jenkins
 
ENV JENKINS_URL "http://jenkins"
ENV JENKINS_SLAVE_ADDRESS ""
ENV JENKINS_USER "admin"
ENV JENKINS_PASS "admin"
ENV SLAVE_NAME ""
ENV SLAVE_SECRET ""
ENV SLAVE_EXECUTORS "1"
ENV SLAVE_LABELS "docker"
ENV SLAVE_WORING_DIR ""
ENV CLEAN_WORKING_DIR "true"

COPY ./certificates/CASubIntegrada.cer /usr/local/share/ca-certificates/CASubIntegrada.cer
RUN chmod 644 /usr/local/share/ca-certificates/CASubIntegrada.cer
COPY ./certificates/svn.minhati.com.br.cer /usr/local/share/ca-certificates/svn.minhati.com.br.cer
RUN  chmod 644 /usr/local/share/ca-certificates/svn.minhati.com.br.cer
RUN update-ca-certificates

CMD [ "python", "-u", "/var/lib/jenkins/slave.py" ]
