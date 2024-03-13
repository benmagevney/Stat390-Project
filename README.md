# Stat390-Project
### Spencer Huie, Ben Magevney, Ryan Shanker



## Problem Overview
In response to the unprecedented global challenges posed by the COVID-19 pandemic, which has severely impacted healthcare systems and economic stability worldwide, our project seeks to address the critical need for accurate COVID-19 case number forecasts. By developing time series models that incorporate historical data trends, our goal is to generate reliable regional level predictions of COVID-19 case numbers in the United States. This project aims to provide healthcare and governmental bodies with the insights needed for effective response strategies.

Our approach involves collecting extensive COVID-19 data from American states, conducting exploratory research to identify key drivers, and employing both univariate and multivariate modeling techniques for precise caseload forecasting on an aggregated regional basis. The project’s primary objective is to create advanced forecasting tools that assist governments and health organizations in strategic planning and healthcare resource management. 

## Organization
The data preparation and EDA was all done by the entire group. Each member then developed the models on their own and contained them in their own folder titled with their name and models (ex: `bens_models`)

## Working Strategy 
Each group member will work on their own branches for exploratory analysis and testing. As soon as they have accomplished their goal and the code is working, merge it into the main branch.

## Data Preparation and EDA
All data was taken from the Google COVID-19 Open Data Repository. The datasets in this repository are sourced from hundreds of sources globally, such as the WHO, The New York Times, and Eurostat. Data preparation and final datasets can be found in its own folder, data. Exploratory data analysis, developed in collaboration with all members, can also be found in its own folder, eda.
The EDA folder consists of:
* bivariate analysis
* correlation analysis
* multivariate analysis
* prophet feature selection
* seasonal decomposition
* stationarity analysis
* univariate feature analysis
* xgboost feature selection


## Models
Each team member has a separate folder whcih contains their models (building, parameter tuning, plotting, etc.).These folders contain some, but not necessarily all, of the following models:
* ARIMA
* SARIMA
* AutoARIMA
* Prophet (univariate and multivariate are separate files)
* XGBoost
* LSTM
