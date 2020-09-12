#!/bin/bash
echo "updatting repository"
cd aws_ec2_django
git pull https://github.com/evansMeja/aws_ec2_django.git
sudo supervisorctl restart all