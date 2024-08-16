This project is on Disease Prediction by Machine Learning Model (XGBoost) from the symptoms given by the user.
The whole project is showcased in a website created using Streamlit
The app.py file needs to be run in order to run the website
When the app.py is run it will ask to run a command in the terminal to open the website (The path to the app.py file should be enclosed within this "" to avoid any error.)
data.py file loads the dataset into some pandas dataframes
Doctor.py file does the model training and testing work and serializes the model into joblib file
WebClinic.py file deserializes the joblib files (disease prediction model, label encoder and the dataset) and uses some functions to take input the list of symptoms from the user and make the model predict the disease from that list and shows the output.
order of running the files: data.py->Doctor.py->app.py
