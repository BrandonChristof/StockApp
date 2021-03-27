# StockApp

A Web Application that displays relevant stock information by inputting a stock symbol.

## Installation

requirements.txt contains all the necessary packages to run this application. Located at StockProject/requirements.txt

```bash
pip install -r requirements.txt
```

## Usage

Change into the StockProject/ directory and run the following command:

```bash
python manage.py runserver <PORT_NUMBER>
```

Where <PORT_NUMBER> is variable. 

Then, in your browser, go to the URL:

```bash
http://localhost:<PORT_NUMBER>/
```

Search any stock ticker and click Search to display basic fundamentals and current stock price/changes. Do not search by company name - only search by stock ticker.