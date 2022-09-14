import streamlit as st
# from PIL import  Image

# Custom imports 
from multipage import MultiPage
from Pages import data_upload, explore_data, classification_models, regression_models # import your pages here

# Create an instance of the app 
app = MultiPage()

# Title of the main page
# display = Image.open('Logo.png')
# display = np.array(display)
# st.image(display, width = 400)
# st.title("Data Storyteller Application")
# col1, col2 = st.beta_columns(2)
# col1.image(display, width = 400)
# col2.title("Machine Learning Trial Room App")

#st.image("https://pngfile.net/download/OwfxHu60MBfhycChCLA8PuMnK2xdI3P2jcLRNO5pRD4IpiIu5nqQXEf1IfsI2ErdKFcHM6bfqVy08Mklt7Np2Y7CX1sWhckEP7bQCpHILfI8VJMQ18QDT5UAcHRgoJ0FUHAiZFpH4mocU0QEqFyJzwlp4rIRNmBUIQb699lgnmFEBPvaf6oUCo2vGv1dvNTKkEoBGxPX/large", width= 150)
st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Dentsu-logo_black.svg/2560px-Dentsu-logo_black.svg.png', width=250)
st.title("ML Data Trial Laboratory")


# Add all your application here
app.add_page("Upload Data", data_upload.app)
app.add_page("Explore Data", explore_data.app)
app.add_page("Classification Models", classification_models.app)
app.add_page("Regression Models", regression_models.app)


# The main app
app.run()

# Footer of the app
footer = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            footer:after {
                visibility: visible;
                display: block;
                position: relative;
                padding: 5px;
                top: 2px;
            }
            </style>
            """
st.markdown(footer, unsafe_allow_html=True)
