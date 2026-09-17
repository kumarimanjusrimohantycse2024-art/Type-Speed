import unittest

from Git import build_result_message, calculate_wpm


class TypingSpeedLogicTests(unittest.TestCase):
    def test_calculate_wpm_for_known_input(self):
        self.assertEqual(calculate_wpm("one two three", 30), 6)

    def test_calculate_wpm_handles_non_positive_elapsed_time(self):
        self.assertEqual(calculate_wpm("one two", 0), 0)

    def test_build_result_message_for_empty_input(self):
        self.assertEqual(
            build_result_message("   ", "target sentence", 10),
            "Please type something!",
        )

    def test_build_result_message_for_correct_sentence(self):
        self.assertEqual(
            build_result_message("hello world", "hello world", 60),
            "Correct! Your typing speed is 2 WPM.",
        )

    def test_build_result_message_for_incorrect_sentence(self):
        self.assertEqual(
            build_result_message("hello world", "hello", 60),
            "Incorrect! You typed 2 WPM.",
        )


if __name__ == "__main__":
    unittest.main()
