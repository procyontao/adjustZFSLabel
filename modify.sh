dd if=mpatha_label01 of=/dev/multipath/mpatha conv=notrunc 
dd if=mpathaa_label01 of=/dev/multipath/mpathaa conv=notrunc 
dd if=mpathab_label01 of=/dev/multipath/mpathab conv=notrunc 
dd if=mpathac_label01 of=/dev/multipath/mpathac conv=notrunc 
dd if=mpathad_label01 of=/dev/multipath/mpathad conv=notrunc 
dd if=mpathae_label01 of=/dev/multipath/mpathae conv=notrunc 

dd if=mpatha_label23 of=/dev/multipath/mpatha conv=notrunc count=1024 bs=512 seek=26843544064 
dd if=mpathaa_label23 of=/dev/multipath/mpathaa conv=notrunc count=1024 bs=512 seek=26843544064 
dd if=mpathab_label23 of=/dev/multipath/mpathab conv=notrunc count=1024 bs=512 seek=26843544064 
dd if=mpathac_label23 of=/dev/multipath/mpathac conv=notrunc count=1024 bs=512 seek=26843544064 
dd if=mpathad_label23 of=/dev/multipath/mpathad conv=notrunc count=1024 bs=512 seek=26843544064 

