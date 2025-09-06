
# Modular Car Data Scraper & Analyzer

This project is a modular system for scraping car data from a website, processing it through a server, and analyzing the results. The system consists of three main components: a web scraper client, a data processing server, and a data analyzer.

## Project Structure

```
├── client.py          # Web scraper client
├── server.py          # Data processing server
└── fileAnalyzer.py    # Data analysis module
```

## Components

### 1. client.py (Web Scraper)
- **Purpose**: Scrapes car data from a target website
- **Functionality**:
  - Authenticates with the website
  - Scrapes car listings from multiple pages
  - Extracts car details (company, model, year, trim, kilometer, price)
  - Sends extracted data to the server
  - Receives processed data and saves it to `file.txt`
- **Key Libraries**: `requests`, `BeautifulSoup`, `json`, `re`, `socket`

### 2. server.py (Data Processor)
- **Purpose**: Processes scraped car data using a custom spreadsheet-like language
- **Functionality**:
  - Listens for connections from the client
  - Creates tables to store car data
  - Implements a custom language for data manipulation
  - Processes and analyzes car data
  - Sends processed data back to the client
- **Key Features**:
  - Custom spreadsheet language with cell references (e.g., `A1`, `B2`)
  - Arithmetic operations (+, -, *, /)
  - Variable assignment and context management
  - Hash-based cell addressing system

### 3. fileAnalyzer.py (Data Analyzer)
- **Purpose**: Analyzes processed car data
- **Functionality**:
  - Reads processed data from `file.txt`
  - Performs various statistical analyses:
    - Model comparison between companies
    - Production year analysis
    - Price analysis by company
    - Specific model analysis (e.g., Peugeot 206)
  - Uses pandas and numpy for data manipulation
- **Key Libraries**: `json`, `numpy`, `pandas`

## Setup Instructions

1. **Install Dependencies**:
   ```bash
   pip install requests beautifulsoup4 numpy pandas
   ```

2. **Start the Server**:
   ```bash
   python server.py
   ```
   The server will start listening on port 9999.

3. **Run the Client**:
   ```bash
   python client.py
   ```
   The client will scrape data, send it to the server, and save processed data to `file.txt`.

4. **Analyze the Data**:
   ```bash
   python fileAnalyzer.py
   ```
   The analyzer will process the data and print statistical results.

## Data Flow

1. **Scraping Phase**:
   - `client.py` scrapes car data from the website
   - Data is sent to `server.py` via socket connection

2. **Processing Phase**:
   - `server.py` processes data using custom spreadsheet language
   - Processed data is sent back to `client.py`

3. **Analysis Phase**:
   - `fileAnalyzer.py` reads processed data from `file.txt`
   - Performs statistical analysis and prints results

## Key Features

- **Modular Design**: Each component has a distinct responsibility
- **Custom Spreadsheet Language**: Implemented in `server.py` for data manipulation
- **Real-time Processing**: Data is processed as it's scraped
- **Statistical Analysis**: Comprehensive analysis of car market data

## Notes

- The scraper uses hardcoded credentials for authentication
- The server implements a custom hash-based addressing system for cells
- Analysis results are printed to the console (can be modified to save to files)
- The system is designed to handle 500 pages of car listings

## Output Files

- `file.txt`: Contains processed car data in JSON format
- Console output: Statistical analysis results from `fileAnalyzer.py`

This modular system provides a complete solution for web scraping, data processing, and analysis of car market data. Each component can be developed and tested independently while maintaining interoperability through standardized data formats.
