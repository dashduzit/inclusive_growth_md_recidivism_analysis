Data driven solutions to reduce recidivism and promote financial inclusion in under-served Maryland communities using Mastercard's Inclusive Growth Score
## 🧠 Project Summary 
Recidivism in Baltimore isn't about unwillingness to change - it's about structural financial exclusion
Our project uses Mastercard's Inclusive Growth Score (IGS) and public data to map systemic disparities between Baltimore City and Montgomery County. We propose the OpenLine Reentry Program, a place-based reentry program powered by prepaid Mastercard technology, compliance-based housing, and employment incentives
The goal? Reduce recidivism by 10%, generate $17M+ in state savings, and drive inclusive financial opportunity across under-served Maryland communities
## 📍 Problem Focus
Baltimore neighborhoods score < 45 on the IGS - signaling disinvestment in Baltimore City.
High poverty, unemployment, and incarceration rates persist
1 in 3 Baltimore residents has a criminal record, excluding them from housing and jobs 
We asked: What if reentry was treated as a financial equity problem, not a criminal one? 
## 🛠️ Methodology 
1. **Cluster Selection** - We analyzed zip-code clusters from: Baltimore City (Penn North, Park Heights) and Montgomery County (Bethesda, North Potomac)
2. **Data Collection & Cleaning** - Inclusive Growth Score Platform (required dataset) , BLS, Census, DPSCS, HUD, Excel + Python used for data transformation
3. **AWS Integration** - S3: Hosted data and slide deck for public access and Athena: Queried cluster-level disparities
4. **Equity Framing** - Our analysis centered race, place, and access - not just raw numbers - to drive human-centered insights
## 📊 Data Source
- **excel-to-csv-data-chart.csv**: Primary dataset used for analysis — includes Inclusive Growth Scores, recidivism data, education, and median income by neighborhood cluster
- Derived from Mastercard IGS scores and Maryland public datasets
- Tools used: Python (Pandas, Matplotlib), Jupyter Notebook


## ⚙️ Lambda Function
This project includes an AWS Lambda function ('lambda_function.py') that automates query execution for recidivism analysis:

1. **Query**: Retrieves top 10 ZIP codes by 2020 imprisonment rate 
2. **Runs**: On demand, programatically through 'boto3'
3. **Output**: Results exported to S3 at 's3://igs-md-recidivism-analysis/athena-results/'
4. **Used For**: Enabling automation, reproducibility, and scalable ETL workflows 

**Technologies Used**:
- AWS Lambda (Python 3.12 runtime)
- AWS Athena (serverless query)
- AWS S3 (storage for query results)
- 'boto3' SDK
## 💡 Our Solution: OpenLine Reentry Program
Reentry isn't a dead end - it's an OpenLine.

**Pilot Program Features:** 

1. Mastercard reloadable card (authorized purchases only)
2. Mandatory employment, drug-free, compliance, and housing engagement
3. Rent contribution + financial coaching (not free but fair)
4. Exclusions: violent crimes, active gang ties
5. Measurable KPIs: empployment rate, recidivism drop, cost savings
## 💳 Why Mastercard?
Mastercard is uniquely positioned to drive financial inclusion for returning citizens. With its global payments infrastructure, deep commitment to social impact through the Inclusive Growth Score, and history of public-private partnerships, Mastercard can bring OpenLine to scale - transforming reentry from a crisis into an opportunity
## 🔗 References 
- [Prison Policy Initiative: Origin of Maryland’s Incarcerated Population (2023)](https://www.prisonpolicy.org/origin/md/report.html)  
- [Prison Policy Initiative: Baltimore City CSA Prison Admissions (2020)](https://www.prisonpolicy.org/origin/md/2020/baltimore_csa.html)  
- [Prison Policy Initiative: Maryland 2020 Report Overview](https://www.prisonpolicy.org/origin/md/2020/report.html)  
- [U.S. Census QuickFacts: Baltimore City, MD](https://www.census.gov/quickfacts/fact/table/baltimorecitymaryland/INC110223)  
- [Baltimore City Open Data – Community Statistical Areas](https://data.baltimorecity.gov/datasets/204beefe92a645d79fdf0969957bbdf8_0/explore?location=39.281551%2C-76.707445%2C16.00)  
- [Maryland DPSCS – Reentry Services](https://dpscs.maryland.gov/rehabservs/reentry/reentryunit.shtml)  
- [Mastercard Center for Inclusive Growth](https://www.mastercardcenter.org)
