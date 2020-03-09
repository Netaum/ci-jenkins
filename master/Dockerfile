FROM jenkins/jenkins:lts

RUN /usr/local/bin/install-plugins.sh \
    git \
    matrix-auth \
    workflow-aggregator \
    docker-workflow \
    blueocean \
    credentials-binding \
    subversion \
    git-parameter \
    ansicolor \
    groovy-postbuild

ENV JENKINS_USER admin
ENV JENKINS_PASS admin

ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false

COPY executors.groovy /usr/share/jenkins/ref/init.groovy.d/
COPY default-user.groovy /usr/share/jenkins/ref/init.groovy.d/

VOLUME /var/jenkins_home
COPY --chown=jenkins:jenkins ./certificates/CASubIntegrada.cer /usr/local/share/ca-certificates/CASubIntegrada.cer
RUN chmod 644 /usr/local/share/ca-certificates/CASubIntegrada.cer
COPY --chown=jenkins:jenkins ./certificates/svn.minhati.com.br.cer /usr/local/share/ca-certificates/svn.minhati.com.br.cer
RUN  chmod 644 /usr/local/share/ca-certificates/svn.minhati.com.br.cer
USER root
RUN update-ca-certificates

USER jenkins