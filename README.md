# python-model-builder
Sample project for training a python model

## How to start

Use following command to clone the git repo, build an image and run the container: 
```bash
git clone git@github.com:Luke31/python-model-builder.git &&
cd python-model-builder &&
docker build -t python-model-builder . &&
docker run -it python-model-builder
```