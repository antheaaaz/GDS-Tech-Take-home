# GDS-Tech-Take-home

**Internship GDS Tech - Data Engineer CareerCoach CC4.0 Assignment**  
This repository contains the code for the take-home assignment for the Data Engineer role with GDS Tech - CareerCoach 4.0 product.

## Setup and Installation

```bash
# Clone the repository
git clone https://github.com/antheaaaz/GDS-Tech-Take-home.git

# Navigate to the repository directory
cd GDS-Tech-Take-home

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# For macOS/Linux:
source venv/bin/activate
# For Windows:
venv\Scripts\activate

# Install the required packages
pip install -r requirements.txt

```
## Assumptions

### Rating Threshold
For this project, we made the following assumptions when filtering ratings:

- We only include ratings that are in English.

- The rating texts considered are as follows:
  - **Excellent**
  - **Very Good**
  - **Good**
  - **Average**
  - **Poor**
 

##  Deploy this using AWS cloud services 
Since the project is focused on historical data and doesn't require real-time updates, AWS Glue is an ideal solution for running scheduled batch jobs. These jobs will be scheduled at regular intervals to process large volumes of data, ensuring that only new or modified records are ingested. AWS Glue’s Python Shell jobs will make API calls to Zomato's API, pulling restaurant ratings, event data, and other relevant information.

**Data Flow & Processing**:
Raw Data Storage: The raw data collected from Zomato’s API will be stored in Amazon S3 in a structured format like JSON or CSV. 

**Data Processing**: After storing raw data in S3, AWS Glue will run transformation jobs to clean, filter, and structure the data. This processed data can then be stored back in another S3 bucket or different prefixes within the same bucket, labeled as "processed" data. This helps in separating raw and processed datasets, which makes querying and managing the data easier.

**Querying Processed Data**: Once the data is processed and stored, Amazon Athena will be used to query the processed data directly from S3. 

**Visualization with QuickSight**: After querying the processed data through Athena, Amazon QuickSight can be connected to visualize the insights. QuickSight will create dashboards or reports showing restaurant ratings, events, and other insights Steven needs for his project.


## Architecture Diagram/ Data Flow Summary:
API Integration via AWS Glue Python Shell Jobs → S3 (Raw Data Storage) → AWS Glue (ETL & Processing) → S3 (Processed Data Storage) → Amazon Athena (Querying Processed Data) → Amazon QuickSight (Visualization)


