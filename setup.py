from setuptools import setup, find_packages

setup(
    name="tagalog-checker",
    version="0.1",
    description="A simple package to check if a file contains common Tagalog terms.",
    author="Christan Shane Plaza",
    packages=find_packages(),
    package_data={
        "tagalog_checker": ["tagalog_terms.json"]  # Include the JSON file
    },
    install_requires=[],
    entry_points={
        "console_scripts": ["tagalog-checker=tagalog_checker.checker:check_file_for_tagalog_terms"]
    }
)
