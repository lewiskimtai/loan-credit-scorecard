# 1. Library imports
import pandas as pd
import numpy as np
import pickle
from fastapi import FastAPI
import uvicorn

# 2. Create the app object
app = FastAPI()

#. Load Model
loaded_model = pickle.load(open("scorecard.pkl", "rb"))

# Define predict function
@app.post('/predict')
def predict(CHK_ACCT, DURATION,	HISTORY, SAV_ACCT, EMPLOYMENT, REAL_ESTATE,	PROP_UNKN_NONE,	AGE, OTHER_INSTALL,	OWN_RES):
    data = pd.DataFrame([[CHK_ACCT, DURATION,	HISTORY, SAV_ACCT, EMPLOYMENT, REAL_ESTATE,	PROP_UNKN_NONE,	AGE, OTHER_INSTALL,	OWN_RES]])
    data.columns = ['CHK_ACCT', 'DURATION',	'HISTORY', 'SAV_ACCT', 'EMPLOYMENT', 'REAL_ESTATE',	'PROP_UNKN_NONE',	'AGE', 'OTHER_INSTALL',	'OWN_RES']

    predictions = np.exp(loaded_model.predict(data)) 
    return {'prediction': int(predictions[0])}

# if __name__ == '__main__':
#     uvicorn.run(app, host='127.0.0.1', port=8000)