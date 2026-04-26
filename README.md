# Signature recognition

#### Language and Libraries

<p>
<a><img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen" alt="python"/></a>
<a><img src="https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white" alt="pandas"/></a>
<a><img src="https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white" alt="numpy"/></a>
<a><img src="https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white" alt="opencv"/></a>
<a><img src="https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white" alt="pytorch"/></a>
<a><img src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)" alt="docker"/></a>
<a><img src="https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white" alt="gcp"/></a>
</p>

## Problem statement

The task of signature recognition involves building a system that can automatically recognize an individual's signature from a given set of signature images. 
The system should be able to distinguish between genuine signatures and forged ones, and should work robustly even in the presence of noise and variations in the signature style.

## Solution Proposed

The goal of signature recognition is to develop an accurate and reliable system that can automatically recognize an individual's signature and distinguish it from forged signatures. 
This can have practical applications in areas such as document verification, fraud detection, and biometric identification.

## Dataset Used

CEDAR Signature is a database of off-line signatures for signature verification. 
Each of 55 individuals contributed 24 signatures thereby creating 1,320 genuine signatures. Some were asked to forge three other writers’ signatures, eight times per subject, thus creating 1,320 forgeries. 
Each signature was scanned at 300 dpi gray-scale and binarized using a gray-scale histogram. Salt pepper noise removal and slant normalization were two steps involved in image preprocessing. The database has 24 genuines and 24 forgeries available for each writer.
## Model Used

ResNet-34 is a popular deep convolutional neural network architecture that was introduced in the paper "Deep Residual Learning for Image Recognition" by Kaiming He et al. in 2016.

ResNet-34 consists of 34 layers, including 33 convolutional layers and 1 fully connected layer. 
The architecture of ResNet-34 is based on the residual learning framework, which allows the network to be deeper while maintaining good performance.

## How to run?

### Step 1: Clone the repository
```bash
git clone my repository 
```

### Step 2- Create a conda environment after opening the repository

```bash
conda create -p env python=3.8 -y
```

```bash
conda activate env
```

### Step 3 - Install the requirements
```bash
pip install -r requirements.txt
```

### Step 4 - Install Google Cloud Sdk and configure

#### For Windows
```bash
https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe
```
#### For Ubuntu
```bash
sudo apt-get install apt-transport-https ca-certificates gnupg
```
```bash
echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
```
```bash
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -
```
```bash
sudo apt-get update && sudo apt-get install google-cloud-cli
```
```bash
gcloud init
```
Before running server application make sure your `Google Cloud Storage` bucket is available

### Step 5 - Run the application server
```bash
python app.py
```

## Run locally

1. Check if the Dockerfile is available in the project directory

2. Build the Docker image

```
docker build -t sign . 
```

3. Run the Docker image

```
docker run -d -p 8080:8080 <IMAGEID>
```

4. Open docker image in interactive model

```
docker exec -ti <IMAGEID> bash
```

5. Authenticate GCloud

```
gcloud auth login
```

6. Authenticate default application

```
gcloud auth application-default login
```

👨‍💻 Tech Stack Used
1. Python
2. Pytorch
3. Docker

🌐 Infrastructure Required.
1. Google Cloud Storage
2. Google Compute Engine
3. Google Artifact Registry
4. Circle CI


## `src` is the main package folder which contains 

**Artifact** : Stores all artifacts created from running the application

**Components** : Contains all components of this project
- DataIngestion
- DataTransformation
- ModelTrainer
- ModelEvaluation
- ModelPusher

**Custom Logger and Exceptions** are used in the project for better debugging purposes.

=====================================================================