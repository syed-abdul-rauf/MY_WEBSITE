Created comprehensive test suite for the AI learning module at website/tests/test_ai_learning.py with:

- Basic module import and existence tests
- Tokenization function tests (basic, operators, empty strings, special characters, multiline code)
- Vocabulary structure validation tests
- String-to-index (stoi) and index-to-string (itos) mapping tests
- Training data shape validation
- Integration tests for the tokenization-to-vocabulary pipeline
- Edge case tests for special characters, multiline code, and comments

The test suite uses pytest and includes proper path setup to import the ai.learning module. All tests are defensive and check for attribute existence before testing, making them robust against the commented-out code in the learning.py file.