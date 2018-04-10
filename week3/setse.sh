#!/bin/bash

setenforce 1
sed -i 's/^SELINUX=.*/SELINUX=enforcing/g' /etc/selinux/config

yum install setroubleshoot-server -y
service auditd restart

mkdir -p /home/shiyanlou/website
chown -R --reference='/var/www/html' /home/shiyanlou/website
chcon -R --reference='/var/www/html' /home/shiyanlou/website

touch /home/shiyanlou/config
chcon -t httpd_sys_content_t /home/shiyanlou/config
