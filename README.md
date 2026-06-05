# Amazon Sales Data Cleaning and Preprocessing

## Overview

This project focuses on cleaning and preprocessing Amazon sales data using Python. The goal is to improve data quality by handling missing values, removing duplicate records, and standardizing data formats before loading the processed data into MySQL for analysis.

## Features

* Handle missing (null) values
* Remove duplicate records
* Standardize and clean data formats
* Export cleaned data for further analysis
* Load processed data into MySQL
* Run the workflow in a Linux environment
* Version control using Git and GitHub

## Technologies Used

* Python
* Pandas
* MySQL
* Linux
* Git & GitHub

## Workflow

1. Read raw Amazon sales data from CSV files.
2. Identify and handle missing values.
3. Remove duplicate records.
4. Standardize data formats and clean inconsistencies.
5. Generate a refined dataset.
6. Load the cleaned data into MySQL.
7. Validate the loaded data for analysis.

## Project Structure

```text
Amazon-Sales-Data-Cleaning/
│
├── data/
│   ├── raw_data.csv
│   └── cleaned_data.csv
│
├── scripts/
│   └── data_cleaning.py
│
├── sql/
│   └── load_data.sql
│
├── README.md
└── requirements.txt
```

## Learning Outcomes

* Data cleaning and preprocessing using Python
* Working with structured datasets using Pandas
* Loading data into MySQL databases
* Linux-based workflow execution
* Git and GitHub version control practices

## Future Improvements

* Automate the workflow using scheduling tools
* Add data validation checks
* Generate summary reports and visualizations
* Integrate logging and error handling
