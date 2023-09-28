<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/images/IDSN-logo.png" alt="Skill Network" width="400px">

# Dashboard Creation

## About
This assignment is about creating a reporting dashboard for an e-commerce company's key metrics using IBM Cognos Analytics and other required software.

## Estimated Time
30 minutes.

## Scenario
You are a data engineer at an e-commerce company. Your company has finished setting up a data warehouse. Now you are assigned the responsibility to design a reporting dashboard that reflects the key metrics of the business.

## Objectives
In this assignment you will:
- Create a dashboard using Cognos Analytics

## Software Required
- IBM Cognos Analytics or Cognos Dashboard Embedded
- Watson Studio
- (Optional) Cloud instance of IBM DB2 database

**Note:** In case you did not create an IBM Cloud account or a DB2 instance in the previous module, you can simply upload the CSV file instead into IBM Cognos Analytics.

## Note - Screenshots
Throughout this lab, you will be prompted to take screenshots and save them on your own device. You will need these screenshots to either answer graded quiz questions or to upload as your submission for peer review at the end of this course. You can use various free screengrabbing tools to do this or use your operating system’s shortcut keys to do this (for example Alt+PrintScreen in Windows).

## Pre-requisites
If you plan to use the IBM Cognos Analytics Trial version to do this lab, it is presumed that you have worked on it already. If you want to brush up on the basics of using Cognos Analytics, it is recommended that you complete the following labs:
- Getting Started with Cognos Analytics
- Different Methods for Creating Dashboard Visualizations with Cognos Analytics

If your Cognos Analytics trial has expired, it is highly recommended that you finish the Setup and Practice Assignment before you proceed with this assignment using Cognos Dashboard Embedded and Watson Studio.

---

## Environment Setup
Before you proceed with the assignment:

1. Download the data from this [link](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/analytics/ecommerce.csv).

### Exercise 1 - Load data into the data warehouse
In order to complete Tasks 1-3 below, you have an option to first load the data into a DB2 database (Option A), or load the CSV file directly into Cognos (Option B).

#### Task 1 - Import data
Option A: If you choose DB2 to complete the task:
- Import data in the downloaded file `ecommerce.csv` into a table named `sales_history`.
- Take a screenshot of the command you used to load the data into the data warehouse (DB2) and its output.

Option B: If you choose to load the data directly into Cognos:
- Upload the downloaded CSV file `ecommerce.csv` into Cognos Analytics and take a screenshot of successful loading of the CSV file into Cognos.
- Name the screenshot as `dataimport.jpg` (images can be saved with either .jpg or .png extension).

#### Task 2 - List top 10 rows
Option A: If you choose DB2 to complete the task:
- List the first 10 rows in the table `sales_history`.
- Take a screenshot of the first 10 rows of the table.

Option B: If you choose Cognos Analytics to complete the task:
- Convert the uploaded dataset `ecommerce.csv` into a Data module and take a screenshot of the first 10 rows of the table.
- Name the screenshot as `top10rows.jpg` (images can be saved with either .jpg or .png extension).

### Exercise 2 - Accessing the DataSource in Cognos
#### Task 3 - Create a data source in Cognos
Option A: If you choose DB2 to complete the task:
- Create a data source in Cognos that points to the table `sales_history` in your IBM DB2 database.
- Take a screenshot of the command you used and the output.

Option B: If you choose Cognos Analytics to complete the task:
- Take a screenshot of the `datasource` in the Cognos Analytics workspace.
- Name the screenshot as `datasource.jpg` (images can be saved with either .jpg or .png extension).

### Exercise 3 - Create a dashboard
#### Task 4 - Create a line chart
- Create a line chart of month-wise total sales for the year 2020.
- Take a screenshot of the line chart you created.
- Name the screenshot as `linechart.jpg` (images can be saved with either .jpg or .png extension).

#### Task 5 - Create a pie chart
- Create a pie chart of category-wise total sales.
- Take a screenshot of the pie chart you created.
- Name the screenshot as `piechart.jpg` (images can be saved with either .jpg or .png extension).

#### Task 6 - Create a bar chart
- Create a bar chart of Quarterly sales of mobile phones.
- Take a screenshot of the bar chart you created.
- Name the screenshot as `barchart.jpg` (images can be saved with either .jpg or .png extension).

---

## End of assignment

## Authors
- Ramesh Sannareddy

## Other Contributors
- Rav Ahuja

## Change Log
- **Date (YYYY-MM-DD)**: 2021-11-23
  - **Version**: 0.1
  - **Changed By**: Ramesh Sannareddy
  - **Change Description**: Created initial version

- **Date (YYYY-MM-DD)**: 2022-02-02
  - **Version**: 0.2
  - **Changed By**: Ramesh Sannareddy
  - **Change Description**: Updated version

- **Date (YYYY-MM-DD)**: 2023-04-28
  - **Version**: 0.3
  - **Changed By**: Steve Ryan
  - **Change Description**: Edits from Item Level Feedback

- **Date (YYYY-MM-DD)**: 2023-06-24
  - **Version**: 0.4
  - **Changed By**: Lakshmi Holla
  - **Change Description**: Updated version

## Copyright
Copyright (c) 2022 IBM Corporation. All rights reserved.