import unittest
from HtmlTestRunner import HTMLTestRunner
import os

def discover_tests():
    # Load all test cases from the 'tests' directory
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Discover all test modules in the 'tests' directory
    for test_module in loader.discover('tests', pattern='*.py'):
        suite.addTests(test_module)
    
    return suite

if __name__ == "__main__":
    # Define the output directory and file name for the report
    output_dir = 'reports'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    report_file = os.path.join(output_dir, 'test_report.html')
    
    # Create the test suite
    suite = discover_tests()
    
    # Run the tests and generate the report
    with open(report_file, 'wb') as report:
        runner = HTMLTestRunner(output=output_dir, report_title='Selenium Test Report', descriptions='Test Report for Selenium Tests')
        runner.run(suite)
