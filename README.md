Automated UI Testing for cockpit-ovirt using Selenium

Steps to run tests:

1. Install geckodriver
2. Install py.tests
3. Ensure that geckodriver is installed in the correct path
   i.e. The path under which geckodriver is present should be available in $PATH
4. Run the command 'py.test test_suite.py' to run the whole test suite
5. To run a single test 'py.test test_suite.py::test_test_name'
   For e.g. if you wish to run, test_gluster_deployment_fail_check
   Then run the command 'py.test test_suite.py::test_gluster_deployment_fail_check'


Enhancements needed:

1. Proper logging
2. Multiple test cases need to be added
3. Behavioral UI tests
4. Better code flow, defining methods and adding decorators where needed
