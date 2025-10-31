# aws-athena-to-s3-pipeline
A simple AWS Lambda function that:
- Queries data from an AWS Athena table
- Waits for the query ro complete
- Saves the results into an S3 bucket

## Lambda Code (Python 3.9) 

import boto3
import json
import time

def lambda_handler(event, context):
    client = boto3.client('athena')
    response = client.start_query_execution(
        QueryString = "SELECT * FROM athena_table",
        QueryExecutionContext = {
            'Database': 'inclusive_growth'
        },
        ResultConfiguration = {
            'OutputLocation': 's3://inclusive-growth-metrics/athena-results/'
        }
    )
    query_execution_id = response['QueryExecutionId']

    while True:
        result = client.get_query_execution(QueryExecutionId=query_execution_id)
        status = result['QueryExecution']['Status']['State']
        if status in ['SUCCEEDED', 'FAILED', 'CANCELLED']:
            break
            time.sleep(2)

            return {
                'statusCode': 200,
                'body': json.dumps(f"Query {status}, ID: {query_execution_id}")
            }
