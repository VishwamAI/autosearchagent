import unittest
from src.main import vishwam_model, parse_query, execute_search, process_data, summarize_data, generate_response

class TestVishwamModel(unittest.TestCase):

    def test_vishwam_model(self):
        query = "Test query"
        response = vishwam_model(query)
        self.assertEqual(response, "Summary of the data")

    def test_parse_query(self):
        query = "Test query"
        parsed_query = parse_query(query)
        self.assertEqual(parsed_query, query)

    def test_execute_search(self):
        parsed_query = "Test query"
        search_results = execute_search(parsed_query)
        self.assertEqual(search_results, ["result1", "result2", "result3"])

    def test_process_data(self):
        search_results = ["result1", "result2", "result3"]
        processed_data = process_data(search_results)
        self.assertEqual(processed_data, search_results)

    def test_summarize_data(self):
        processed_data = ["result1", "result2", "result3"]
        summary = summarize_data(processed_data)
        self.assertEqual(summary, "Summary of the data")

    def test_generate_response(self):
        summary = "Summary of the data"
        response = generate_response(summary)
        self.assertEqual(response, summary)

if __name__ == '__main__':
    unittest.main()
