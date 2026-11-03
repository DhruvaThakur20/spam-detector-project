Spam Message Detector using Machine Learning

Project Description

The Spam Message Detector is a Machine Learning project that identifies whether a given text message is Spam or Not Spam.

It uses Natural Language Processing (NLP) and a Machine Learning classification algorithm to analyze messages and predict their category.

Features

- Detects spam and legitimate messages.
- Displays prediction confidence.
- Simple HTML frontend.
- Python Flask backend.
- Machine Learning-based text classification.

Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- HTML
- CSS
- JavaScript
- Machine Learning
- NLP

Project Structure

spam-detector-project/
│
├── app.py
├── train_spam_classifier.py
├── index.html
├── spam_model.pkl
├── vectorizer.pkl
├── confusion_matrix.png
├── requirements.txt
└── README.md

Installation and Setup

Step 1: Install Python

Install Python on your computer.

Step 2: Install Required Libraries

Open Command Prompt in the project folder and run:

pip install -r requirements.txt

Step 3: Run the Application

python app.py

Step 4: Open the Frontend

Open "index.html" in your web browser while the Flask backend is running.

Machine Learning Algorithm

The project uses the Multinomial Naive Bayes algorithm for spam classification.

TF-IDF (Term Frequency-Inverse Document Frequency) is used for text feature extraction.

Dataset

The project uses a spam message dataset containing spam and legitimate messages.

Output

The application predicts whether the entered message is:

- Spam
- Not Spam

It also displays the prediction confidence.

Author

Dhruva Thakur

License

This project is created for educational purposes.
