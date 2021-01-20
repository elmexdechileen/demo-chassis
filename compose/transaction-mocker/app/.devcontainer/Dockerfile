ARG VARIANT="3"
FROM continuumio/anaconda3

ENV PIP_TARGET=/usr/local/pip-global
ENV PYTHONPATH=${PIP_TARGET}:${PYTHONPATH}
ENV PATH=${PIP_TARGET}/bin:${PATH}
ENV ORACLE_HOME=/opt/oracle/instantclient_19_8

RUN apt update && apt install -y alien 

RUN wget https://download.oracle.com/otn_software/linux/instantclient/211000/oracle-instantclient-basic-21.1.0.0.0-1.x86_64.rpm && \
 	alien -i oracle-*.rpm && \
 	echo 'export PATH=$PATH:/opt/oracle/instantclient_19_8' >> /etc/profile && \
 	echo 'export LD_LIBRARY_PATH=/opt/oracle/instantclient_19_8' >> /etc/profile && \
 	echo 'export ORACLE_HOME=/opt/oracle/instantclient_19_8' >> /etc/profile && \
 	ln -s /opt/oracle/instantclient_19_8/libclntsh.so /usr/lib/libclntsh.so && \
 	ln -s /opt/oracle/instantclient_19_8/libnnz19.so /usr/lib/libnnz19.so && \
 	ln -s /opt/oracle/instantclient_19_8/libclntsh.so.19.1 /usr/lib/libclntsh.so.19.1 && \
 	ln -s /opt/oracle/instantclient_19_8/libocci.so.19.1 /usr/lib/libocci.so.19.1 && \
 	ln -s /opt/oracle/instantclient_19_8/libclntshcore.so.19.1 /usr/lib/libclntshcore.so.19.1 && \
 	ln -s /opt/oracle/instantclient_19_8/libipc1.so /usr/lib/libipc1.so && \
 	ln -s /opt/oracle/instantclient_19_8/liboramysql19.so /usr/lib/liboramysql19.so
