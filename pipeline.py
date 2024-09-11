import pandas as pd # type: ignore
from dagster import job, op, get_dagster_logger

@op
def load_data():
    get_dagster_logger().info("Loading data...")
    data = pd.DataFrame({
        'id': [1, 2, 3],
        'value': [100, 200, 300]
    })
    return data

@op
def transform_data(data: pd.DataFrame):
    get_dagster_logger().info("Transforming data...")
    data['transformed_value'] = data['value'] * 10
    return data

@op
def save_data(data: pd.DataFrame):
    get_dagster_logger().info("Saving data...")
    print(data)
    return True

@job
def simple_data_pipeline():
    data = load_data()
    transformed_data = transform_data(data)
    save_data(transformed_data)

if __name__ == "__main__":
    result = simple_data_pipeline.execute_in_process()
    assert result.success