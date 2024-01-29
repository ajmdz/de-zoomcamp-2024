-- Create an external table from the GCS bucket parquet files
CREATE OR REPLACE EXTERNAL TABLE `taxi_data.green_2022_external`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://de-zoomcamp-409609-demo-bucket/green_taxi_2022/green_tripdata_2022-*.parquet']
);

-- Create a materialized table from the external table
CREATE OR REPLACE TABLE taxi_data.green_2022_materialized
AS
SELECT * FROM taxi_data.green_2022_external;

-- Partition by lpep_pickup_datetime Cluster on PULocationID
CREATE OR REPLACE TABLE taxi_data.green_2022_partitioned_clustered
PARTITION BY DATE(lpep_pickup_datetime)
CLUSTER BY PULocationID AS
SELECT * FROM taxi_data.green_2022_external;