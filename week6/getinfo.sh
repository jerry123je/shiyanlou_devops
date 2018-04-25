#!/bin/bash

disk_usage=`df -h|grep '/$'|awk '{print $5}'|cut -d% -f1`

if [[ "$disk_usage -gt 85" ]];then
    echo "need notice, use: $disk_usage%"
else
    echo "is OK, use: $disk_usage%"
fi

total_mem=`free -m|grep '^Mem'|awk '{print $2}'`
used_mem=`free -m|grep '^-/+'|awk '{print $3}'`
mem_prec=`expr "scale=1; $used_mem / $total_mem * 100"|bc`

if [[ "$mem_prec -gt 90" ]];then
    echo "need notice, use: $mem_prec%"
else
    echo "is OK, use: $mem_prec%"
fi

aver_load=`uptime|awk -F"[:,]" '{print $8}'`

if [[ "$aver_load -gt 0.7" ]];then
    echo "need notice, use: $aver_load"
else
    echo "is OK, use: $aver_load"
fi


