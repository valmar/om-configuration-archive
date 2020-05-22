## Add the number of cores and the host IPs in place of question marks in lines 9 and 10
source /reg/g/cfel/onda/onda-20181214/setup-bash.sh
#. setup-bash.sh
echo Running `pwd`/monitor_wrapper.sh
echo '#!/bin/bash' > `pwd`/monitor_wrapper.sh
echo '# Auto-generated file from run_onda_crystallography_slac.sh' >> `pwd`/monitor_wrapper.sh
echo '. /reg/g/cfel/onda/onda-20181214/setup-bash.sh' >> `pwd`/monitor_wrapper.sh
echo "onda_monitor.py 'shmem=psana.0:stop=no'" >> `pwd`/monitor_wrapper.sh
chmod +x `pwd`/monitor_wrapper.sh
`which mpirun` --oversubscribe --map-by ppr:8:node --host daq-cxi-mon07,daq-cxi-mon08 `pwd`/monitor_wrapper.sh




