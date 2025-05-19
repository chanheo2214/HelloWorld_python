import unittest
from unittest.mock import patch
from helloworld import main

class TestMainFunction(unittest.TestCase):
    @patch("builtins.print")
    def test_main_output(self, mock_print):
        main()
        mock_print.assert_called_once_with("Hello, World!")

if __name__ == "__main__":
    unittest.main()
