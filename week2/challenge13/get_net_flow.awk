#!/bin/awk -f
 
function Convert(stream){
    n=stream
    #unit=('B' 'KB' 'MB' 'GB')
    split("B,KB,MB,GB",unit,",")
    for(i in unit){
        if ( n >= 1024 ){
            n=n/1024
        }
        else{
            result = (n""unit[i])
            return result
        }
    }
}
NR > 2 {
    num[$1] = $10
}

END{
    for (i in num){
        printf("%s\t%s\n",i,Convert(num[i]))
               }
}
        
