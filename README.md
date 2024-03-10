# cis6930sp24 -- Assignment1 -- Censoror

## Name:
Pranil Ingle

## Assignment Description:
This assignment involves developing a system that accepts plain text documents, detects sensitive information such as names, dates, phone numbers, and addresses, and censors them. The project aims to automate the redaction process, which is typically time-consuming and expensive when done manually. The system will read input text files, identify sensitive entities, replace them with a censor character, and generate censored versions of the files. Additionally, it provides an option to generate statistics about the censoring process.

## Approach to Developing the Code

### Understanding the Requirements

The first step in developing the code was to thoroughly understand the requirements specified in the assignment prompt. This involved identifying the key tasks such as detecting and censoring sensitive information, handling various input formats, and generating statistics.

### Planning the Project Structure

Once the requirements were clear, I planned the structure of the project. This included organizing the code into modules and functions, defining the database schema, and outlining the workflow for data extraction and processing.

### Implementing the Functions

With the project structure in place, I began implementing the individual functions required to fulfill the tasks. These functions included:
- `censor_text`: Detects and censors sensitive information such as names, dates, phone numbers, and addresses in the text.
- `censor_files`: Processes input files to censor sensitive information and generate censored versions.
- `redactNames`,`redactDates`,`redactPhones`,`redactAddresses`:Functions for detecting and censoring specific types of sensitive information (names, dates, phones, addresses).

### Writing Tests

To ensure the correctness and robustness of the code, I wrote test functions to validate each function's behavior. These test functions covered various scenarios, including detecting and censoring different types of sensitive information, handling edge cases, and generating statistics accurately.

### Debugging and Refinement

Throughout the development process, I continuously debugged the code and refined the implementation to address any issues or edge cases encountered. This involved thorough testing, error handling, and optimization where necessary.

## How to Install:
Clone the repository:

git clone https://github.com/CodeRanger1998/cis6930sp24-assignment1

cd cis6930sp24-assignment1

Install dependencies using Pipenv:

pipenv install

## How to Run:

Execute the main script providing the incident summary URL:

pipenv run python censoror.py --input '*.txt' \
                    --names --dates --phones --address\
                    --output 'files/' \
                    --stats stderr

<!-- ![alt text](https://github.com/CodeRanger1998/dataEngineeringProject0/blob/main/resources/dataengineeringanimation.gif "Example run gif") -->

## Functions:

### `redactPhones(text, doc)`
- **Description:** Redacts phone numbers from the text.
- **Parameters:**
  - `text`: Input text containing phone numbers.
  - `doc`: Processed Spacy document object.
- **Returns:** Tuple containing the redacted text and the number of redacted phone numbers.

### `redactDates(text, doc)`
- **Description:** Redacts dates from the text.
- **Parameters:**
  - `text`: Input text containing dates.
  - `doc`: Processed Spacy document object.
- **Returns:** Tuple containing the redacted text and the number of redacted dates.

### `redactNames(text, doc)`
- **Description:** Redacts names from the text.
- **Parameters:**
  - `text`: Input text containing names.
  - `doc`: Processed Spacy document object.
- **Returns:** Tuple containing the redacted text and the number of redacted names.

### `redactAddresses(text)`
- **Description:** Redacts addresses from the text.
- **Parameters:**
  - `text`: Input text containing addresses.
- **Returns:** Tuple containing the redacted text and the number of redacted addresses.

### `censor_text(text, stats, censor_names=True, censor_dates=True, censor_phones=True, censor_address=True)`
- **Description:** Detects and censors sensitive information in the text.
- **Parameters:**
  - `text`: Input text to be censored.
  - `stats`: Option for generating statistics (stderr, stdout, or file path).
  - `censor_names`: Boolean indicating whether to censor names (default True).
  - `censor_dates`: Boolean indicating whether to censor dates (default True).
  - `censor_phones`: Boolean indicating whether to censor phone numbers (default True).
  - `censor_address`: Boolean indicating whether to censor addresses (default True).
- **Returns:** Tuple containing the censored text and statistics string.

### `censor_files(input_pattern, output_dir, stats, censor_names=True, censor_dates=True, censor_phones=True, censor_address=True)`
- **Description:** Processes input files to censor sensitive information and generate censored versions.
- **Parameters:**
  - `input_pattern`: File pattern(s) for input files.
  - `output_dir`: Output directory for censored files.
  - `stats`: Option for generating statistics (stderr, stdout, or file path).
  - `censor_names`: Boolean indicating whether to censor names (default True).
  - `censor_dates`: Boolean indicating whether to censor dates (default True).
  - `censor_phones`: Boolean indicating whether to censor phone numbers (default True).
  - `censor_address`: Boolean indicating whether to censor addresses (default True).
- **Returns:** None.

## Tests

### Test Functions

### `test_redactNames()`
- **Description:** Test function for redacting names.
- **Functionality:**
  - Provides a sample text containing a name.
  - Calls the `redactNames()` function with the provided text.
  - Checks if the redacted text matches the expected output (full block character).
  - Raises an assertion error if the redacted text does not match the expected output or an exception occurs.

### `test_redactDates()`
- **Description:** Test function for redacting dates.
- **Functionality:**
  - Provides a sample text containing a date.
  - Calls the `redactDates()` function with the provided text.
  - Checks if the redacted text matches the expected output (full block character).
  - Raises an assertion error if the redacted text does not match the expected output or an exception occurs.

### `test_redactPhones()`
- **Description:** Test function for redacting phone numbers.
- **Functionality:**
  - Provides a sample text containing a phone number.
  - Calls the `redactPhones()` function with the provided text.
  - Checks if the redacted text matches the expected output (full block character).
  - Raises an assertion error if the redacted text does not match the expected output or an exception occurs.

### `test_redactAddresses()`
- **Description:** Test function for redacting addresses.
- **Functionality:**
  - Provides a sample text containing an address.
  - Calls the `redactAddresses()` function with the provided text.
  - Checks if the redacted text matches the expected output (full block character).
  - Raises an assertion error if the redacted text does not match the expected output or an exception occurs.

## Stats File Contents

The `stats.txt` file will be created in the output directory. The `stats.txt` file contains statistics regarding the redaction process performed on the input text files. Each line in the `stats.txt` file corresponds to a processed input file and includes the following information:

- **File Name:** The name of the input file that was processed.
- **Number of Names Redacted:** The count of names redacted from the text in the input file.
- **Number of Dates Redacted:** The count of dates redacted from the text in the input file.
- **Number of Phones Redacted:** The count of phone numbers redacted from the text in the input file.
- **Number of Addresses Redacted:** The count of addresses redacted from the text in the input file.

This file provides an overview of the sensitive information redacted from each input file, allowing users to understand the extent of the data protection applied during the redaction process.

### Running the Tests

To run the tests, execute the following command in the terminal:

pipenv run python -m pytest

## Bugs and Assumptions:

Assumption: Sensitive information is available in the input text documents in various formats.

Assumption: The system should replace sensitive information with a censor character (e.g., █) to maintain privacy.