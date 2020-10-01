apt-get install openjdk-8-jdk-headless -qq > /dev/null
wget -q https://downloads.apache.org/spark/spark-2.4.7/spark-2.4.7-bin-hadoop2.7.tgz
tar xf spark-2.4.7-bin-hadoop2.7.tgz

pip install -q findspark
pip install -q pyarrow

wget https://repo1.maven.org/maven2/org/apache/kudu/kudu-spark2_2.11/1.12.0/kudu-spark2_2.11-1.12.0.jar
mv /content/kudu-spark2_2.11-1.12.0.jar /content/spark-2.4.7-bin-hadoop2.7/jars/kudu-spark2_2.11-1.12.0.jar

wget https://github.com/welly87/spark-load/raw/master/mysql-connector-java-8.0.14.jar
mv /content/mysql-connector-java-8.0.14.jar /content/spark-2.4.7-bin-hadoop2.7/jars/mysql-connector-java-8.0.14.jar
