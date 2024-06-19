import unittest
from src.main import (
    vishwam_model, parse_query, execute_search,
    process_data, summarize_data, generate_response
)


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
        self.assertIsInstance(search_results, list)
        self.assertGreater(len(search_results), 0)
        for result in search_results:
            self.assertIsInstance(result, str)

    def test_process_data(self):
        search_results = ["  result1  ", "result2\n", "\tresult3"]
        processed_data = process_data(search_results)
        expected_data = ["result1", "result2", "result3"]
        self.assertEqual(processed_data, expected_data)

    def test_summarize_data(self):
        processed_data = ["result1", "result2", "result3", "result4", "result5", "result6"]
        summary = summarize_data(processed_data)
        expected_summary = "result1 result2 result3 result4 result5"
        self.assertEqual(summary, expected_summary)

    def test_generate_response(self):
        summary = "result1 result2 result3 result4 result5"
        response = generate_response(summary)
        expected_response = "Here is the summary of the search results: result1 result2 result3 result4 result5"
        self.assertEqual(response, expected_response)


if __name__ == '__main__':
    unittest.main()
