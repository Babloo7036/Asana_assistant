# Asana_assistant
**Asana** is an AI-powered chatbot designed to assist users in identifying potential medications based on their symptoms. Users can describe their health concerns, and Asana intelligently analyzes their symptoms to suggest suitable medicines. It leverages advanced natural language processing (NLP) and medical databases to provide accurate and relevant recommendations, enhancing user convenience and healthcare accessibility.

## Overview
This project is a **Pharma Chatbot** that suggests medicines based on user symptoms. It is built using **Flask** for the backend and **HTML, CSS, and JavaScript** for the frontend. The chatbot leverages **Natural Language Processing (NLP)** and **Machine Learning (ML)** to provide accurate medicine recommendations.

**Live Demo :** Integrated chatbot in website - [https://babloo7036.github.io/pharmay_frontend/]

**Live Demo :** Chatbot Webapplication - [https://asana-assistant.onrender.com]


## Features
- **User-friendly chatbot UI** for entering symptoms.
- **Flask API** to process symptom input and return medicine suggestions.
- **ML Model (TF-IDF + Logistic Regression)** trained on a dataset of symptoms and medicines.
- **Interactive web interface** with real-time chat updates.

## Tech Stack
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Machine Learning**: Scikit-learn (TF-IDF + Logistic Regression)

## Installation & Setup
### 1. Clone the Repository
```sh
 git clone https://github.com/your-repo/pharma-chatbot.git
 cd pharma-chatbot
```

### 2. Install Dependencies
```sh
pip install flask scikit-learn pandas
```

### 3. Run the Flask Server
```sh
python app.py
```
The server will start at `http://127.0.0.1:5000/`

### 4. Open the Chatbot UI
Open `chatbot_template.html` in a web browser.

## API Endpoint
### `POST /predict`
- **Request**: JSON `{ "symptoms": "fever headache" }`
- **Response**: JSON `{ "medicine": "Paracetamol" }`

## Project Structure
```
/pharma-chatbot
│── app.py               # Flask backend
│── chatbot_template.html # Chatbot UI
│── README.md            # Project documentation
└── requirements.txt     # Dependencies
```

## Future Enhancements
- Use **Deep Learning (LSTMs, Transformers)** for better accuracy.
- Integrate a **Database** for storing chat history.
- Improve UI with **React.js** for dynamic interactions.


