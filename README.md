# SMS Spam Detection System Using NLP

## Overview
This project, **SMS Spam Detection System Using NLP**, was developed as part of the AICTE Internship on AI, a joint CSR initiative by Microsoft and SAP under the mentorship of Rathod Jay. It aims to detect and classify SMS messages as **Spam** or **Not Spam** using Natural Language Processing (NLP) and machine learning techniques. The system is implemented as an interactive web application using **Streamlit**.

---

## Features
- **Real-time Classification**: Predict whether an SMS message is Spam or Not Spam.
- **Machine Learning Powered**: Trained using the Naive Bayes algorithm.
- **Interactive UI**: Built with Streamlit for user-friendly interaction.
- **High Accuracy**: Achieves 97.84% accuracy on the spam classification dataset.

---

## Directory Structure

```plaintext
jain131102-sms-spam-detection-system-using-nlp/
├── app.py                     # Streamlit app for SMS classification
├── model.pkl                  # Trained Naive Bayes model
├── requirements.txt           # Dependencies
├── sms-spam-detection.ipynb   # Jupyter Notebook for training and evaluation
├── sms-spam.csv               # Dataset used for training
├── vectorizer.pkl             # CountVectorizer object
└── .ipynb_checkpoints/        # Temporary Jupyter Notebook checkpoints
```
---

## Installation and Usage

### Prerequisites
- Python 3.7 or higher
- Internet connection to install dependencies

### Step 1: Clone the Repository
```bash
git clone https://github.com/Jain131102/SMS-Spam-Detection-System-Using-NLP.git
cd jain131102-sms-spam-detection-system-using-nlp
```

## Step 2: Install Dependencies
Install the required Python packages using `pip`:
```bash
pip install -r requirements.txt
```

## Step 3: Run the Application
Start the Streamlit app:
```bash
streamlit run app.py
```

## Step 4: Use the Application
- Access the app in your browser at `http://localhost:8501`.
- Enter an SMS message in the text box and click **Predict** to classify the message.

---

## How It Works

### Data Preprocessing
- SMS text is cleaned by:
  - Removing unnecessary characters.
  - Converting text to lowercase.
- Text is tokenized and vectorized using **CountVectorizer**.

### Feature Extraction
- **CountVectorizer** converts text into a numerical representation (bag-of-words).

### Model Training
- A **Naive Bayes classifier** is trained on the preprocessed dataset for classification.

### Web Application
- Users input an SMS in the Streamlit app, and the trained model predicts whether it is Spam or Not Spam.

---

## Results

### Example Outputs
1. **Input**: "You have won a free ticket to Bahamas! Claim now!"  
   **Output**: SPAM  
2. **Input**: "Hi, are we still meeting at 5 PM?"  
   **Output**: NOT SPAM  

---

## Dataset
The **spam.csv** dataset was used for training. It consists of:
- **Messages**: The SMS text content.
- **Labels**: Spam (1) or Not Spam (0).

---

## Dependencies
The following libraries are required:
- `streamlit`
- `scikit-learn`
- `numpy`
- `pandas`

---

## Future Enhancements
1. **Advanced Models**: Incorporate deep learning techniques like RNNs or transformers.
2. **Multilingual Support**: Expand to detect spam in multiple languages.
3. **Interactive Features**: Add spam trend visualizations and keyword highlights.
4. **Real-world Integration**: Deploy as a mobile or desktop application.

---

## Author
**Sourabh Jain**  
Email: [sourabh.jain131102@gmail.com](mailto:sourabh.jain131102@gmail.com)  
*Guided by Rathod Jay under the AICTE Internship on AI*

---

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
