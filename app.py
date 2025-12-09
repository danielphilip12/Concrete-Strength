from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    # input=[float(x) for x in request.form.values()]
    inputs = []
    for x in request.form.values():
        try:
            inputs.append(float(x))
        except ValueError:
            inputs.append(x)  # keep as string if not a number
    print(request.form.keys())
    # gets the inputs from the submitted form's values. 
    print(inputs)
   
    input_array = np.array(inputs).reshape(1, -1)
    df = pd.DataFrame(columns=request.form.keys(), data=input_array)
    print(df)
    # reshapes the array of the inputs into a format the model can understand. 
    output=model.predict(df)[0].round(2)

    # makes the prediction of the inputs passed in with the model. 
    return render_template("home.html", prediction_test=output)
# returns the home.html template with prediction_test value passed in so it displays on the page. 


if __name__ == "__main__":
    app.run(debug=True)