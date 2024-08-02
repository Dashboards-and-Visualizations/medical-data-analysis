# Medical Data Analysis

This project involves processing and visualizing medical examination data. The script calculates BMI, normalizes data, 
converts data formats, cleans data, and generates visualizations to help analyze the data.

## Overview

The main script (`calculator.py`) performs the following tasks:
1. Loads and processes the medical examination data.
2. Calculates BMI and determines overweight status.
3. Normalizes cholesterol and glucose levels.
4. Converts data to long format for easier plotting.
5. Cleans the data by removing invalid entries and outliers.
6. Generates visualizations for categorical data and correlation matrices.


## Project Structure

```
medical-data-analysis/
├── data/
│   └── medical_examination.csv
├── output-figures/
│   ├── category-plot.jpg
│   └── medical-data.jpg
├── scripts/
│   ├── calculator.py
│   └── test_calculator.py
├── docs/
│   ├── results.md
│   └── tests.md
├── README.md
└── requirements.txt
```

## Setup

### Prerequisites

Ensure you have the following packages installed:

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `unittest`

You can install these dependencies using the following command:

```sh
pip install requirements.txt
```

### Files

- **`data/medical_examination.csv`**: The input data file containing medical examination data.
- **`output-figures/`**: Directory where the output figures will be saved.
- **`scripts/calculator.py`**: The main script for processing and visualizing data.
- **`scripts/test_calculator.py`**: The test script for unit testing the functions in `calculator.py`.
- **`docs/results.md`**: Directory for detailed results and analysis of the data.
- **`docs/test.md`**: Directory for detailed description of the test cases and their outcomes.

### Running the Script

To run the main script and generate the visualizations, execute the following command:

```sh
python scripts/calculator.py
```

## Results

Detailed results and analysis of the data can be found in the [results.md](results.md) file.

## Testing

Unit tests are provided to ensure the functionality of each component in the `calculator.py` script. For detailed 
information about the test cases and their outcomes, refer to the [test.md](test.md) file.

### Running the Tests

To run the tests, execute the following command:

```sh
python -m unittest scripts/test_calculator.py
```

## Error Handling

The script includes error handling for common issues such as missing files, empty data, and missing columns. These errors 
are managed and reported to ensure smooth execution.

## Visualizations

### Category Plot

This plot shows the count of various categorical variables (active, alcohol consumption, cholesterol, glucose levels, 
overweight status, smoking status) split by the presence of cardiovascular disease.

<img src="https://github.com/Dashboards-and-Visualizations/medical-data-analysis/blob/main/figures/category-plot.jpg">

### Correlation Matrix

This heatmap shows the correlation between different medical variables, helping to identify potential relationships and 
patterns.

<img src="https://github.com/Dashboards-and-Visualizations/medical-data-analysis/blob/main/figures/medical-data.jpg">

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License.

---
