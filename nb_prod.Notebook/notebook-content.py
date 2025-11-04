# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "7db192c3-b2af-41e0-a856-758510511fae",
# META       "default_lakehouse_name": "lh_prod",
# META       "default_lakehouse_workspace_id": "2fd3687f-104a-4ada-a52e-22a1720ecd6b",
# META       "known_lakehouses": [
# META         {
# META           "id": "7db192c3-b2af-41e0-a856-758510511fae"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

from pyspark.sql.types import *
from pyspark.sql.functions import *
from decimal import Decimal

schema = StructType([
    StructField("s", StringType(), True),
    StructField("i", IntegerType(), True),
    StructField("l", LongType(), True),
    StructField("sh", ShortType(), True),
    StructField("d", DoubleType(), True),
    StructField("dec", DecimalType(10, 2), True)
])
        
data = [
    ("B", 45, 67, 5, 11.9, Decimal('9.5555')),
    ("B", 1, 5, 5, 5.9, Decimal('3.1111')),
    ("B", 2, 20, 6, 2.5, Decimal('0.01')),
    ("B", 2, 20, 6, 2.5, Decimal('0.01')),
    ("B", 2, 20, 6, 2.5, Decimal('0.01')),
    ("B", 2, 20, 6, 2.5, Decimal('0.01')),
    ("B", 2, 20, 6, 2.5, Decimal('0.01'))
]
        
df = spark.createDataFrame(data, schema)
df.write.mode('overwrite').save("abfss://POV_PROD@onelake.dfs.fabric.microsoft.com/lh_prod.Lakehouse/Tables/001_poc_prod")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
