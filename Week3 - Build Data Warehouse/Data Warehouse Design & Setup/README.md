<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/images/IDSN-logo.png" alt="Skill Network" width="400px">


# Data Warehousing

This assignment is part of the Skills Network Labs Cloud IDE, providing a hands-on environment for data warehousing projects. In this assignment, you will design and implement a data warehouse for an ecommerce company named SoftCart.com.

### About the Environment
- Estimated time needed: 60 minutes
- Environment: SN Labs Cloud IDE
- Tools/Software: pgAdmin ERD Design Tool, PostgreSQL Database Server
- Important Notice: Sessions in this lab environment are not persistent, so save your data to avoid losing it.

## Scenario
You are a data engineer hired by SoftCart.com, an international ecommerce company. Your task is to design a data warehouse to enable the creation of various sales reports.

## Objectives
In this assignment, you will:
1. Design a Data Warehouse using the pgAdmin ERD design tool.
2. Create the schema in the Data Warehouse.

## Tools / Software
- ERD Design Tool of pgAdmin
- PostgreSQL Database Server

## Note - Screenshots
Throughout this lab, you'll be prompted to take screenshots for reference.

### About the Dataset
The dataset used in this assignment is programmatically created for this purpose.

## Exercise 1 - Design a Data Warehouse
The ecommerce company has provied you the sample data.
![Ecommerce Sample Data](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/ecom-sample-data.png)

### Task 1 - Design the dimension table `softcartDimDate`
Design the table `softcartDimDate` using the ERD design tool, focusing on daily granularity. Here's a partial list of example fields:
- dateid
- month
- monthname
- ...

Take a screenshot of the table `softcartDimDate` in the ERD tool, displaying all field names and data types.

Screenshot Name: `softcartDimDate.jpg`

### Task 2 - Design the dimension table `softcartDimCategory`
Design the table `softcartDimCategory` using the ERD design tool.

### Task 3 - Design the dimension table `softcartDimItem`
Design the table `softcartDimItem` using the ERD design tool.

### Task 4 - Design the dimension table `softcartDimCountry`
Design the table `softcartDimCountry` using the ERD design tool.

### Task 5 - Design the fact table `softcartFactSales`
Design the table `softcartFactSales` using the ERD design tool. Take a screenshot of the table, displaying all field names and data types.

Screenshot Name: `softcartFactSales.jpg`

### Task 6 - Design the Relationships
Design the required relationships (one-to-one, one-to-many, etc.) among the tables. Take a screenshot of the entire ERD, showing all relationships among the tables.

Screenshot Name: `softcartRelationships.jpg`

## Exercise 2 - Create the Schema
In this exercise, you will create the schema of the data warehouse.

### Task 7 - Create the Schema
Download the schema SQL from the ERD tool and create the schema in a database named `staging`. Take a screenshot showing the success of the schema creation.

Screenshot Name: `createschema.jpg`

## End of the Assignment

### Authors
- Ramesh Sannareddy

### Other Contributors
- Rav Ahuja

### Change Log
- 2021-12-12: Version 0.1 by Ramesh Sannareddy (Created initial version)
- 2022-02-02: Version 0.2 by Ramesh Sannareddy (Updated version)
- 2022-09-14: Version 0.3 by Appalabhaktula Hema (Updated instructions)
- Copyright (c) 2022 IBM Corporation. All rights reserved.


