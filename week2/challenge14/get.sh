#!/bin/bash

port=$1

port_check=`lsof -i:$port|awk 'NR>1 {print $1}'`
if [[ -z "$port_check" ]] ;then
    echo OFF
    exit 0
else
    result=`lsof -i:$port|awk 'NR>1 {print $1}'|uniq|xargs which`
    echo $result
fi
