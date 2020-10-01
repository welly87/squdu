export PATH=$PATH:/content/spark-2.4.7-bin-hadoop2.7/bin
export SOURCE_TABLE=person
export IMPALA_TABLE_NAME=person
export PRIMARY_KEY=BusinessEntityID
export SPARK_CMD_ARGS="$SOURCE_TABLE $IMPALA_TABLE_NAME $PRIMARY_KEY"