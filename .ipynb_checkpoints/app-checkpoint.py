import streamlit as st
import pickle

def main():
    # Set Streamlit page configuration
    st.set_page_config(
        page_title="SMS Spam Detection App",
        page_icon=":envelope:",
        layout="wide",
    )

    # Load model and vectorizer
    cv = pickle.load(open("vectorizer.pkl", "rb"))
    model = pickle.load(open("model.pkl", "rb"))

    # Main app UI
    st.title("SMS Spam Detection App")
    st.write("*Made with ❤️ by Sourabh Jain*")

    # Input field for SMS text
    user_input = st.text_area("Enter the SMS to check for spam")

    # Button to trigger prediction
    if st.button("Predict", key="predict_button"):
        if user_input:
            data = [user_input]
            vectorized_data = cv.transform(data).toarray()
            result = model.predict(vectorized_data) 
            if result[0]==0:
                st.warning("THIS IS NOT SPAM SMS")
            else:
                st.warning("THIS IS A SPAM SMS")
        else:
            st.warning("Please enter an SMS")
        
# Run the app when the script is executed
if __name__ == "__main__":
    main()
