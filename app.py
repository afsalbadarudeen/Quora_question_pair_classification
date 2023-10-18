import streamlit as st
import helper
import pickle

# Add a background image
page_bg_img = '''
<style>
.stApp {
background-image: url("https://wallpapercave.com/wp/wp6957320.jpg");
background-size: cover;
color: white;
}
h1, .element-container .markdown-text-container p, label, .stTextInput label span, .stTextInput input, .element-container .stMarkdown h1 {
color: white !important;
}

.stTextInput > div > div > input {
color: black !important;
background-color: white !important;
}

button {
color: blue !important;
}

</style>
'''


st.markdown(page_bg_img, unsafe_allow_html=True)

model = pickle.load(open('model1.pkl', 'rb'))
st.markdown("<h1 style='text-align: center; color: white;'>Duplicate question pairs</h1>", unsafe_allow_html=True)


q1 = st.text_input("Input your question 1")
q2 = st.text_input("Input your question 2")

if st.button("Find"):
    query = helper.query_point_creator(q1,q2)
    result = model.predict(query)[0]

    if result:
        st.header("Duplicate Questions")
    else:
        st.header("Non Duplicate Questions")


    # Add a note
    st.markdown('''
    **Please Note**: This prediction is provided for experimental and educational purposes. While we strive for accuracy, it may not always be 100% precise. Use this tool as a helpful reference, but always exercise your own judgment. If you have any questions or feedback, feel free to get in touch. Thank you for using our service!
    ''')

# Add some space before contact info
for _ in range(4):
    st.write("\n")
# Add contact info
st.markdown('''
**Contact Info**: afzalbadarudeen.07@gmail.com
''', unsafe_allow_html=True)