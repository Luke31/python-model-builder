# python-model-builder
Sample project for training a python ML-model and persisting it inside the container as `/app/model/model.joblib` 

## How to use

Use following command to clone the git repo, build an image and run the container: 
```bash
git clone git@github.com:Luke31/python-model-builder.git &&
cd python-model-builder &&
docker build -t python-model-builder . &&
docker run -it python-model-builder
```
The resulting model is now persisted inside the image as `/app/model/model.joblib`

Use this resulting image for building a prediction-image like:
```dockerfile
COPY --from python-model-builder /app/model/model.joblib /app/model/model.joblib 
```

Inside your new prediction image you can load the model in python using
```python
from joblib import load
model = load('/app/model/model.joblib')    
```
