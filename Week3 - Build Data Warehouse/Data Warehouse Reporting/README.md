<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/images/IDSN-logo.png" alt="Skill Network" width="400px">


# Data Warehouse Reporting

### Software Used in this Lab
To complete this lab you will utilize the relational database service available as part ofIBM Skills Network Labs (SN Labs) Cloud IDE. SN Labs is a virtual lab environment used in this course.
<p align="center">
  <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/images/postgresql.png" alt="Skill Network" width="150px">
</p>

### Scenario
You are a data engineer hired by an ecommerce company named SoftCart.com . The company retailsdownload only items like E-Books, Movies, Songs etc. The company has international presence andcustomers from all over the world. You have designed the schema for the data warehouse in the previousassignment. Data engineering is a team game. Your senior data engineer reviewed your design. Your schemadesign was improvised to suit the production needs of the company. In this assignment you will generatereports out of the data in the data warehouse.
### Objectives
In this assignment you will:
- Load data into Data Warehouse
- Write aggregation queries
- Create MQTs
Throughout this lab you will be prompted to take screenshots and save them on your owndevice. You will need these screenshots to either answer graded quiz questions or to upload asyour submission for peer review at the end of this course. You can use various freescreengrabbing tools to do this or use your operating system’s shortcut keys to do this (forexample Alt+PrintScreen in Windows).
### About the dataset
The dataset you would be using in this assignment is not a real life dataset. It was programmatically created for this assignment purpose.


## Lab Setup

Before starting the assignment, ensure you perform the following steps:

1. [Download the SQL file](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/CREATE_SCRIPT.sql) and save it to your local system.
2. Start the PostgreSQL server.
3. Create a new database named "Test1".
4. Create the following tables:
   - DimDate
   - DimCategory
   - DimCountry
   - FactSales

## Loading Data

### Task 1 - Load data into the dimension table DimDate

- [Download data](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/data/DimDate.csv
)
- Load the data into the DimDate table.
- Take a screenshot of the first 5 rows in the DimDate table and name it `DimDate.jpg`.

### Task 2 - Load data into the dimension table DimCategory

- [Download data](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/DimCategory.csv)
- Load the data into the DimCategory table.
- Take a screenshot of the first 5 rows in the DimCategory table and name it `DimCategory.jpg`.

### Task 3 - Load data into the dimension table DimCountry

- [Download data](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/DimCountry.csv)
- Load the data into the DimCountry table.
- Take a screenshot of the first 5 rows in the DimCountry table and name it `DimCountry.jpg`.

### Task 4 - Load data into the fact table FactSales

- [Download data](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/FactSales.csv)
- Load this data into the FactSales table.
- Take a screenshot of the first 5 rows in the FactSales table and name it `FactSales.jpg`.

## Queries for Data Analytics

### Task 5 - Create a grouping sets query

Create a grouping sets query using the columns country, category, totalsales. Take a screenshot of the SQL query and the output rows. Name the screenshot `groupingsets.jpg`.

### Task 6 - Create a rollup query

Create a rollup query using the columns year, country, and totalsales. Take a screenshot of the SQL query and the output rows. Name the screenshot `rollup.jpg`.

### Task 7 - Create a cube query

Create a cube query using the columns year, country, and average sales. Take a screenshot of the SQL query and the output rows. Name the screenshot `cube.jpg`.

### Task 8 - Create an MQT

Create an MQT named `total_sales_per_country` that has the columns country and total_sales. Take a screenshot of the SQL query. Name the screenshot `mqt.jpg`.

## End of the Assignment

### Authors

[Niveditha Pandith](https://www.linkedin.com/in/niveditha-pandith-53a057231?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDB0321ENSkillsNetwork867-2022-01-01)

### Other Contributors
- Rav Ahuja

## Change Log

| Date (YYYY-MM-DD) | Version | Changed By          | Change Description              |
| ------------------ | ------- | ------------------- | -------------------------------- |
| 2022-12-16         | 0.3     | Niveditha Pandith   | Converted initial version to Postgres |
| 2021-12-12         | 0.1     | Ramesh Sannareddy   | Created initial version         |
| 2022-02-02         | 0.2     | Ramesh Sannareddy   | Updated version                |

**Copyright (c) 2022 IBM Corporation. All rights reserved.**
