<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/labs/module%201/images/IDSNlogo.png
" alt="Skill Network" width="200px">


## Analyse search terms on the e-commerce web server
<img src="https://www.edureka.co/blog/wp-content/uploads/2018/07/PySpark-logo-1.jpeg" alt="Py Spark" width="300px">
In this lab you will  analyze search terms data from the e-commerce web server,  load the sales forecast model and predict the sales for the year 2023.

### Install Spark
```bash
!pip install pyspark
!pip install findspark
!pip install pandas
```
### Import Libraries
```python
import findspark
findspark.init()
import pandas as pd
from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
```
### Importing Spark ML libraries
```python
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
```


### Start session
```python
sc = SparkContext()
# Creating a spark session
spark = SparkSession \
    .builder \
    .appName("Analyse search terms on the e-commerce web server") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()
```
### Download The search term dataset from the below url
https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/Bigdata%20and%20Spark/searchterms.csv

```python
df =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/Bigdata%20and%20Spark/searchterms.csv')
```

### Load the csv into a spark dataframe
```python
sdf = spark.createDataFrame(df)
```
### TASKS BEGINS
Print the number of rows and columns
```python
print("Number of rows:", sdf.count())
print("Number of columns:", len(sdf.columns))
```
### Print the top 5 rows
```python
sdf.show(5)
```
### Find out the datatype of the column searchterm
```python
sdf.select('searchterm').dtypes[0]
```
### How many times was the term gaming laptop searched?
```python
# Register the DataFrame as a temporary SQL table
sdf.createOrReplaceTempView('search_data')
query1 = "SELECT COUNT(*) AS search_times FROM search_data WHERE searchterm = 'gaming laptop'"

spark.sql(query1).show()
```
### Print the top 5 most frequently used search terms
```python
query2 = """
    SELECT searchterm, COUNT(*) AS frequency
    FROM search_data
    GROUP BY searchterm
    ORDER BY frequency DESC
    LIMIT 5
"""
result = spark.sql(query2).show()
```
### The pretrained sales forecasting model is available at the below URL
https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/Bigdata%20and%20Spark/model.tar.gz

``` bash
# Download File
!wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/Bigdata%20and%20Spark/model.tar.gz

# Extract File
!tar -zxvf model.tar.gz
```
### Load the sales forecast model
```python
# Using LinearRegressionModel to load the model
from pyspark.ml.regression import LinearRegressionModel
model = LinearRegressionModel.load('sales_prediction.model')
```
### Using the sales forecast model, predict the sales for the year of 2023
```python
def predict(year):
    assembler = VectorAssembler(inputCols=["year"], outputCol="features")
    data = [[year, 0]]
    columns = ["year", "sales"]
    _ = spark.createDataFrame(data, columns)
    __ = assembler.transform(_).select('features', 'sales')
    predictions = model.transform(__)
    predictions.select('prediction').show()

predict(2023)
```

## For the complete process, [click here](https://github.com/Makmurry/IBM-Data-Engineering-Professional-Certificate/blob/21b5c2f979fc13f42c71c4cfb0fad0f45811173c/Week6%20-%20Big%20Data%20Analytics%20With%20Spark/Spark_MLOps.ipynb)
