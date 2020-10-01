#!/usr/bin/env python3

import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["SPARK_HOME"] = "/content/spark-2.4.7-bin-hadoop2.7"

driver_path = "/content/mysql-connector-java-8.0.14.jar" 

os.environ['PYSPARK_SUBMIT_ARGS'] = f'pyspark-shell --packages org.apache.kudu:kudu-spark2_2.11:1.12.0 --driver-class-path {driver_path} --jars {driver_path}'

import findspark
findspark.init("spark-2.4.7-bin-hadoop2.7")

from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Bea Cukai - PySpark/Kudu") \
    .config('spark.driver.bindAddress','localhost') \
    .config('spark.driver.allowMultipleContexts','true') \
    .config('spark.sql.execution.arrow.pyspark.enabled', 'true') \
    .getOrCreate()