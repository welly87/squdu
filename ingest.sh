chmod +x ./env.sh

./env.sh

spark-shell -i ingest_mysql_to_kudu.scala --driver-class-path mysql-connector-java-8.0.14.jar --jars mysql-connector-java-8.0.14.jar --packages org.apache.kudu:kudu-spark2_2.11:1.12.0  --master local[*] --conf spark.driver.bindAddress=127.0.0.1 --conf spark.driver.host=127.0.0.1 --conf spark.driver.port=7777 --conf spark.driver.args="$SPARK_CMD_ARGS"

chmod +x create_impala_table.py

./create_impala_table.py
