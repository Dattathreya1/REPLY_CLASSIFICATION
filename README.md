# 📧 Reply Classification API
A machine-learning service that classifies short business replies as **Positive**, **Negative**, or **Neutral**.

This project was built as part of the **SvaraAI – AI/ML Engineer Internship Assignment** and demonstrates the full pipeline:
* **Data exploration & model training** (Google Colab notebook)
* **Model serving with FastAPI** (`app.py`)
* **Environment management** (`requirements.txt`)
* Optional **Transformer fine-tuning** for greater robustness

---

## 📁 Repository Structure
reply-classifier/
│
├─ README.md # Project documentation (this file)
├─ app.py # FastAPI application to serve the model
├─ requirements.txt # Python dependencies
├─ baseline_tfidf_logreg.pkl # Pre-trained baseline model (scikit-learn)
├─ Reply_Classifier_Colab.ipynb # Colab notebook: EDA, training, evaluation
└─ (optional) distilbert_run/ # Saved transformer model if fine-tuned

markdown
Copy code

---

## 🛠️ How `app.py` and `requirements.txt` Were Created

**`app.py`**  
I designed and wrote this file myself after training the model.  
It:
1. Loads the saved scikit-learn pipeline (`baseline_tfidf_logreg.pkl`) with `joblib`.
2. Defines a Pydantic schema to accept JSON input (`{"text": "sample reply"}`).
3. Exposes two endpoints:
   * `GET /` – health check
   * `POST /predict` – returns predicted label and confidence.
4. Uses FastAPI so we automatically get a browser-based Swagger UI for easy testing.

**`requirements.txt`**  
While developing `app.py` I listed the exact packages imported by the notebook and API:
fastapi
uvicorn
joblib
scikit-learn

javascript
Copy code
This guarantees anyone can recreate the same environment with a single command:
```bash
pip install -r requirements.txt
🚀 Quick Start – Run Locally
1️⃣ Clone the Repository
bash
Copy code
git clone https://github.com/<your-username>/reply-classifier.git
cd reply-classifier
2️⃣ (Optional but Recommended) Create a Virtual Environment
bash
Copy code
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Start the FastAPI Server
bash
Copy code
uvicorn app:app --reload --port 8000
The API is now live at http://127.0.0.1:8000

🧪 Test the API
Interactive Swagger UI
Visit http://127.0.0.1:8000/docs, click POST /predict, then Try it out and enter:

json
Copy code
{
  "text": "Looks good—schedule a demo"
}
Click Execute to receive a JSON prediction.

Command Line (curl)

bash
Copy code
curl -X POST "http://127.0.0.1:8000/predict" \
     -H "Content-Type: application/json" \
     -d '{"text":"Looks good—schedule a demo"}'
Example response:

json
Copy code
{"label":"positive","confidence":0.97}
🔄 Re-Train or Reproduce the Model
Open Reply_Classifier_Colab.ipynb in Google Colab.

Upload the provided dataset reply_classification_dataset.csv.

Runtime ▸ Run all to execute every cell:

Cleans and explores the dataset.

Trains a TF-IDF + Logistic Regression classifier.

Evaluates accuracy and macro-F1.

Saves the model to baseline_tfidf_logreg.pkl.

Optional: DistilBERT Fine-Tuning
Switch Colab runtime to GPU (Runtime ▸ Change runtime type ▸ GPU).

Uncomment trainer.train() in the notebook.

After training, download the generated distilbert_run/ folder and modify app.py to load that model if you want a transformer backend.

🗂 Dataset
File: reply_classification_dataset.csv

Size: ~2,100 short replies.

Classes: positive, negative, neutral (balanced).

🐳 Docker (Optional)
To containerize the service:

Create a Dockerfile (example included in notebook comments):

dockerfile
Copy code
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
Build & run:

bash
Copy code
docker build -t reply-classifier .
docker run -p 8000:80 reply-classifier
💡 Key Points
End-to-end: from data exploration to a deployable REST API.

Explainability: The API returns the predicted label and confidence score.

Maintainability: requirements.txt ensures reproducible environments.

Flexibility: Switch between lightweight scikit-learn or a transformer model.
