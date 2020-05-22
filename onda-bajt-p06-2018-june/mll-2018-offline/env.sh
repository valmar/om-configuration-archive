source /gpfs/cfel/cxi/common/cfelsoft-rh7/setup.sh
module load cfel-python2/latest
echo `which python`
export ONDA_INSTALLATION_DIR=/gpfs/cfel/cxi/scratch/user/cxiuser/Software/onda
export PYTHONPATH=${ONDA_INSTALLATION_DIR}:${PYTHONPATH}
export PATH=${ONDA_INSTALLATION_DIR}:${ONDA_INSTALLATION_DIR}/GUI/:${ONDA_INSTALLATION_DIR}/tools/:${PATH}

