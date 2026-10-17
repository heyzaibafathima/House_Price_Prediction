# House Price Prediction System

## Project Overview

The House Price Prediction System is a machine learning project that predicts house prices based on features such as area, number of rooms, and age of the house.

This project uses **Linear Regression**, a supervised machine learning algorithm, to estimate house prices. The model is trained in Jupyter Notebook and deployed using Streamlit to provide a simple and interactive web application.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Model Training](#model-training)
- [Saving the Trained Model](#saving-the-trained-model)
- [Setting Up the Streamlit Application](#setting-up-the-streamlit-application)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Future Enhancements](#future-enhancements)

## Features

- Predicts house prices using Linear Regression.
- Handles missing values in the dataset.
- Splits the dataset into training and testing sets.
- Saves the trained machine learning model for reuse.
- Provides a simple user interface using Streamlit.
- Displays predicted house prices based on user inputs.

## Technologies Used

- **Python** – Programming language
- **Jupyter Notebook** – Data preprocessing, model training, and testing
- **Pandas** – Data loading and manipulation
- **Scikit-learn** – Linear Regression and model evaluation
- **Matplotlib** – Data visualization
- **Pickle** – Saving and loading the trained model
- **Streamlit** – Building the web application
- **PyCharm** – Developing and running the Streamlit application

## Project Structure

```text
House-Price-Prediction/
│
├── linearregression.ipynb
├── homeprices.csv
├── model.pkl
├── app.py
└── README.md
```

### File Description

- **linearregression.ipynb** – Contains the code for data preprocessing, training, and testing the Linear Regression model.
- **homeprices.csv** – Contains the housing dataset used to train the model.
- **model.pkl** – Stores the trained model for use in the Streamlit application.
- **app.py** – Contains the Streamlit code for the user interface and price prediction.
- **README.md** – Provides project information and setup instructions.

## Getting Started

### Prerequisites

Install the following before running the project:

- Python
- Jupyter Notebook or Visual Studio Code with Jupyter support
- PyCharm
- Required Python libraries

Install the libraries using the command below:

```bash
pip install pandas scikit-learn matplotlib streamlit
```

## Model Training

The model is trained using Jupyter Notebook.

1. Open `linearregression.ipynb` in Jupyter Notebook or VS Code.
2. Load the `homeprices.csv` dataset using Pandas.
3. Explore the dataset and check for missing values.
4. Replace missing values in the `rooms` column with the median.
5. Separate the input features and target variable.
6. Split the dataset into training and testing sets.
7. Create and train the Linear Regression model.
8. Generate predictions and examine the model coefficients and intercept.

The model is trained using the `LinearRegression()` class from Scikit-learn.

## Saving the Trained Model

After training the model, save it using Python's Pickle module.

Add the following code in a new cell at the end of the notebook and run it:

```python
import pickle

with open("model.pkl", "wb") as file:
    pickle.dump(reg, file)
```

Here, `reg` is the trained Linear Regression model.

After running this cell, the `model.pkl` file will be generated in the notebook's current working directory.

## Setting Up the Streamlit Application

1. Open PyCharm and create or open your project folder.
2. Locate the generated `model.pkl` file from the notebook's working directory.
3. Copy `model.pkl` into your PyCharm project folder.
4. Create a Python file named `app.py` in the same folder.
5. Add the Streamlit code to load the saved model, collect house details, and display the predicted price.

Make sure `app.py` and `model.pkl` are in the same folder.

## Running the Application

Open the terminal in PyCharm and execute:

```bash
python -m streamlit run app.py
```

Streamlit starts the application and displays a local URL in the terminal, usually:

```text
http://localhost:8501
```

Open this URL in your web browser to access the House Price Prediction System.

## Usage

1. Open the Streamlit application in your browser.
2. Enter the area of the house.
3. Enter the number of rooms.
4. Enter the age of the house.
5. Click the **Predict** Price button.
6. View the estimated house price displayed by the application.

The application uses the trained model stored in `model.pkl` to make predictions without retraining the model every time it starts.

## Project Workflow

The project follows these steps:

**Jupyter Notebook → Data Preprocessing → Model Training → Save `model.pkl` → Copy Model to PyCharm → Create `app.py` → Run Streamlit → View Predictions in Browser**

## Future Enhancements

- Improve prediction accuracy using additional housing features.
- Display evaluation metrics such as R² score and Mean Absolute Error.
- Add graphs to visualize house price trends.
- Deploy the application online so that users can access it remotely.

## Conclusion

The House Price Prediction System demonstrates how machine learning can be used to estimate house prices. By combining Linear Regression with Streamlit, the project provides a simple way to enter housing details and obtain price predictions through a web interface.

This project provides practical experience in data preprocessing, model training, model saving, and machine learning application development.
