# Loan Credit Scorecard.
# Project Link
https://loan-credit-scorecard.streamlit.app/

## Problem Statement.
Financial institutions play a crucial role in providing loans to individuals and businesses, enabling them to meet their financial goals. However, the process of evaluating loan applications and determining creditworthiness can be complex and time-consuming. To streamline this process and make more informed lending decisions, the financial institution aims to develop a predictive credit scorecard model.

## Project Breakdown.
This project comprises of three code file:

- #### scorecard.ipynb 
    -  Loads the data from [Loan.xlsx] and does the Exploratory Data Analysis on the data.
    -  Data preprocessing steps(Handling outliers & Feature Engineering)
    - Fits and trains the data on an Ensemble Binary Classification algorithm (Random Forest Classifier) since we are predicting a target with only 2 values (Binary Classification Problem)
    - Saves the model into the [scorecard.pkl] file.

- #### main.py 
    - Loads the model and uses FASTAPI to create an API hosted on Heroku. 
    - Manages requests and makes predictions based on the parameters.

- #### streamlit.py 
    - The API endpoint that comprises of the User Interface in Streamlit.
    - Takes in user inputs and passes the values through the API and makes predictions.
    - Also comprises of the Exploratory Data Analysis functionality that is a dashboard for the user to visualize the data.

## Tools used:
As seen in the [requirements.txt] file
-   fastapi==0.89.1
-   gunicorn==20.1.0
-   matplotlib==3.5.1
-   matplotlib-inline==0.1.3
-   numpy==1.22.3
-   openpyxl==3.0.10
-   pandas==1.4.3
-   pickleshare==0.7.5
-   plotly==5.10.0
-   requests==2.27.1
-   scikit-learn==1.1.3
-   seaborn==0.11.2
-   streamlit==1.12.2
-   urllib3==1.26.9


### Create a virtual environment
1. Install virtualenv:
```sh
pip install virtualenv
``` 
2. Create a virtualenv using the following command:
 ```sh
virtualenv env
```
3. To activate the environment you must be in the directory where the environment was created
 ```sh
cd env
```
then
 ```sh
Scripts\activate 
```
4. Install dependancies.
 ```sh
pip install -r requirements. txt
```