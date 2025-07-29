from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json, date_trunc, when, lit
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, TimestampType

spark = (
    SparkSession.builder
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
    .config("spark.sql.catalog.spark_catalog", 
            "org.apache.spark.sql.delta.catalog.DeltaCatalog")
    .config("spark.jars.packages", "io.delta:delta-core_2.12:2.4.0")
    .getOrCreate()
)

spark.sparkContext.setLogLevel("ERROR")

df_dados_validacao = (
    spark.read.format("delta")
    .load("/data/delta/bronze/iot_emulado")
)

df_dados_validacao.show(10, truncate= False)