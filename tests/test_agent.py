import unittest
from unittest.mock import patch
from src.agent import (
    parse_query, break_down_query, scrape_data, summarize_text, handle_query,
    interactive_cli
)
from io import StringIO


class TestAgent(unittest.TestCase):

    def test_parse_query(self):
        query = (
            "What is the capital of France? Also, tell me about the Eiffel Tower."
        )
        expected_tokens = [
            'what', 'is', 'the', 'capital', 'of', 'france', 'also', 'tell', 'me',
            'about', 'the', 'eiffel', 'tower'
        ]
        self.assertEqual(parse_query(query), expected_tokens)

    def test_break_down_query(self):
        query = (
            "What is the capital of France? Also, tell me about the Eiffel Tower."
        )
        expected_sub_queries = [
            'What is the capital of France',
            'Also, tell me about the Eiffel Tower'
        ]
        self.assertEqual(break_down_query(query), expected_sub_queries)

    @patch('src.agent.scrape_data')
    def test_scrape_data(self, mock_scrape_data):
        mock_scrape_data.return_value = (
            "Eiffel Tower is a wrought-iron lattice tower on the Champ de Mars in "
            "Paris, France."
        )
        url = "https://en.wikipedia.org/wiki/Eiffel_Tower"
        scraped_data = scrape_data(url)
        self.assertIsNotNone(scraped_data)
        self.assertIn("Eiffel Tower", scraped_data)

    @patch('src.agent.scrape_data')
    def test_scrape_data_invalid_url(self, mock_scrape_data):
        mock_scrape_data.return_value = None
        url = "https://en.wikipedia.org/wiki/Invalid_Page"
        scraped_data = scrape_data(url)
        self.assertIsNone(scraped_data)

    def test_summarize_text(self):
        text = (
            "The Eiffel Tower is a wrought-iron lattice tower on the Champ de Mars in "
            "Paris, France. It is named after the engineer Gustave Eiffel, whose "
            "company designed and built the tower. Locally nicknamed 'La dame de fer' "
            "(French for 'Iron Lady'), it was constructed from 1887 to 1889 as the "
            "centerpiece of the 1889 World's Fair."
        )
        summary = summarize_text(text)
        self.assertIsNotNone(summary)
        self.assertIn("Eiffel Tower", summary)

    def test_summarize_text_short(self):
        text = "Eiffel Tower"
        summary = summarize_text(text)
        self.assertIsNotNone(summary)
        self.assertIn("Eiffel Tower", summary)

    @patch('src.agent.scrape_data')
    def test_handle_query(self, mock_scrape_data):
        mock_scrape_data.return_value = (
            "Paris is the capital of France. The Eiffel Tower is a famous landmark in "
            "Paris."
        )
        query = (
            "What is the capital of France? Also, tell me about the Eiffel Tower."
        )
        results = handle_query(query)
        self.assertIsInstance(results, list)
        self.assertGreater(len(results), 0)
        for result in results:
            self.assertIsNotNone(result)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)

    @patch('src.agent.scrape_data')
    def test_handle_query_no_results(self, mock_scrape_data):
        mock_scrape_data.return_value = None
        query = "asdkjfhaskjdfhaskjdfh"
        results = handle_query(query)
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), 0)

    @patch('src.agent.scrape_data')
    def test_handle_query_failed_request(self, mock_scrape_data):
        mock_scrape_data.return_value = None
        query = "invalid search query that should fail"
        results = handle_query(query)
        self.assertIsInstance(results, list)
        self.assertEqual(len(results), 0)

    @patch('src.agent.handle_query')
    def test_interactive_cli(self, mock_handle_query):
        mock_handle_query.return_value = [
            "Paris is the capital of France.",
            "The Eiffel Tower is a famous landmark in Paris."
        ]
        user_input = (
            "What is the capital of France? Also, tell me about the Eiffel Tower.\n"
            "exit\n"
        )
        expected_output = (
            "Welcome to the Auto Search Agent CLI!\n"
            "Type 'exit' to quit the CLI.\n"
            "Type 'help' for instructions on how to use the CLI.\n"
            "Enter your query: Results: ['Paris is the capital of France.', "
            "'The Eiffel Tower is a famous landmark in Paris.']\n"
            "Enter your query: Exiting the CLI. Goodbye!\n"
        )

        with patch('sys.stdin', StringIO(user_input)), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            interactive_cli()
            self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
