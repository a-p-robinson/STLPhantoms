#!/bin/bash
# Install the dependent packages for Scientific Linux 7.2 (shoudl also work on RHEL / CENTOS)
sudo yum install -y python-matplotlib numpy scipy vtk-python python-pip
sudo pip install --upgrade pip
sudo pip install --trusted-host www.simpleitk.org -f http://www.simpleitk.org/SimpleITK/resources/software.html SimpleITK
sudo pip install pydicom
