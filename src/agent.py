import re
import requests
import nltk
from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup

# Ensure necessary NLTK data packages are downloaded
nltk.download('punkt')

def parse_query(query):
    """
    Parse the input query to understand the intent and extract relevant keywords.
    """
    # Tokenize the query
    tokens = word_tokenize(query.lower())

    # Remove punctuation and non-alphanumeric characters
    tokens = [re.sub(r'\W+', '', token) for token in tokens if re.sub(r'\W+', '', token)]

    return tokens

def break_down_query(query):
    """
    Break down complex queries into smaller sub-queries.
    """
    # For simplicity, split the query into sentences
    sub_queries = re.split(r'[.?!]', query)

    # Remove empty sub-queries
    sub_queries = [sub_query.strip() for sub_query in sub_queries if sub_query.strip()]

    return sub_queries

def scrape_data(url):
    """
    Scrape data from the given URL using Beautiful Soup.
    """
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.get_text()
    else:
        return None

if __name__ == "__main__":
    # Example usage
    query = "What is the capital of France? Also, tell me about the Eiffel Tower."
    parsed_query = parse_query(query)
    sub_queries = break_down_query(query)

    print("Parsed Query:", parsed_query)
    print("Sub-Queries:", sub_queries)

    # Example URL for scraping
    url = "https://en.wikipedia.org/wiki/Eiffel_Tower"
    scraped_data = scrape_data(url)
    print("Scraped Data:", scraped_data[:500])  # Print first 500 characters of scraped data
