from pyspark.sql import SparkSession
from service.LoggerService import LoggerService
from service.Exception import ConsumerException
from pyspark.sql.functions import col, from_json, date_trunc, when, lit
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, TimestampType

log = LoggerService('consumer').get_logger()

try:
    spark = (
        SparkSession.builder
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config("spark.sql.catalog.spark_catalog", 
                "org.apache.spark.sql.delta.catalog.DeltaCatalog")
        .config("spark.jars.packages", "io.delta:delta-core_2.12:2.4.0")
        .getOrCreate()
    )

    schema = (
        StructType([
            StructField('device_id', StringType()),
            StructField('temperature', DoubleType()),
            StructField('humidity', DoubleType()),
            StructField('date', TimestampType())
        ])
    )

    log.info('LENDO OS DADOS DO TOPICO KAFKA')
    df_iot_data = (
            spark.readStream
                .format("kafka")
                .option("kafka.bootstrap.servers", "kafka:9092")
                .option("subscribe", "iot_topic")
                .option("startingOffsets", "latest")
                .load()
    )

    log.info('FORMATANDO OS DADOS')
    df_format_json = (
        df_iot_data.selectExpr("CAST(value AS STRING) as json_str")
        .withColumn("data", from_json(col("json_str"), schema))
        .select("data.*")
    )

    df_data_formatada = (
        df_format_json.withColumn(
            'data_referencia',
            date_trunc('HOUR',col('date').cast('timestamp'))
        ).drop('date')
    )

    log.info('SALVANDO OS DADOS')
    (
        df_data_formatada.writeStream
            .format('delta')
            .outputMode("append")
            .partitionBy('data_referencia')
            .option("checkpointLocation", "/tmp/checkpoint/bronze/iot_emulado")
            .start("/data/delta/bronze/iot_emulado")
            .awaitTermination()
    )

except ConsumerException as e:

    log.error(f'Erro ao executar o consumer: {e}')

