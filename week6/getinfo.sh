#!/bin/bash

disk_usage=`df -h|grep '/$'|awk '{print $5}'|cut -d% -f1`

if [[ "$disk_usage" > "85" ]];then
    echo -e "Disk-Root: \tneed notice, use: $disk_usage%"
else
    echo -e "Disk-Root: \tis OK, use: $disk_usage%"
fi

total_mem=`free -m|grep '^Mem'|awk '{print $2}'`
#used_mem=`free -m|grep '^Mem'|awk '{print $3}'`
used_mem=`free -m|grep '^-/+'|awk '{print $3}'`
mem_prec=$(printf "%.1f" `expr "scale=3; $used_mem / $total_mem * 100"|bc`)

if [[ "$mem_prec" > "90" ]];then
    echo -e "Memory: \tneed notice, use: $mem_prec%"
else
    echo -e "Memory: \tis OK, use: $mem_prec%"
fi

cpu_count=`grep 'model name' /proc/cpuinfo|uniq -c|awk '{print $1}'`
total_load=`uptime|awk -F"[:,]" '{print $8}'`
aver_load=$(printf "%.2f" `expr "scale=2; $total_load / $cpu_count"|bc`)

if [[ "$aver_load" > "0.7" ]];then
    echo -e "Loadaverage: \tneed notice, use: $aver_load"
else
    echo -e "Loadaverage: \tis OK, use: $aver_load"
fi


