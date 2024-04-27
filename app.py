# To install the fast api package you use pip install fastapi uvicorn

# 1.Library imports
import uvicorn ##ASGI
from fastapi import FastAPI
from BankNote import BankNote
import pickle

# 2. Creatin the app object
app = FastAPI()
pickle_in = open("classifier.pkl", "rb")
classifier = pickle.load(pickle_in)

# 3. Index route opens automatically on http://127.0.0.1:8000
@app.get("/")
def index():
    return {"message": "Hello, stranger"}

# 4. Route with a single parameter, this returns the parameter within a message 
#located at same port with AnyNameHere
@app.get("/{name}") #the 
def get_name(name: str):
    return {"message": f"Hello, {name}"}

# 5. Expose the prediction function, make a prediction from the JSON data
#and return the predicted BankNote with the confidence
@app.post("/predict")
def predict_BankNote(data: BankNote):
    data = data.dict()
    variance = data["variance"]
    skewness = data["skewness"]
    curtosis = data["curtosis"]
    entropy = data["entropy"]

    #print(classifier.predict([[variance,skewness,curtosis,entropu]]))
    prediction = classifier.predict([[variance,skewness,curtosis,entropy ]])
    if (prediction[0]>0.5):
        prediction = "Fake note"
    else:
        prediction = "It's a bank note"
    return{
        "prediction" : prediction
    }
# 6. Now it is time to run the API with uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port = 8000)

#uvicorn app:app --reload   


    