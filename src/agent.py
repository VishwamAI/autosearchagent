import re
import requests
import nltk
from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer

# Ensure necessary NLTK data packages are downloaded
nltk.download('punkt')

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")


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
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            return soup.get_text()
        else:
            return None
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None


def summarize_text(text):
    """
    Summarize the given text using Sumy's LsaSummarizer.
    """
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, 2)  # Summarize the text into 2 sentences
    return " ".join([str(sentence) for sentence in summary])


def handle_query(query):
    """
    Handle the input query by breaking it down, performing web searches, and summarizing the results.
    """
    sub_queries = break_down_query(query)
    results = []

    for sub_query in sub_queries:
        # Perform a web search for the sub-query
        search_results = search(sub_query, tld="com", num=1, stop=1, pause=2)
        for url in search_results:
            print(f"Accessing URL: {url}")  # Debugging print statement
            scraped_data = scrape_data(url)
            if scraped_data:
                print(f"Scraped Data: {scraped_data[:500]}")  # Debugging print statement
                summary = summarize_text(scraped_data)
                print(f"Summary: {summary}")  # Debugging print statement
                results.append(summary)
            else:
                print(f"Failed to scrape data from URL: {url}")  # Debugging print statement

    if not results:
        print("No valid data found from the URLs.")
    return results


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

    # Example summarization
    if scraped_data:
        summary = summarize_text(scraped_data)
        print("Summary:", summary)

    # Example handling of a query
    results = handle_query(query)
    print("Results:", results)
