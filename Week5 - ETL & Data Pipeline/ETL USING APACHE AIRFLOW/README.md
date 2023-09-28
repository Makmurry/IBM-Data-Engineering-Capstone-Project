<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/labs/module%201/images/IDSNlogo.png
" alt="Skill Network" width="200px">


# Data Pipelines Using Apache AirFlow

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/de/AirflowLogo.png/800px-AirflowLogo.png" alt="Skill Network" width="200px">
</p>

## About This SN Labs Cloud IDE

This Skills Network Labs Cloud IDE provides a hands-on environment for course and project related labs. It utilizes Theia, an open-source IDE (Integrated Development Environment) platform, that can be run on desktop or on the cloud. To complete this lab, we will be using the Cloud IDE based on Theia and Apache Airflow running in a Docker container.

### Important Notice about this lab environment

Please be aware that sessions for this lab environment are not persistent. A new environment is created for you every time you connect to this lab. Any data you may have saved in an earlier session will get lost. To avoid losing your data, please plan to complete these labs in a single session.

## Scenario

Write a pipeline that analyzes the web server log file, extracts the required lines (ending with html) and fields (time stamp, size) and transforms (bytes to mb) and load (append to an existing file).

## Objectives

In this assignment you will author an Apache Airflow DAG that will:

1. Extract data from a web server log file
2. Transform the data
3. Load the transformed data into a tar file

## Tools / Software

- Apache AirFlow

## Note - Screenshots

Throughout this lab you will be prompted to take screenshots and save them on your own device. You will need these screenshots to either answer graded quiz questions or to upload as your submission for peer review at the end of this course. You can use various free screengrabbing tools to do this or use your operating system’s shortcut keys to do this (for example Alt+PrintScreen in Windows).

---

## Exercise 1 - Prepare the lab environment

Before you start the assignment:

1. Start Apache Airflow.
2. Download the dataset from the source to the destination mentioned below.

**Source:** [Dataset Source](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/ETL/accesslog.txt)

**Destination:** `/home/project/airflow/dags/capstone`

---

## Exercise 2 - Create a DAG

### Task 1 - Define the DAG arguments

Create a DAG with these arguments:

- `owner`
- `start_date`
- `email`

You may define any suitable additional arguments.

**Screenshot Name:** `dag_args.jpg`

### Task 2 - Define the DAG

Create a DAG named `process_web_log` that runs daily. Use a suitable description.

**Screenshot Name:** `dag_definition.jpg`

### Task 3 - Create a task to extract data

Create a task named `extract_data`.

This task should extract the ip address field from the web server log file and save it into a file named `extracted_data.txt`.

**Screenshot Name:** `extract_data.jpg`

### Task 4 - Create a task to transform the data in the txt file

Create a task named `transform_data`.

This task should filter out all the occurrences of the ip address "198.46.149.143" from `extracted_data.txt` and save the output to a file named `transformed_data.txt`.

**Screenshot Name:** `transform_data.jpg`

### Task 5 - Create a task to load the data

Create a task named `load_data`.

This task should archive the file `transformed_data.txt` into a tar file named `weblog.tar`.

**Screenshot Name:** `load_data.jpg`

### Task 6 - Define the task pipeline

Define the task pipeline as per the details given below:

- First task: `extract_data`
- Second task: `transform_data`
- Third task: `load_data`

**Screenshot Name:** `pipeline.jpg`

---

## Exercise 3 - Getting the DAG operational

Save the DAG you defined into a file named `process_web_log.py`.

### Task 7 - Submit the DAG

**Screenshot Name:** `submit_dag.jpg`

### Task 8 - Unpause the DAG

**Screenshot Name:** `unpause_dag.jpg`

### Task 9 - Monitor the DAG

**Screenshot Name:** `dag_runs.jpg`

---

## End of the assignment.

**Authors:**
- Ramesh Sannareddy

**Other Contributors:**
- Rav Ahuja

**Change Log:**

| Date (YYYY-MM-DD) | Version | Changed By            | Change Description       |
|--------------------|---------|-----------------------|--------------------------|
| 2021-13-12         | 0.1     | Ramesh Sannareddy     | Created initial version  |
| 2022-30-01         | 0.2     | Alison Woolford       | Updated version          |
| 2022-04-14         | 0.2     | Alison Woolford       | Updated version          |

**Copyright (c) 2022 IBM Corporation. All rights reserved.**
