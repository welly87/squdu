#!/usr/bin/env python3

import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
os.environ["SPARK_HOME"] = "/content/spark-2.4.7-bin-hadoop2.7"
os.environ["PATH"] += ":/content/spark-2.4.7-bin-hadoop2.7/bin"
os.environ["SOURCE_TABLE"] = "person"

os.environ["IMPALA_TABLE_NAME"] = "person"
os.environ["PRIMARY_KEY"] = "BusinessEntityID"
os.environ["SPARK_CMD_ARGS"] = "$SOURCE_TABLE $IMPALA_TABLE_NAME $PRIMARY_KEY"
