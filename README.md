#  Vacancies Pipeline

A data pipeline for extracting, cleaning, visualising, and forecasting job vacancies using UK Office for National Statistics (ONS) data.

##  Overview

This project aims to:
- Retrieve vacancy data from ONS sources.
- Clean and preprocess the data for analysis.
- Generate visualisations to explore trends and revisions.
- Apply a forecasting model to predict future vacancies.

## Project Structure
- `config/`: Configuration file for the pipeline.
- `data/`: Contains raw and processed data files.
- `output/`: Stores visualisations and model outputs.
- `pipeline.ipynb`: Jupyter notebook implementing the pipeline.
- `requirements.txt`: List of required Python packages.

## Getting Started
### Prerequisites
- Python 3.7 or higher
- Jupyter Notebook
- Required Python packages (see `requirements.txt`)

### Installation
```bash
git clone https://github.com/nurikhayal/vacancies.git
cd vacancies
pip install -r requirements.txt
```
### Running the Pipeline
1. Open `config/config.ini` to set parameters (e.g., data source URLs, forecast parameters). Save the file.
2. Open and run `pipeline.ipynb` in Jupyter Notebook.
3. Visualisations and model outputs will be saved in the `output/` directory.

## Data Sources
- UK Office for National Statistics (ONS) vacancy data.

## Contact
**Nuri Khayal**  
Lead Policy Analyst  
Bank of England  
https://github.com/nurikhayal 

