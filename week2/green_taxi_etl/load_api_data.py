import io
import pandas as pd
from datetime import datetime
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    
    taxi_dtypes = {
        'VendorID': pd. Int64Dtype(), 
        'passenger_count': pd. Int64Dtype(), 
        'trip_distance': float,
        'RatecodeID': pd. Int64Dtype(),
        'store_and_fwd_flag' :str,
        'PULocationID': pd. Int64Dtype(),
        'DOLocationID': pd.Int64Dtype(),
        'payment_type': pd. Int64Dtype(),
        'fare_amount': float,
        'extra': float,
        'mta_tax': float,
        'tip_amount': float,
        'tolls_amount': float,
        'improvement_surcharge': float,
        'total amount': float,
        'congestion_surcharge': float
    }

    parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']

    df = pd.DataFrame()
    for mm in range(10,13):
        url = f'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-{str(mm)}.csv.gz'
        df = pd.concat([df, pd.read_csv(url, sep=",", compression="gzip", dtype=taxi_dtypes, parse_dates=parse_dates)],
                        ignore_index=True)
        
    return df


@test
def test_output(output, *args) -> None:
    # Just checking dates that fall outside of 10-2020 to 12-2020
    start_date = datetime(2020, 10, 1).date()
    end_date = datetime(2020, 12, 31).date()
    outside_date_range = (output['lpep_pickup_datetime'].dt.date < start_date) | (output['lpep_pickup_datetime'].dt.date > end_date)
    print(output[outside_date_range].lpep_pickup_datetime)

    assert output is not None, 'The output is undefined'
    
