# Medical Data Analysis Test Script

## Overview

This README provides an overview of the `test_calculator.py` script, which is designed to test the functionality of the 
`calculator.py` script. The `calculator.py` script processes and analyzes medical examination data, including calculating 
BMI, normalizing data, converting data formats, cleaning data, and visualizing the results.

## Prerequisites

Before running the tests, ensure you have the following packages installed:

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `unittest`

You can install these dependencies using the following command:

```sh
pip install requirements.txt
```

## Test Script Details

The `test_calculator.py` script contains unit tests for each function in the `calculator.py` script. It uses Python's 
built-in `unittest` framework to define and run the tests.

### Test Functions

1. **test_load_data**
   - Tests the `load_data` function to ensure it correctly loads data from a CSV file.

2. **test_process_data**
   - Tests the `process_data` function to ensure it correctly processes the data by calculating BMI and normalizing 
cholesterol and glucose levels.

3. **test_convert_to_long_format**
   - Tests the `convert_to_long_format` function to ensure it correctly converts the data to long format for easier 
plotting.

4. **test_plot_category_data**
   - Tests the `plot_category_data` function to ensure it correctly plots the categorical data and saves the plot to the 
specified path.

5. **test_clean_data**
   - Tests the `clean_data` function to ensure it correctly cleans the data by removing invalid entries and outliers.

6. **test_plot_correlation_matrix**
   - Tests the `plot_correlation_matrix` function to ensure it correctly plots the correlation matrix and saves the plot 
to the specified path.

### Test Data

The tests use a sample DataFrame created within the script to simulate the data that would be loaded from the 
`medical_examination.csv` file. This allows the tests to run independently of the actual data file.

### Running the Tests

To run the tests, simply execute the `test_calculator.py` script. If you are using an IDE like PyCharm, you can run the 
tests directly from the IDE. Alternatively, you can run the tests from the command line using the following command:

```sh
python -m unittest test_calculator.py
```

### Example Output

The test output will indicate whether each test passed or failed. If a test fails, an error message will be displayed, 
providing details about the failure.

```sh
....
----------------------------------------------------------------------
Ran 6 tests in 0.297s

OK
```

## Error Handling

The `calculator.py` script includes error handling to manage potential issues such as missing files, empty data, and 
missing columns. The test script verifies that these errors are correctly raised and handled.

## Conclusion

The `test_calculator.py` script is an essential component for ensuring the reliability and correctness of the 
`calculator.py` script. By running these tests, you can verify that the medical data analysis functions perform as 
expected and handle various edge cases and errors appropriately.