<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/images/IDSN-logo.png" alt="Skill Network" width="400px">


# Querying data in NoSQL databases


## About This Assignment
This Skills Network Labs Cloud IDE provides a hands-on environment for course and project related labs. Itutilizes Theia, an open-source IDE (Integrated Development Environment) platform, that can be run ondesktop or on the cloud. To complete this lab, we will be using the Cloud IDE based on Theia and Mongodbrunning in a Docker container.

## Important Notice about this lab environment
Please be aware that sessions for this lab environment are not persisted. Every time you connect to this lab, anew environment is created for you. Any data you may have saved in the earlier session would get lost. Planto complete these labs in a single session, to avoid losing your data.

## Scenario
You are a data engineer at an e-commerce company tasked with designing a data platform using MongoDB as a NoSQL database. This platform will be used to store e-commerce catalog data.

## Objectives

In this assignment, you will:

- Import data into a MongoDB database.
- Query data in a MongoDB database.
- Export data from MongoDB.

## Tools / Software

- MongoDB Server
- MongoDB Command Line Backup Tools

## Important Notice

Please note that lab environments are not persisted, so any data saved in earlier sessions will be lost. Plan to complete these labs in a single session.

## Note - Screenshots
Throughout this lab you will be prompted to take screenshots and save them on your own device. You willneed these screenshots to either answer graded quiz questions or to upload as your submission for peerreview at the end of this course. You can use various free screengrabbing tools to do this or use youroperating system's shortcut keys to do this (for example Alt+PrintScreen in Windows).

## Exercise 1 - Check the Lab Environment

Before you proceed with the assignment:

- Check if you have the 'mongoimport' and 'mongoexport' installed on the lab; otherwise, install them.

## Check if 'mongoimport' and 'mongoexport' are Installed

Type the following commands in your terminal to check if 'mongoimport' and 'mongoexport' are already installed:

```bash
mongoimport
```
```bash
mongoexport
```
### Install 'mongoimport' and 'mongoexport'
If the commands above are not recognized, you can install 'mongoimport' and 'mongoexport' by following these steps:

### Download the MongoDB Database Tools:
```bash
wget https://fastdl.mongodb.org/tools/db/mongodb-database-tools-ubuntu1804-x86_64-100.3.1.tgz
```
### Extract the downloaded file:
```bash
tar -xf mongodb-database-tools-ubuntu1804-x86_64-100.3.1.tgz
```
### Add the tools to your PATH:
```bash
export PATH=$PATH:/home/project/mongodb-database-tools-ubuntu1804-x86_64-100.3.1/bin
```
Now, you should have 'mongoimport' and 'mongoexport' installed and accessible in your terminal.

### Download 'catalog.json'
Before proceeding further, download the 'catalog.json' file using the following command:

```bash
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/nosql/catalog.json
```
### Start MongoDB
To start MongoDB, you can use the following command:
```bash
start_mongo
```

With these setup steps completed, you are ready to proceed with Exercise 2.

### Exercise 2 - Working with MongoDB

### Task 1 - Import 'catalog.json' into MongoDB

Import 'catalog.json' into MongoDB server into a database named 'catalog' and a collection named 'electronics'.

- Take a screenshot of the command you used and the output.
- Name the screenshot as `mongoimport.jpg` (images can be saved with either .jpg or .png extension).

### Task 2 - List out all the Databases

Take a screenshot of the command you used and the output.

- Name the screenshot as `list-dbs.jpg` (images can be saved with either .jpg or .png extension).

### Task 3 - List out all the Collections in the Database 'catalog'

Take a screenshot of the command you used and the output.

- Name the screenshot as `list-collections.jpg` (images can be saved with either .jpg or .png extension).

### Task 4 - Create an Index on the Field “type”

Take a screenshot of the command you used and the output.

- Name the screenshot as `create-index.jpg` (images can be saved with either .jpg or .png extension).

### Task 5 - Write a Query to Find the Count of Laptops

Take a screenshot of the command you used and the output.

- Name the screenshot as `mongo-query-laptops.jpg` (images can be saved with either .jpg or .png extension).

### Task 6 - Write a Query to Find the Number of Smartphones with Screen Size of 6 Inches

Take a screenshot of the command you used and the output.

- Name the screenshot as `mongo-query-mobiles1.jpg` (images can be saved with either .jpg or .png extension).

### Task 7 - Write a Query to Find Out the Average Screen Size of Smartphones

Take a screenshot of the command you used and the output.

- Name the screenshot as `mongo-query-mobiles2.jpg` (images can be saved with either .jpg or .png extension).

### Task 8 - Export Fields '_id', 'type', 'model' from the 'electronics' Collection into a File Named 'electronics.csv'

Take a screenshot of the command you used and the output.

- Name the screenshot as `mongoexport.jpg` (images can be saved with either .jpg or .png extension).

## End of Assignment

**Authors:**
- Ramesh Sannareddy

**Other Contributors:**
- Rav Ahuja

**Change Log:**

| Date (YYYY-MM-DD) | Version | Changed By      | Change Description        |
|--------------------|---------|-----------------|---------------------------|
| 2022-04-14         | 0.2     | Lakshmi Holla  | Changed question          |
| 2021-14-18         | 0.1     | Ramesh Sannareddy | Created initial version |

**Copyright (c) 2022 IBM Corporation. All rights reserved.**

