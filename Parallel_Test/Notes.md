pytest -n 2                 Individual test methods
pytest -n auto              Same as -n, but uses all CPU cores

Tests/test_search.py::TestSearch::test_search_mobile 
Tests/test_login.py::TestLogin::test_valid_login 
[gw1] PASSED Tests/test_search.py::TestSearch::test_search_mobile 
[gw0] PASSED Tests/test_login.py::TestLogin::test_valid_login 

Tests/test_search.py::TestSearch::test_search_laptop 
Tests/test_login.py::TestLogin::test_invalid_login 
[gw1] PASSED Tests/test_search.py::TestSearch::test_search_laptop 
[gw0] PASSED Tests/test_login.py::TestLogin::test_invalid_login 
---------------------------------------------------------------------------
pytest -n 2 --dist=loadscope        All methods in the same class/module

Tests/test_login.py::TestLogin
[gw0] PASSED Tests/test_login.py::TestLogin::test_valid_login 
[gw0] PASSED Tests/test_login.py::TestLogin::test_invalid_login

Tests/test_search.py::TestSearch:
[gw1] PASSED Tests/test_search.py::TestSearch::test_search_mobile 
[gw1] PASSED Tests/test_search.py::TestSearch::test_search_laptop 
---------------------------------------------------------------------------
pytest -n 2 --dist=loadfile                     Entire test file

Tests/test_login.py::TestLogin
[gw0] PASSED Tests/test_login.py::TestLogin

Tests/test_search.py::TestSearch:
[gw1] PASSED Tests/test_search.py::TestSearch