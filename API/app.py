import streamlit as st
import requests

st.set_page_config(page_title="PASS/FAIL Predictor")
st.title("Student PASS/FAIL Predictor")
st.write("Enter the marks for 3 subjects to predict whether the student will pass or fail")

# Input marks
mark1 = st.number_input("Subject 1 marks", min_value=0, max_value=100, value=50)
mark2 = st.number_input("Subject 2 marks", min_value=0, max_value=100, value=50)
mark3 = st.number_input("Subject 3 marks", min_value=0, max_value=100, value=50)

features = [mark1, mark2, mark3]

if st.button("Predict Result"):
    try:
        st.info("Sending request to backend...")  # Status message
        response = requests.post(
            "https://fastapi-mi-render-model.onrender.com/predict",
            json={"features": features},
            timeout=10  # prevent Streamlit from hanging
        )

        st.write(f"Status Code: {response.status_code}")  # helpful for debugging

        if response.status_code == 200:
            result = response.json().get("prediction")
            if result == 1:
                st.success("✅ The student is predicted to pass")
            elif result == 0:
                st.error("❌ The student is predicted to fail")
            else:
                st.warning(f"⚠️ Unexpected prediction value: {result}")
        else:
            st.error(f"🔥 Server error: {response.status_code}")
            st.text(response.text)

    except requests.exceptions.RequestException as e:
        st.error(f"❗ Request failed: {e}")
