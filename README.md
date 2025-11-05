**Data-Driven Strategies to Reduce Recidivism & Expand Financial Inclusion in Maryland**

This repository contains the datasets, analysis notebook, AWS pipeline configuration, and Lambda automation code used to support our policy proposal and spatial equity analysis.

Leveraging Mastercard's Inclusive Growth Score to inform community-centered reentry solutions.

## 🧠 Project Summary 
Recidivism in Baltimore is not a matter of personal failure - it is the outcome of systemic financial exclusion.
This project analyzes neighborhood-level disparities between Baltimore City and Montgomery County using Mastercard's Inclusive Growth Score (IGS), public socioeconomic datasets, and incarceration data. 
Based on our findings, we propose the OpenLine Reentry Program - a place-based reentry initiative powered by reloadable Mastercard technology, compliance-based housing, and employment incentives.

**Goal:** Reduce recidivism by 10%, generate $17M+ in state savings, and expand inclusive financial access across under-served Maryland communities.

## 📍 Problem Statement
- Baltimore neighborhoods score < 45 on the IGS - signaling historic disinvestment.
- 1 in 3 Baltimore residents has a criminal record - blocking access to housing, financial remedies, and employment
- Traditional reentry policies treat returning citizens as a criminal issue, not an economic justice issue

**Our approach reframes reentry as a financial equity problem**

## 🛠️ Methodology 
1. **Cluster Selection** - Compared Baltimore City and Montgomery County zip-code clusters 
2. **Data Collection & Cleaning** - Inclusive Growth Score Platform (required dataset), BLS, Census, DPSCS processed in Excel + Python used for data transformation
3. **AWS Integration** - S3: storage, Glue: schema catalog, Athena: SQL querying, Lambda: query automation
4. **Equity Framing** - Analysis centered race, place and access, not just raw indicators 

## 📊 Data Source
- **excel-to-csv-data-chart.csv**: Primary dataset used for analysis — includes Inclusive Growth Scores, recidivism data, education, and median income by zip-code clusters
- **Tools used**: Python (Pandas), Jupyter Notebook, AWS Athena

## ⚙️ AWS Lambda Automation
This repository includes a Lambda function (lambda_function.py) that automates Athena queries 
**Function Outputs:**
- Retrieves Top 10 clusters by imprisonment_rate_2020
- Writes results to: s3://igs-md-recidivism-analysis/athena-results/

**Stack:**
- AWS Lambda (Python 3.12)
- AWS Athena
- AWS S3
- boto3

## 💡 Proposed Solution: OpenLine Reentry Program
Reentry isn't a dead end - it's an OpenLine.

**Key Features:** 

1. Reloadable Mastercard credit card - authorized purchases only (no cash misuse)
2. Structured employment + housing compliance model 
3. Rent contribution + financial coaching 
4. Participant eligibility safeguards (no fraud/gang affiliations/violent offenses)

**KPIs:**
- ↑ Employment stability 
- ↓ Recidivism 
- ↑ Credit + banking access
- ROI measured per participant + cost savings to state 

## 💳 Why Mastercard?
Mastercard has proven infrastructure for secure, reloadable payments, a public commitment to inclusive economic growth, and global experience in public-private partnerships. 
Mastercard can transform reentry into an economic mobility pipeline, rather than a cycle of incarceration.

## 🔗 References 
- [Prison Policy Initiative: Origin of Maryland’s Incarcerated Population (2023)](https://www.prisonpolicy.org/origin/md/report.html)  
- [Prison Policy Initiative: Baltimore City CSA Prison Admissions (2020)](https://www.prisonpolicy.org/origin/md/2020/baltimore_csa.html)  
- [Prison Policy Initiative: Maryland 2020 Report Overview](https://www.prisonpolicy.org/origin/md/2020/report.html)  
- [U.S. Census QuickFacts: Baltimore City, MD](https://www.census.gov/quickfacts/fact/table/baltimorecitymaryland/INC110223)  
- [Baltimore City Open Data – Community Statistical Areas](https://data.baltimorecity.gov/datasets/204beefe92a645d79fdf0969957bbdf8_0/explore?location=39.281551%2C-76.707445%2C16.00)  
- [Maryland DPSCS – Reentry Services](https://dpscs.maryland.gov/rehabservs/reentry/reentryunit.shtml)
- [Maryland Justice Reinvestment Coordinating Council: Prison Population Drivers (2015)](https://gocpp.maryland.gov/jrcc/documents/presentation-20150729-prison-drivers.pdf)
- [Mastercard Center for Inclusive Growth](https://www.mastercardcenter.org)
