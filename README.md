README
------

This Python script retrieves the content of a news article from the website "[https://ge.globo.com](https://ge.globo.com/)" and saves it in a CSV file named "scrapped_data.csv".

The script uses the `requests` library to send a GET request to the URL of the article and the `BeautifulSoup` library to parse the HTML response.

The scraped text is then concatenated into a single string and written to the CSV file.

### Requirements:

-   Python 3.x
-   `requests` library (can be installed with pip)
-   `BeautifulSoup` library (can be installed with pip)
-   `csv` library (built-in)

### Usage:

1.  Save the code in a file with a `.py` extension.
2.  Make sure you have installed the required libraries.
3.  Run the script in a terminal or an IDE.
4.  Check the directory for the `scrapped_data.csv` file.

### Notes:

-   The code raises a `RuntimeError` if the status code of the response is not 200 (OK). This means that the website may have changed the structure of the page or the URL is invalid.
-   The script only retrieves the title and content of the article. Additional modifications may be needed if 