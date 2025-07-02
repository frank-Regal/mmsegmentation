ARG PYTORCH="1.11.0"
ARG CUDA="11.3"
ARG CUDNN="8"
ARG MMCV="2.0.1"

FROM pytorch/pytorch:${PYTORCH}-cuda${CUDA}-cudnn${CUDNN}-devel

SHELL ["/bin/bash", "-c"]

ENV TORCH_CUDA_ARCH_LIST="6.0 6.1 7.0+PTX"
ENV TORCH_NVCC_FLAGS="-Xfatbin -compress-all"
ENV CMAKE_PREFIX_PATH="$(dirname $(which conda))/../"

# To fix GPG key error when running apt-get update
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/3bf863cc.pub
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/7fa2af80.pub

RUN apt-get update && apt-get install -y git ninja-build libglib2.0-0 libsm6 libxrender-dev libxext6 libgl1-mesa-dev  \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN conda clean --all

# Install MMCV
ARG PYTORCH
ARG CUDA
ARG MMCV
RUN ["/bin/bash", "-c", "pip install openmim"]
RUN ["/bin/bash", "-c", "mim install mmengine"]
RUN ["/bin/bash", "-c", "mim install mmcv==${MMCV}"]

# Install MMSegmentation
RUN git clone -b main https://github.com/frank-Regal/mmsegmentation.git /mmsegmentation
WORKDIR /mmsegmentation
ENV FORCE_CUDA="1"
RUN pip install -r requirements.txt
RUN pip install --no-cache-dir -e .

# Install other dependencies
RUN DEBIAN_FRONTEND=noninteractive apt update && apt upgrade -y \
    && apt install -y software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt update \
    && apt install -y \
    apt-utils \
    curl \
    sudo \
    nano \
    vim \
    tmux \
    wget \
    x11-apps \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Initialize conda and add to bashrc
RUN conda init bash && \
    echo 'export PYTHONPATH=/root/EgoNRG:$PYTHONPATH' >> ~/.bashrc && \
    echo -e "PS1='\e[1m\e[93m\u\e[97m@\e[93m\h:\e[35m\w\e[0m\e[97m#\e[0m '" >> ~/.bashrc

# Copy entrypoint script
COPY ./thirdparty/mmsegmentation/docker/entrypoint.sh /entrypoint.sh
ENTRYPOINT /entrypoint.sh