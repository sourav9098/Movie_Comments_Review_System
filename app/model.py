import pickle
import os

# Load saved model and vectorizer
model_path = os.path.join(os.getcwd(), "model.pkl")
vectorizer_path = os.path.join(os.getcwd(), "vectorizer.pkl")

model = pickle.load(open(model_path, "rb"))
vectorizer = pickle.load(open(vectorizer_path, "rb"))

def predict_sentiment(review):
    data = vectorizer.transform([review]).toarray()
    prediction = model.predict(data)[0]
    return "Positive 😊" if prediction == 1 else "Negative 😞"
