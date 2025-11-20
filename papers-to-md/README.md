# Project Title: Papers to Markdown Converter

## Overview
This project is designed to automatically scan a specified folder for new PDF files and convert them into Markdown format. The converted files are saved in a separate directory, allowing for easy organization and access.

## Features
- Monitors the "Papers" folder for new PDF files.
- Converts detected PDF files into Markdown format.
- Saves the converted Markdown files in the "Papers md" folder.

## Project Structure
```
papers-to-md
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── watcher.py
│   ├── converter.py
│   ├── config.py
│   └── utils.py
├── Papers
├── Papers md
├── tests
│   ├── test_converter.py
│   └── test_watcher.py
├── scripts
│   └── run_watcher.sh
├── requirements.txt
├── pyproject.toml
├── .gitignore
└── README.md
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd papers-to-md
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To start monitoring the "Papers" folder and convert new PDF files, run the following command:
```
python src/main.py
```

## Running Tests
To ensure that the conversion and monitoring functionalities work as expected, run the tests using:
```
pytest tests/
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.