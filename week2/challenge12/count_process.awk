#!/bin/awk -f

{
    num[$1]++
} 

END{
    for (i in num) 
    {
        printf("%s %d\n",i,num[i])
    }
}
