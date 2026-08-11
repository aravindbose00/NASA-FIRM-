# Methodology

## Project Overview

This project analyzes NASA FIRMS Active Fire data from MODIS and
VIIRS satellite instruments using sustainable and memory-efficient
computational techniques.

## Data Sources

Three datasets are analyzed:

- VIIRS J1
- MODIS
- VIIRS SNPP

The datasets are stored in the `data/` directory.

## Memory-Efficient Processing

Large datasets can require significant computational memory.
Therefore, this project uses several optimization techniques.

### 1. Explicit Data Types

Numerical columns are assigned appropriate data types such as
`float32` instead of using larger default data types where possible.

Categorical columns such as satellite, instrument, confidence,
version, and day/night are stored using categorical data types.

### 2. Chunked Data Processing

Instead of loading an entire CSV file into memory, datasets are
processed in smaller chunks.

This reduces peak memory consumption and makes the analysis more
suitable for large datasets.

### 3. Single-Pass Aggregation

Summary statistics are calculated while each chunk is processed.

This avoids repeatedly reading and processing the complete dataset.

### 4. Reuse of Derived Summaries

Calculated summaries are stored and reused for later analysis and
visualization instead of recomputing them.

### 5. Reservoir Sampling

A bounded reservoir sample is maintained for visualizations.

This allows representative visualization without storing every
observation in memory.

### 6. Garbage Collection

Python's built-in `gc` module is used during data processing to
support memory management.

After large temporary objects or processed chunks are no longer
required, they can be deleted and garbage collection can be triggered
using `gc.collect()`.

This supports the project's objective of reducing unnecessary memory
usage when processing large datasets.


## Analysis

The project analyzes:

- Fire Radiative Power (FRP)
- FRP mean, standard deviation, minimum and maximum
- Missing values
- Day and night fire detections
- Monthly fire-detection patterns
- Geographic distribution of active-fire detections
- Differences between satellite datasets
- 


## Sustainability

The computational approach focuses on reducing unnecessary memory
allocation, repeated computation, and redundant data processing.

The objective is to preserve analytical value while reducing
computational waste.
