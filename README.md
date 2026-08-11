# NASA-FIRM-
# NASA FIRMS Fire Data Analysis

## Overview

This project analyzes NASA FIRMS (Fire Information for Resource Management
System) active fire data using memory-efficient and sustainable computational
techniques.

The project uses MODIS and VIIRS satellite fire-detection datasets and focuses
on performing meaningful data analysis while reducing unnecessary memory usage
and computational overhead.

## Project Objectives

The main objectives are:

- Analyze NASA FIRMS active fire datasets
- Compare MODIS and VIIRS fire detections
- Analyze Fire Radiative Power (FRP)
- Investigate missing values
- Analyze day and night fire detections
- Study monthly fire-detection patterns
- Visualize geographic fire distributions
- Apply memory-efficient computational techniques

## Project Structure

```text
NASA-FIRMS-Analysis/
│
├── data/
│   ├── Dataset1.csv
│   ├── Dataset2.csv
│   ├── Dataset3.csv
│   └── README.md
│
├── Analysis.code/
│   ├── nasa_firms_analysis.ipynb
│   └── README.md
│
├── tests/
│   └── tests_analysis.py
│
├── doc/
│   └── methodology.md
│
├── README.md
├── requirements.txt
├── pyproject.toml
└── .gitignore
```

## Dataset

Three NASA FIRMS active-fire datasets are stored in the `data/` directory.

The datasets contain satellite-based active fire observations with variables
such as:

- Latitude
- Longitude
- Brightness
- Scan
- Track
- Acquisition date and time
- Satellite
- Instrument
- Confidence
- Fire Radiative Power (FRP)
- Day/Night detection

## Analysis

The analysis is performed in the Jupyter Notebook located in:

```text
Analysis.code/nasa_firms_analysis.ipynb
```

The analysis includes:

- Data loading and optimization
- Memory usage comparison
- FRP summary statistics
- Missing-value analysis
- FRP distribution
- Geographic fire distribution
- Day/night fire detection comparison
- Monthly fire-detection trends

## Sustainable Computational Techniques

The project applies several techniques to reduce memory usage and
computational waste.

### Explicit Data Types

Appropriate numerical and categorical data types are assigned during data
loading to reduce memory requirements.

### Downcasting and Categoricals

Numerical values are stored using smaller suitable data types where possible,
and repeated categorical values are represented using categorical data types.

### Chunked Ingestion

Large CSV datasets are processed in smaller chunks rather than loading the
complete dataset into memory at once.

### Single-Pass Aggregation

Summary statistics are calculated while chunks are being processed, reducing
the need for repeated processing.

### Reuse of Derived Summaries

Previously calculated summaries are reused for analysis and visualization
where possible.

### Garbage Collection

Python's built-in `gc` module is used to support memory management by removing
unnecessary objects from memory when they are no longer required.

## Technologies Used

- Python
- Jupyter Notebook
- NumPy
- Pandas
- Matplotlib

Python's built-in `gc` module is also used for memory management.

## Installation

Clone or download the repository and install the required Python packages:

```bash
pip install -r requirements.txt
```

The main dependencies are listed in `requirements.txt` and
`pyproject.toml`.

## Running the Project

1. Install the required dependencies.
2. Make sure the three datasets are available in the `data/` folder.
3. Open:

```text
Analysis.code/nasa_firms_analysis.ipynb
```

4. Run the notebook cells in order.

## Documentation

A detailed explanation of the computational methodology is available at:

```text
doc/methodology.md
```

## Data Source

NASA FIRMS Active Fire Dataset (MODIS/VIIRS).

## Author

**Arvind Bose**

NASA FIRMS Active Fire Data Analysis  
Sustainable Computational Engineering
