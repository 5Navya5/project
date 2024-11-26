import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
from main import (greet_me, start_listening, pause_listening, take_command, speak, get_news, weather_forecast, 
                  add_reminder, check_reminders, translate_text, youtube, search_on_google, search_on_wikipedia, 
                  send_email, open_cmd, open_camera, open_notepad, open_calculator, close_cmd, 
                  close_camera, close_notepad, close_calculator, find_ip_address, open_whatsapp, open_instagram, 
                  tell_joke, movie_report, perform_calculation, answer_query, previous_task_result, exit_program)

class TestMain(unittest.TestCase):

    # Existing tests...

    @patch('main.open_cmd')
    def test_open_cmd(self, mock_open_cmd):
        mock_open_cmd.return_value = None
        self.assertIsNone(open_cmd())

    @patch('main.open_camera')
    def test_open_camera(self, mock_open_camera):
        mock_open_camera.return_value = None
        self.assertIsNone(open_camera())

    @patch('main.open_notepad')
    def test_open_notepad(self, mock_open_notepad):
        mock_open_notepad.return_value = None
        self.assertIsNone(open_notepad())

    @patch('main.open_calculator')
    def test_open_calculator(self, mock_open_calculator):
        mock_open_calculator.return_value = None
        self.assertIsNone(open_calculator())

    @patch('main.close_cmd')
    def test_close_cmd(self, mock_close_cmd):
        mock_close_cmd.return_value = None
        self.assertIsNone(close_cmd())

    @patch('main.close_camera')
    def test_close_camera(self, mock_close_camera):
        mock_close_camera.return_value = None
        self.assertIsNone(close_camera())

    @patch('main.close_notepad')
    def test_close_notepad(self, mock_close_notepad):
        mock_close_notepad.return_value = None
        self.assertIsNone(close_notepad())

    @patch('main.close_calculator')
    def test_close_calculator(self, mock_close_calculator):
        mock_close_calculator.return_value = None
        self.assertIsNone(close_calculator())

    @patch('main.find_ip_address')
    def test_find_ip_address(self, mock_find_ip_address):
        mock_find_ip_address.return_value = '192.168.0.1'
        self.assertEqual(find_ip_address(), '192.168.0.1')

    @patch('main.open_whatsapp')
    def test_open_whatsapp(self, mock_open_whatsapp):
        mock_open_whatsapp.return_value = None
        self.assertIsNone(open_whatsapp())

    @patch('main.open_instagram')
    def test_open_instagram(self, mock_open_instagram):
        mock_open_instagram.return_value = None
        self.assertIsNone(open_instagram())

    @patch('main.tell_joke')
    def test_tell_joke(self, mock_tell_joke):
        mock_tell_joke.return_value = 'Why did the scarecrow win an award? Because he was outstanding in his field!'
        self.assertEqual(tell_joke(), 'Why did the scarecrow win an award? Because he was outstanding in his field!')

    @patch('main.movie_report')
    def test_movie_report(self, mock_movie_report):
        mock_movie_report.return_value = 'Inception is a 2010 science fiction action film.'
        self.assertEqual(movie_report(), 'Inception is a 2010 science fiction action film.')

    @patch('main.perform_calculation')
    def test_perform_calculation(self, mock_perform_calculation):
        mock_perform_calculation.return_value = '4'
        self.assertEqual(perform_calculation('2 + 2'), '4')

    @patch('main.answer_query')
    def test_answer_query(self, mock_answer_query):
        mock_answer_query.return_value = 'The Eiffel Tower is a wrought-iron lattice tower on the Champ de Mars in Paris, France.'
        self.assertEqual(answer_query('What is the Eiffel Tower?'), 'The Eiffel Tower is a wrought-iron lattice tower on the Champ de Mars in Paris, France.')

    @patch('main.previous_task_result')
    def test_previous_task_result(self, mock_previous_task_result):
        mock_previous_task_result.return_value = 'The previous task was to perform a calculation: 2 + 2 = 4'
        self.assertEqual(previous_task_result(), 'The previous task was to perform a calculation: 2 + 2 = 4')

    @patch('main.exit_program')
    def test_exit_program(self, mock_exit_program):
        mock_exit_program.return_value = None
        self.assertIsNone(exit_program())

if __name__ == '__main__':
    unittest.main()
