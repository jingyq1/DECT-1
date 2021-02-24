#!/usr/bin/env bash
export CUDA_VISIBLE_DEVICES=0,1,2,3

my_dir="$(dirname "$0")"
. $my_dir/set_env.sh

echo "MMAR_ROOT is set to $MMAR_ROOT"

# Data list containing all data
CONFIG_FILE="config/config_train.json"
ENVIRONMENT_FILE="config/environment.json"

# Pre-trained checkpoint
MMAR_CKPT="models/model.ckpt"

DATA_ROOT="/workspace/Data/COVID/COVID_Test_Data"
DATASET_JSON="${MMAR_ROOT}/config/dataset_0.json"
OUTPUT_DIR="${MMAR_ROOT}/model_finetuned"

N_GPUS=2
mkdir -p ${OUTPUT_DIR}
mpirun -np ${N_GPUS} -H localhost:${N_GPUS} -bind-to none -map-by slot \
    -x NCCL_DEBUG=INFO -x LD_LIBRARY_PATH -x PATH -mca pml ob1 -mca btl ^openib --allow-run-as-root \
    python3 -u  -m nvmidl.apps.train \
    -m $MMAR_ROOT \
    -c $CONFIG_FILE \
    -e $ENVIRONMENT_FILE \
    --set \
    DATA_ROOT=${DATA_ROOT} \
    DATASET_JSON=${DATASET_JSON} \
    PRETRAIN_WEIGHTS_FILE="" \
    MMAR_CKPT=${MMAR_CKPT} \
    MMAR_CKPT_DIR=${OUTPUT_DIR} \
    learning_rate=1e-4 \
    num_training_epoch_per_valid=1 \
    epochs=200 \
    multi_gpu=true 2>&1 | tee ${OUTPUT_DIR}/log.txt
