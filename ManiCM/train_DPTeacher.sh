export HYDRA_FULL_ERROR=1
export CUDA_VISIBLE_DEVICES=5

python train_DPTeacher.py --config-name=dp_teacher.yaml 