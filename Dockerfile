FROM openshift/rhel7

COPY smasher.py /opt/app-root/src/smasher.py

MAINTAINER Freddy Montero <fmontero@redhat.com>

USER 1001

CMD ["python", "/opt/app-root/src/smasher.py"]
