#!/usr/bin/env bash


my_dir="$(dirname "$0")"
. $my_dir/set_env.sh

echo "MMAR_ROOT set to ${MMAR_ROOT}"
additional_options="$*"

# Data list containing all data
CONFIG_FILE="config/config_train.json"
ENVIRONMENT_FILE="config/environment.json"

# Pre-trained checkpoint
MMAR_CKPT="models/model.ckpt"

DATA_ROOT="/claraDevDay/classify_model/dataset_root"
DATASET_JSON="/claraDevDay/classify_model/dataset_root/datalist2.json"
OUTPUT_DIR="${MMAR_ROOT}/models"

mkdir -p ${OUTPUT_DIR}
python3 -u  -m nvmidl.apps.train \
    -m ${MMAR_ROOT} \
    -c ${CONFIG_FILE} \
    -e ${ENVIRONMENT_FILE} \
    --set \
    epochs=30 \
    learning_rate=1e-64 \
    DATA_ROOT=${DATA_ROOT} \
    DATASET_JSON=${DATASET_JSON} \
    PRETRAIN_WEIGHTS_FILE="" \
    MMAR_CKPT=${MMAR_CKPT} \
    MMAR_CKPT_DIR=${OUTPUT_DIR} \
    multi_gpu=false \
    ${additional_options} 2>&1 | tee ${OUTPUT_DIR}/log.txt
