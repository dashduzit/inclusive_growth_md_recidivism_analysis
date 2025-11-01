"""
Lambda Function: Athena Query Executor for MD Recidivism Analysis

Description: 
This AWS Lambda function triggers an Athena query to analyze recidivism rates between Baltimore City and Montgomery County using the 'baltimore_city_vs_montgomery_sheet1__csv' table stored in the 'igs_database' Athena database.

Query Results:
- Ordered by 2020 imprisonment rates (desc)
- Top 10 rows
- Exported to S3; s3://igs-md-recidivism-analysis/athena-results/

Technologies Used: 
- Python 3.12
- Boto3 for Athena client 
- S3 for query results output 
"""

import boto3
import time
import json

def lambda_handler(event, context):
    client = boto3.client('athena')
    query = """
    Select * from baltimore_city_vs_montgomery_sheet1__csv
    order by imprisonment_rate_2020 desc
    LIMIT 10;
    """
    response = client.start_query_execution(
        QueryString=query,
        QueryExecutionContext={
            'Database': 'igs_database'
        },
        ResultConfiguration={
            'OutputLocation': 's3://igs-md-recidivism-analysis/athena-results/'
        }
    )
    query_execution_id = response['QueryExecutionId']

    while True:
        results = client.get_query_execution(QueryExecutionId=query_execution_id)
        status = results['QueryExecution']['Status']['State']
        if status in ['SUCCEEDED', 'FAILED', 'CANCELLED']:
            break

        time.sleep(0.2)
        status == 'SUCCEEDED'
        return {
            'status': 'query succeeded',
            'queryExecutionID':  query_execution_id,
            'resultLocation': 's3://igs-md-recidivism-analysis/athena-results/' + query_execution_id + '.csv'
        }
        else: 
            return {
                'status': 'query failed with state: {status}',
                'queryExecutionID': query_execution_id
            }

