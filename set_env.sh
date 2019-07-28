export NCCL_P2P_DISABLE=1
export NCCL_IB_DISABLE=1

CUDNN_VERSION=5.1
CUDA_VERSION=8.0
export CUDA_VISIBLE_DEVICES=0
export FLAGS_cudnn_deterministic=0
export FLAGS_fraction_of_gpu_memory_to_use=1

export PATH=/home/work/cuda-${CUDA_VERSION}/bin:$PATH
export LD_LIBRARY_PATH=/home/work/cudnn_v${CUDNN_VERSION}_cuda8/cuda/lib64:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=/home/work/nccl_2.1.15-1+cuda8.0_x86_64/lib/:/home/work/cuda-${CUDA_VERSION}/lib64:${LD_LIBRARY_PATH}
