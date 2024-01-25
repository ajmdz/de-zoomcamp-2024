if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    
    # Remove rows with 0 passenger count or trip distance
    data = data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]

    # Create pickup date column from pickup datetime
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    # Rename columns in camel case to snake case
    data.columns = ['vendor_id', 'lpep_pickup_datetime', 'lpep_dropoff_datetime',
       'store_and_fwd_flag', 'ratecode_id', 'pu_location_id', 'do_location_id',
       'passenger_count', 'trip_distance', 'fare_amount', 'extra', 'mta_tax',
       'tip_amount', 'tolls_amount', 'ehail_fee', 'improvement_surcharge',
       'total_amount', 'payment_type', 'trip_type', 'congestion_surcharge',
       'lpep_pickup_date']

    return data


@test
def test_output(output, *args) -> None:
    assert 'vendor_id' in output.columns, "vendor_id column not found"
    assert output['passenger_count'].isin([0]).sum() == 0, "There are rides with zero passengers"
    assert output['trip_distance'].isin([0]).sum() == 0, "There are rides with zero distance"
