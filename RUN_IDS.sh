#!/bin/bash
for i in {1..2000}
do
sudo ovs-ofctl dump-flows s1 > jax1
grep "nw_src" jax1 > jax2.csv
awk -F "," '{split($4,a,"="); print a[2]","}' jax2.csv > jaxpackets.csv
awk -F "," '{split($5,d,"="); print d[2]","}' jax2.csv > jaxbytes.csv
awk -F "," '{split($14,b,"="); print b[2]","}' jax2.csv > jaxipsrc.csv
awk -F "," '{split($15,c,"="); print c[2]","}' jax2.csv > jaxipdst.csv
python IDS.py
sudo ovs-ofctl del-flows s1
echo "Analyzing Traffic:"

python network_monitoring.py
r=$(awk '{print $0;}' Result.txt)
if [ $r -eq 1 ]; then
echo " $(tput setaf 1) Network is under attack!!$(tput sgr 0)"
elif [ $r -eq 0 ]; then
echo "Normal Traffic Detected"

fi
sleep 3
done
