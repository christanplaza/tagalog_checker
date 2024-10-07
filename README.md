# Tagalog Checker

A simple Python package to check if a file contains any Tagalog terms.

## Installation

### Install via GitHub

You can install this package directly from GitHub using pip:

```bash
pip install git+https://github.com/christanplaza/tagalog-checker.git
```

### Install for Development (Optional)
If you want to install the package for development purposes, you can clone the repository and install it in editable mode:

```bash
git clone https://github.com/christanplaza/tagalog-checker.git
cd tagalog-checker
pip install -e .
```

## Usage
After installation, you can use the package to check if a file contains any common Tagalog terms.

### Example Usage
1. Import the package and call the function to check a file:

```python
from tagalog_checker.checker import check_file_for_tagalog_terms

# Specify the file path to be checked
file_path = "path/to/your/file.txt"

# Run the checker
result = check_file_for_tagalog_terms(file_path)

# Print the result (True if Tagalog terms are found, False otherwise)
print(result)
```
2. Suppose you have a text file (`file.txt`) with the following content:

```
Kamusta! Kumain ka na ba?
```

You can check if this file contains Tagalog words:
```python
result = check_file_for_tagalog_terms("file.txt")
print(result)  # Output will be True since 'Kamusta' is a Tagalog word
```

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

### License
This project is licensed under the MIT License. See the LICENSE file for details.

### Breakdown of Each Section:

1. **Installation Instructions**:
   - Describes how to install the package directly from GitHub using pip.
   - Provides an optional section for developers who want to install the package in editable mode using `pip install -e .` for making modifications.

2. **Usage Instructions**:
   - Shows users how to import the package and call the `check_file_for_tagalog_terms` function.
   - Provides a code example of how the function works.
   - Includes an example file content and what the expected output would be.

3. **Contributing**:
   - Invites users to contribute, letting them know they can submit issues or pull requests.

4. **License**:
   - Briefly explains the license under which the project is shared (MIT in this case).

### Updating the README:

Once you have updated your `README.md`, you can commit and push the changes to your repository:

```bash
git add README.md
git commit -m "Update README with usage instructions"
git push
```
