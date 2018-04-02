#!/bin/bash

#if [ $# != 1 ]; then
#    echo "wrong input"; exit 1
#fi

function Convert(){
num=$1
unit=('B' 'KB' 'MB' 'GB')
for i in ${unit[*]};do
    if (( $num >= 1024 ));then
        ((num=num/1024))
    else
        echo $num $i
        break
    fi
done
}

