import org.apache.spark.sql.types._
import org.apache.spark.sql.DataFrame

import collection.JavaConverters._
import org.apache.kudu.client._
import org.apache.kudu.spark.kudu._

def setNotNull(df: DataFrame, columns: Seq[String]) : DataFrame = {
  val schema = df.schema
  // Modify [[StructField] for the specified columns.
  val newSchema = StructType(schema.map {
    case StructField(c, t, _, m) if columns.contains(c) => StructField(c, t, nullable = false, m)
    case y: StructField => y
  })
  // Apply new schema to the DataFrame
  df.sqlContext.createDataFrame(df.rdd, newSchema)
}

def load_to_kudu(source: String, table: String, keys: Seq[String]) = {
  val sfmta_raw = spark.read.format("jdbc").option("url", "jdbc:mysql://relational.fit.cvut.cz/AdventureWorks2014?serverTimezone=UTC").option("dbtable", source).option("user", "guest").option("password", "relational").load()

  sfmta_raw.createOrReplaceTempView(table)

  val notNullWhere = keys.map(x => s"$x IS NOT NULL").mkString(" AND ")

  var df = spark.sql(s"SELECT * FROM $table WHERE $notNullWhere")

  df = setNotNull(df, keys)

  val kudu_master = "178.128.112.105:7051,178.128.112.105:7151,178.128.112.105:7251"

  val kuduContext = new KuduContext(kudu_master, spark.sparkContext)

  // Delete the table if it already exists.
  if(kuduContext.tableExists(table)) {
    kuduContext.deleteTable(table)
  }

  kuduContext.createTable(table, df.schema, keys, new CreateTableOptions().setNumReplicas(3).addHashPartitions(keys.toList.asJava, 4))

  kuduContext.insertRows(df, table)

  val sfmta_kudu = spark.read.option("kudu.master", kudu_master).option("kudu.table", table).option("kudu.scanLocality", "leader_only").format("kudu").load

  sfmta_kudu.createOrReplaceTempView(table)

  spark.sql(s"SELECT count(*) FROM $table").show()
}

val params = sc.getConf.get("spark.driver.args")
// println(params)

val args = params.split("\\s+")

load_to_kudu(args(0), args(1), args.slice(2, args.length))
