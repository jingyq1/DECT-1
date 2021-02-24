#!/usr/bin/env bash

my_dir="$(dirname "$0")"
. $my_dir/set_env.sh

echo "MMAR_ROOT set to $MMAR_ROOT"

# Data list containing all data
CONFIG_FILE=config/config_validation_trt.json
ENVIRONMENT_FILE=config/environment.json

python3 -u  -m nvmidl.apps.evaluate \
    -m $MMAR_ROOT \
    -c $CONFIG_FILE \
    -e $ENVIRONMENT_FILE \
    --set \
    DATASET_JSON=$MMAR_ROOT/dataset_root/datalist.json \
    output_infer_result=true \
    do_validation=false