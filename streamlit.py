# Import Libraries
import streamlit as st
st.set_page_config(layout="wide", initial_sidebar_state="expanded", )
import pandas as pd
import numpy as np
import plotly.express as px
import streamlit.components.v1 as components
import requests

# Dataset
url = "phone_df.csv"

# Prediction Function connected to the FAST API
def get_predictions(CHK_ACCT, DURATION,	HISTORY, SAV_ACCT, EMPLOYMENT, REAL_ESTATE,	PROP_UNKN_NONE,	AGE, OTHER_INSTALL,	OWN_RES):
    url = 'https://loan-credit-scorecard-8730a72d721d.herokuapp.com//predict?CHK_ACCT={CHK_ACCT}&DURATION={DURATION}&HISTORY={HISTORY}&SAV_ACCT={SAV_ACCT}&EMPLOYMENT={EMPLOYMENT}&REAL_ESTATE={REAL_ESTATE}&PROP_UNKN_NONE={PROP_UNKN_NONE}&AGE={AGE}&OTHER_INSTALL={OTHER_INSTALL}&OWN_RES={OWN_RES}' \
        .format(CHK_ACCT=CHK_ACCT, DURATION=DURATION, HISTORY=HISTORY, SAV_ACCT=SAV_ACCT, EMPLOYMENT=EMPLOYMENT, REAL_ESTATE=REAL_ESTATE, PROP_UNKN_NONE=PROP_UNKN_NONE, AGE=AGE, OTHER_INSTALL=OTHER_INSTALL, OWN_RES=OWN_RES)
    response = requests.post(url)
    json_response = response.json()
    score=json_response['prediction']
    return score

# Side Bar
st.sidebar.image('photos/logo.png')
st.sidebar.header("Phone Price Prediction")
menu = ['Get Score','Exploratory Data Analysis','About']
selection = st.sidebar.selectbox("", menu)

st.sidebar.write('Predicting Loan Score Credits for new customers is important to Financial Institutions to predict customers probability to pay the loan and avoid costs that come with bad loan customers.')

# Get Price Functionality
if selection == 'Get Score':
    col1, col2 = st.columns(2)
    with col1:
        st.image('photos/phones.jpg')
        st.title('Enter customer details')
        st.image('photos/specs.png')
        brand = st.selectbox('Select Brand', ['', 'Nokia', 'Samsung', 'Infinix', 'Tecno', 'Redmi', 'Itel', 'Vivo', 'Hisence', 'Oppo', 'Motorola', 'Realme'], index=0)
        screen_size = st.number_input("Enter screen_size (Size of the screen)")
        ram = st.number_input("Enter RAM capacity (RAM defines how fast the phone is)")
        rom = st.number_input("Enter ROM capacity (ROM defines memory storage)")
        mp = st.number_input("Enter Megapixels (Defines the resolution and quality of photos taken)")
        battery = st.number_input("Enter battery capacity (Defines battery life)")

        result = ""

        # when 'Predict' is clicked, make the prediction and store it
        if st.button("Predict"):
            result = int(np.exp(get_predictions(brand=brand, screen_size=screen_size, ram=ram, rom=rom, mp=mp, battery=battery)))
            st.success(f'Price of Phone: {result} UGX')
            st.image('photos/phoness.jpg')

    with col2:
        st.image('photos/phonesss.jpg')
        
# Exploratory Data Analysis Functionality
if selection == 'Exploratory Data Analysis':    
    phone_df = pd.read_csv(url, encoding="ISO-8859-1", low_memory=False)
    st.markdown('Display data')
    st.table(phone_df.head())

    # scatter plot of brand and price
    st.header("Brand and Price")
    fig = px.scatter(phone_df, x='brand', y='price', opacity = 0.25, template = 'plotly_dark', 
                    color='brand', hover_data=['brand', 'price'],title = 'PHONE PRICE PREDICTION (BRAND - PRICE RELATIONSHIP)')
    fig.update_layout(width=900, height=500)
    st.plotly_chart(fig)

    # scatter plot of screen_size and price
    st.header("Screen size and Price")
    fig = px.scatter(phone_df, x='screen_size', y='price', opacity = 0.25, template = 'plotly_dark', 
                    color='screen_size', hover_data=['screen_size', 'price'],title = 'PHONE PRICE PREDICTION (SCREEN SIZE - PRICE RELATIONSHIP)')
    fig.update_layout(width=900, height=500)
    st.plotly_chart(fig)

    # scatter plot of ram and price
    st.header("RAM and Price")
    fig = px.scatter(phone_df, x='ram', y='price', opacity = 0.25, template = 'plotly_dark', 
                    color='ram', hover_data=['ram', 'price'],title = 'PHONE PRICE PREDICTION (RAM - PRICE RELATIONSHIP)')
    fig.update_layout(width=900, height=500)
    st.plotly_chart(fig)

    # scatter plot of rom and price
    st.header("ROM and Price")
    fig = px.scatter(phone_df, x='rom', y='price', opacity = 0.25, template = 'plotly_dark', 
                    color='rom', hover_data=['rom', 'price'],title = 'PHONE PRICE PREDICTION (ROM - PRICE RELATIONSHIP)')
    fig.update_layout(width=900, height=500)
    st.plotly_chart(fig)

    # scatter plot of mp and price
    st.header("MP and Price")
    fig = px.scatter(phone_df, x='mp', y='price', opacity = 0.25, template = 'plotly_dark', 
                    color='mp', hover_data=['mp', 'price'],title = 'PHONE PRICE PREDICTION (MEGA PIXELS - PRICE RELATIONSHIP)')
    fig.update_layout(width=900, height=500)
    st.plotly_chart(fig)

    # scatter plot of battery and price
    st.header("Battery and Price")
    fig = px.scatter(phone_df, x='battery', y='price', opacity = 0.25, template = 'plotly_dark', 
                    color='battery', hover_data=['battery', 'price'],title = 'PHONE PRICE PREDICTION (BATTERY - PRICE RELATIONSHIP)')
    fig.update_layout(width=900, height=500)
    st.plotly_chart(fig)

# adding html  Template

footer_temp = """
	 <!-- CSS  -->
	  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
	  <link href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css" type="text/css" rel="stylesheet" media="screen,projection"/>
	  <link href="static/css/style.css" type="text/css" rel="stylesheet" media="screen,projection"/>
	   <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.5.0/css/all.css" integrity="sha384-B4dIYHKNBt8Bc12p+WXckhzcICo0wtJAoU8YZTY5qE0Id1GSseTk6S+L3BlXeVIU" crossorigin="anonymous">
	 <footer class="page-footer grey darken-4">
	    <div class="container" id="aboutapp">
	      <div class="row">
	        <div class="col l6 s12">
	          <h5 class="white-text">Phone Price Prediction</h5>
	          <p class="grey-text text-lighten-4">Streamlit Practical.</p>
	        </div>
	   <div class="col l3 s12">
	          <h5 class="white-text">Connect With Me</h5>
	          <ul>
	          <a href="www.linkedin.com/in/lewis-kimtai" target="_blank" class="white-text">
	            <i class="fab fa-linkedin fa-4x"></i>
	          </a>
	           <a href="https://github.com/lewiskimtai" target="_blank" class="white-text">
	            <i class="fab fa-github-square fa-4x"></i>
	          </a>
	          </ul>
	        </div>
	      </div>
	    </div>
	    <div class="footer-copyright">
	      <div class="container">
	      Made by <a class="white-text text-lighten-3" https://lewiskimtai.github.io/">Kimtai Lewis</a><br/>
	      <a class="white-text text-lighten-3" href="https://lewiskimtai.github.io/"></a>
	      </div>
	    </div>
	  </footer>
	"""


# About Functionality
if selection == 'About':
    st.subheader("About App")
    st.text('''
                Finding a dream phone at a friendly price without compromising on the ideal features seems impossible, 
                but with this app it makes it possible. This app is built on data about different phone brands, 
                features and their respective prices.
                Trained to predict your favorite phone price according to its specs and brand making it easy for you 
                to afford your number one dream phone.
            ''')
    components.html(footer_temp, height=500)