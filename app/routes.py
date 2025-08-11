from flask import Blueprint, render_template, request
from app.model import predict_sentiment

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        review = request.form['review']
        prediction = predict_sentiment(review)
        return render_template('result.html', review=review, prediction=prediction)
