import pyspark
print("hello")

import pandas as pd 
pd.read_csv('Text1.csv')

from pyspark.sql import SparkSession
spark=SparkSession.builder.appName('Practise').getOrCreate()