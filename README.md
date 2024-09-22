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
