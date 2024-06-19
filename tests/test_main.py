import unittest
from unittest.mock import patch
from src.main import (
    vishwam_model, parse_query, execute_search,
    process_data, summarize_data, generate_response
)


class TestVishwamModel(unittest.TestCase):

    @patch('src.main.execute_search')
    def test_vishwam_model(self, mock_execute_search):
        query = "Test query"
        mock_execute_search.return_value = ["result1", "result2", "result3"]
        response = vishwam_model(query)
        expected_response = (
            "Here is the summary of the search results: "
            "result1 result2 result3"
        )
        self.assertEqual(response, expected_response)

    def test_parse_query(self):
        query = "Test query"
        parsed_query = parse_query(query)
        expected_query = "Test query"
        self.assertEqual(parsed_query, expected_query)

    @patch('src.main.requests.get')
    def test_execute_search(self, mock_get):
        parsed_query = "Test query"
        mock_response = unittest.mock.Mock()
        mock_response.text = """
        <html>
            <body>
                <div class='BNeawe vvjwJb AP7Wnd'>result1</div>
                <div class='BNeawe vvjwJb AP7Wnd'>result2</div>
                <div class='BNeawe vvjwJb AP7Wnd'>result3</div>
            </body>
        </html>
        """
        mock_get.return_value = mock_response
        search_results = execute_search(parsed_query)
        expected_results = ["result1", "result2", "result3"]
        print(f"Search Results: {search_results}")  # Added logging for debugging
        self.assertEqual(search_results, expected_results)

    def test_process_data(self):
        search_results = ["  result1  ", "result2\n", "\tresult3"]
        processed_data = process_data(search_results)
        expected_data = ["result1", "result2", "result3"]
        self.assertEqual(processed_data, expected_data)

    def test_summarize_data(self):
        processed_data = [
            "result1", "result2", "result3", "result4", "result5", "result6"
        ]
        summary = summarize_data(processed_data)
        expected_summary = "result1 result2 result3 result4 result5"
        self.assertEqual(summary, expected_summary)

    def test_generate_response(self):
        summary = "result1 result2 result3 result4 result5"
        response = generate_response(summary)
        expected_response = (
            "Here is the summary of the search results: "
            "result1 result2 result3 result4 result5"
        )
        self.assertEqual(response, expected_response)


if __name__ == '__main__':
    unittest.main()
