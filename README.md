# Reply Classifier

Repository includes:
- `app.py`: FastAPI app exposing `/predict`.
- `Dockerfile`: Container configuration.
- `requirements.txt`: Python dependencies.
- `notebook.ipynb`: Notebook for data prep/training.

## Run locally
```
pip install -r requirements.txt
uvicorn app:app --reload --port 8000
```

## Docker
```
docker build -t reply-classifier .
docker run -p 8000:80 reply-classifier
```
