# Gold Price Prediction using Linear Regression

## Overview

This project demonstrates a simple **Linear Regression model in Python**
to predict **Gold Prices based on S&P 500 values** using a small
simulated dataset.

The script walks through a complete data science workflow including: -
Data creation - Exploratory Data Analysis (EDA) - Handling missing
values - Training a Linear Regression model - Model evaluation -
Assumption validation - Visualization using Matplotlib

## Dataset

The dataset contains **30 days of simulated market data**: - `SP500` →
Predictor variable - `Gold` → Target variable

Some **missing gold prices are intentionally introduced** to demonstrate
handling missing values using **linear interpolation**.

## Workflow

The Python script performs the following steps:

1.  Import required libraries
2.  Generate sample dataset
3.  Perform Exploratory Data Analysis (EDA)
4.  Handle missing values
5.  Split data into training and testing sets
6.  Train a Linear Regression model
7.  Evaluate model performance using:
    -   MAE (Mean Absolute Error)
    -   MSE (Mean Squared Error)
    -   R² Score
8.  Validate linearity assumption using residual plots
9.  Visualize results using Matplotlib

## How to Run

Install dependencies:

    pip install pandas numpy matplotlib scikit-learn

Run the script:

    python gold_linear_regression_example.py

## Limitations

-   Dataset is simulated and small (30 days)
-   Only one predictor variable is used
-   Real gold price models require additional factors such as:
    -   Interest rates
    -   USD Index
    -   Inflation
    -   Geopolitical risk

## Purpose

This project is intended for **learning and demonstration of a basic
machine learning workflow using Linear Regression in Python**.
