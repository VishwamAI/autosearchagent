# autosearchagent
[![Python application](https://github.com/VishwamAI/autosearchagent/actions/workflows/python-app.yml/badge.svg)](https://github.com/VishwamAI/autosearchagent/actions/workflows/python-app.yml)
## Overview
The autosearchagent is an advanced search agent designed to perform web scraping, natural language processing (NLP), and summarization tasks. It is built without using any external APIs and leverages libraries such as Beautiful Soup for web scraping and spaCy for NLP and summarization.

## Features
- **Web Scraping**: Extracts relevant information from web pages.
- **Natural Language Processing**: Parses and understands queries using spaCy.
- **Summarization**: Summarizes the extracted information to provide concise responses.
- **Benchmarking**: Measures the performance of the search agent.

## Project Structure
```
VishwamAI/
├── data/               # Directory for datasets
├── models/             # Directory for storing trained models
├── scripts/            # Directory for scripts (e.g., training, preprocessing, model conversion, auto-update)
├── notebooks/          # Directory for Jupyter notebooks
├── logs/               # Directory for training logs and metrics
├── docs/               # Directory for documentation
├── config/             # Directory for configuration files
├── utils/              # Directory for utility scripts and functions
├── setup.sh            # Script for setting up the environment
├── requirements.txt    # File for specifying required dependencies
└── README.md           # Project overview and instructions
```

## Setup Instructions
1. **Clone the repository**:
    ```bash
    git clone https://github.com/VishwamAI/autosearchagent.git
    cd autosearchagent
    ```

2. **Set up the environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. **Download spaCy model**:
    ```bash
    python -m spacy download en_core_web_sm
    ```

## Usage
To use the autosearchagent, you can run the main script with a query:
```bash
python src/main.py "Your search query"
```

## Benchmarking
To benchmark the performance of the search agent, use the `benchmark.py` script:
```bash
python src/benchmark.py "Your search query"
```

## Vishwam Model
The `vishwam_model` function in `src/main.py` orchestrates the query handling process. It performs the following steps:
1. **Query Parsing**: Parses and understands the query using spaCy.
2. **Search Execution**: Executes the search and retrieves results using Beautiful Soup.
3. **Data Processing**: Processes the search results.
4. **Summarization**: Summarizes the processed data.
5. **Response Generation**: Generates a response based on the summary.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.
