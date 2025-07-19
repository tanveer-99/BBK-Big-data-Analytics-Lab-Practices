#  This initializes Spark and creates a session for DataFrame operations.
from pyspark.sql import SparkSession

# Start Spark
#  This initializes Spark and creates a session for DataFrame operations.
spark = SparkSession.builder.appName("Biostats Analysis").getOrCreate()

# Load CSV file
#  Reads a CSV file into a Spark DataFrame with inferred schema.
df = spark.read.csv("Biostats.csv", header=True, inferSchema=True)

# View first rows
#  Displays the top rows of the DataFrame.
df.show(5)