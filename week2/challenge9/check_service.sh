#!/bin/bash

[[ $# == 1 ]] || echo "Wrong input" || exit 1

resutle=`sudo service $1 status >/dev/null 2>&1`
[[ $? == 0 ]] && echo "is Running" && exit 0

if [ -z `ls /etc/init.d/|grep "$1"` ];
then 
    echo -e "Error: \e[33;1m Service \e[31;1m Not \e[0m Found"
    exit 1
else
    echo "Restarting"
    sudo service $1 stop >/dev/null 2>&1
    sudo service $1 start >/dev/null 2>&1
    [[ $? != 0 ]] && echo "restart failed, Please try manually!" && exit 1
fi


