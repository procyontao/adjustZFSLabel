
for i in `ls /dev/multipath/mpath*`
do
    res1=${i##*/}_label0
    echo $res1
    echo "head -c 262144 $i > $res1"
    head -c 262144 $i > $res1
    res2=${i##*/}_label1
    echo "head -c 524288 $i > tmp"
    head -c 524288 $i > tmp
    echo "tail -c 262144 tmp > $res2" 
    tail -c 262144 tmp > $res2 
    res3=${i##*/}_label2
    dd if=${i} of=./${res3} count=512 bs=512 skip=26843544064
    res4=${i##*/}_label3
    dd if=${i} of=./${res4} count=512 bs=512 skip=26843544576
done
