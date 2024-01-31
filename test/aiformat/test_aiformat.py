import unittest
from unittest.mock import patch
from io import StringIO
import os
import shutil
import yaml
from jinja2 import Template
from click.testing import CliRunner

from aiformat import main, is_source_code_file, is_document_file

class TestMain(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner()

    def tearDown(self):
        pass

    def test_main(self):
        # Create a temporary directory for testing
        temp_dir = 'temp_dir'
        os.makedirs(temp_dir)

        # Create a temporary file for testing
        temp_file = os.path.join(temp_dir, 'temp_file.txt')
        with open(temp_file, 'w') as file:
            file.write('This is a test file.')

        # Mock the click.get_current_context().params
        params = {
            'file_or_text': temp_file,
            'diff': True,
            'inplace': False,
            'recursive': False,
            'verbose': True,
            'command': 'chat',
            'model': 'gpt-3.5-turbo',
            'temperature': 0
        }
        with patch('click.get_current_context') as mock_get_current_context:
            mock_get_current_context.return_value.params = params

            # Mock the yaml.safe_load
            yaml_data = {
                'aiformat_commands': {
                    'chat': 'This is a chat command.'
                }
            }
            with patch('yaml.safe_load') as mock_safe_load:
                mock_safe_load.return_value = yaml_data

                # Mock the Template.render
                with patch.object(Template, 'render') as mock_render:
                    mock_render.return_value = 'This is a prompt.'

                    # Mock the chatgpt_util.LlmModel.execute
                    with patch('your_module.chatgpt_util.LlmModel.execute') as mock_execute:
                        mock_execute.return_value = 'This is an output.'

                        # Run the main function
                        result = self.runner.invoke(main)

                        # Assert the output
                        self.assertEqual(result.exit_code, 0)
                        self.assertIn('This is a prompt.', result.output)
                        self.assertIn('This is an output.', result.output)

        # Remove the temporary directory
        shutil.rmtree(temp_dir)

    def test_is_source_code_file(self):
        self.assertTrue(is_source_code_file('test.cpp'))
        self.assertTrue(is_source_code_file('test.java'))
        self.assertTrue(is_source_code_file('test.py'))
        self.assertTrue(is_source_code_file('test.lua'))
        self.assertTrue(is_source_code_file('test.c'))
        self.assertTrue(is_source_code_file('test.h'))
        self.assertTrue(is_source_code_file('test.js'))
        self.assertTrue(is_source_code_file('test.html'))
        self.assertTrue(is_source_code_file('test.css'))
        self.assertTrue(is_source_code_file('test.php'))
        self.assertTrue(is_source_code_file('test.sql'))
        self.assertTrue(is_source_code_file('test.json'))
        self.assertTrue(is_source_code_file('test.xml'))
        self.assertTrue(is_source_code_file('test.cc'))
        self.assertTrue(is_source_code_file('test.rb'))
        self.assertTrue(is_source_code_file('test.swift'))
        self.assertFalse(is_source_code_file('test.txt'))
        self.assertFalse(is_source_code_file('test.md'))

    def test_is_document_file(self):
        self.assertTrue(is_document_file('test.md'))
        self.assertTrue(is_document_file('test.txt'))
        self.assertTrue(is_document_file('test.log'))
        self.assertTrue(is_document_file('test'))
        self.assertFalse(is_document_file('test.cpp'))
        self.assertFalse(is_document_file('test.java'))
        self.assertFalse(is_document_file('test.py'))
        self.assertFalse(is_document_file('test.lua'))
        self.assertFalse(is_document_file('test.c'))
        self.assertFalse(is_document_file('test.h'))
        self.assertFalse(is_document_file('test.js'))
        self.assertFalse(is_document_file('test.html'))
        self.assertFalse(is_document_file('test.css'))
        self.assertFalse(is_document_file('test.php'))
        self.assertFalse(is_document_file('test.sql'))
        self.assertFalse(is_document_file('test.json'))
        self.assertFalse(is_document_file('test.xml'))
        self.assertFalse(is_document_file('test.cc'))
        self.assertFalse(is_document_file('test.rb'))
        self.assertFalse(is_document_file('test.swift'))

if __name__ == '__main__':
    unittest.main()
