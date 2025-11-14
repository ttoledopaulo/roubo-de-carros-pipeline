from pyspark.sql import SparkSession

def get_spark(app_name="roubo_de_carros_pipeline"):
    spark = (
        SparkSession.builder
        .appName(app_name)
        .master("local[*]")   # em cloud vira o url do cluster
        .config("spark.sql.shuffle.partitions", "8")
        .config("spark.sql.caseSensitive", "false")
        .getOrCreate()
    )
    return spark
