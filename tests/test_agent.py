import unittest
from src.agent import parse_query, break_down_query, scrape_data, summarize_text, handle_query

class TestAgent(unittest.TestCase):

    def test_parse_query(self):
        query = "What is the capital of France? Also, tell me about the Eiffel Tower."
        expected_tokens = ['what', 'is', 'the', 'capital', 'of', 'france', 'also', 'tell', 'me', 'about', 'the', 'eiffel', 'tower']
        self.assertEqual(parse_query(query), expected_tokens)

    def test_break_down_query(self):
        query = "What is the capital of France? Also, tell me about the Eiffel Tower."
        expected_sub_queries = ['What is the capital of France', 'Also, tell me about the Eiffel Tower']
        self.assertEqual(break_down_query(query), expected_sub_queries)

    def test_scrape_data(self):
        url = "https://en.wikipedia.org/wiki/Eiffel_Tower"
        scraped_data = scrape_data(url)
        self.assertIsNotNone(scraped_data)
        self.assertIn("Eiffel Tower", scraped_data)

    def test_summarize_text(self):
        text = ("The Eiffel Tower is a wrought-iron lattice tower on the Champ de Mars in Paris, France. "
                "It is named after the engineer Gustave Eiffel, whose company designed and built the tower. "
                "Locally nicknamed 'La dame de fer' (French for 'Iron Lady'), it was constructed from 1887 to 1889 "
                "as the centerpiece of the 1889 World's Fair.")
        summary = summarize_text(text)
        self.assertIsNotNone(summary)
        self.assertIn("Eiffel Tower", summary)

    def test_handle_query(self):
        query = "What is the capital of France? Also, tell me about the Eiffel Tower."
        results = handle_query(query)
        self.assertIsInstance(results, list)
        self.assertGreater(len(results), 0)
        for result in results:
            self.assertIsNotNone(result)
            self.assertIsInstance(result, str)
            self.assertGreater(len(result), 0)

if __name__ == "__main__":
    unittest.main()
