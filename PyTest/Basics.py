import pytest
# part 1 (framework)
# test keyword should either start or end with test
# to test the function type "py.test" in the command prompt or terminal
# to test a particular file "py.test file_name"
# to test a particular function "py.test -k func_name -v"
# part 2 (markers and parallel mode)
# for test cases with marker "py.test -m name"
# to run the test in parallel mode, install pytest-xdist,
# and use "py.test -n number(no. of threads or workers to run)" eg: py.test -n 5
# part 3 (pytest fixtures)
#  pytest -v -s (name)
# py.test (name) -v -s --html=google_test_report.html
