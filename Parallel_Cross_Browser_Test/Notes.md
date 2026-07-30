If we use browser params - @pytest.fixture(params=["edge", "chrome", "firefox"], scope="function")

-------------------------Run without restriction-------------------------

Run =>
                pytest -n 3

                possible distribution
    Worker gw0:
test_valid_login[edge]
test_blank_login[chrome]
test_select_one_checkbox[firefox]
test_unselect_checkbox[edge]
test_verify_checkbox_result[chrome]
test_invalid_login[firefox]
test_select_multiple_checkbox[edge]

    Worker gw1:
test_valid_login[chrome]
test_invalid_login[edge]
test_select_one_checkbox[chrome]
test_blank_login[firefox]
test_verify_checkbox_result[edge]
test_select_multiple_checkbox[firefox]
test_unselect_checkbox[chrome]

    Worker gw2:
test_valid_login[firefox]
test_invalid_login[chrome]
test_blank_login[edge]
test_select_one_checkbox[edge]
test_unselect_checkbox[firefox]
test_verify_checkbox_result[firefox]
test_select_multiple_checkbox[chrome]

                How its distributed?
Tests are distributed freely.
Same class tests may go to different workers.
Same file tests may go to different workers.
Fastest worker gets next available test.

-------------------------Run class-wise-------------------------

Run =>
                pytest -n 3 --dist=loadscope

    Worker gw0:
TestLogin                    # class name
    test_valid_login[edge]
    test_valid_login[chrome]
    test_valid_login[firefox]

    test_invalid_login[edge]
    test_invalid_login[chrome]
    test_invalid_login[firefox]

    test_blank_login[edge]
    test_blank_login[chrome]
    test_blank_login[firefox]


    Worker gw1:
TestCheckbox                 # class name
    test_select_one_checkbox[edge]
    test_select_one_checkbox[chrome]
    test_select_one_checkbox[firefox]

    test_select_multiple_checkbox[edge]
    test_select_multiple_checkbox[chrome]
    test_select_multiple_checkbox[firefox]

    test_unselect_checkbox[edge]
    test_unselect_checkbox[chrome]
    test_unselect_checkbox[firefox]

    test_verify_checkbox_result[edge]
    test_verify_checkbox_result[chrome]
    test_verify_checkbox_result[firefox]

                How its distributed?
You want all methods of one class to execute together.
You use class-level setup.
You want to avoid splitting class tests across workers.

-------------------------Run file-wise-------------------------

Run =>
                pytest -n 3 --dist=loadfile


    Worker gw0:
Testing/Login/test_login.py
    test_valid_login[edge]
    test_valid_login[chrome]
    test_valid_login[firefox]

    test_invalid_login[edge]
    test_invalid_login[chrome]
    test_invalid_login[firefox]

    test_blank_login[edge]
    test_blank_login[chrome]
    test_blank_login[firefox]

    Worker gw1:
Testing/Checkbox/test_checkbox.py
    test_select_one_checkbox[edge]
    test_select_one_checkbox[chrome]
    test_select_one_checkbox[firefox]

    test_select_multiple_checkbox[edge]
    test_select_multiple_checkbox[chrome]
    test_select_multiple_checkbox[firefox]

    test_unselect_checkbox[edge]
    test_unselect_checkbox[chrome]
    test_unselect_checkbox[firefox]

    test_verify_checkbox_result[edge]
    test_verify_checkbox_result[chrome]
    test_verify_checkbox_result[firefox]


                How its distributed?
You want all tests from one file to stay in the same worker.


=====================================================================

If we use browser like this - @pytest.fixture(scope="function")

-------------------------Run without restriction-------------------------

Run =>
                pytest -n 3

                possible distribution
    Worker gw0:
test_valid_login
test_select_multiple_checkbox

    Worker gw1:
test_invalid_login
test_unselect_checkbox

    Worker gw2:
test_blank_login
test_select_one_checkbox
test_verify_checkbox_result


-------------------------Run class-wise-------------------------

Run =>
                pytest -n 3 --dist=loadscope

    Worker gw0:
TestLogin                    # class name
    test_valid_login
    test_invalid_login
    test_blank_login

    Worker gw1:
TestCheckbox                 # class name
    test_select_one_checkbox
    test_select_multiple_checkbox
    test_unselect_checkbox
    test_verify_checkbox_result

-------------------------Run file-wise-------------------------

Run =>
                pytest -n 3 --dist=loadfile


    Worker gw0:
Testing/Login/test_login.py
    test_valid_login
    test_invalid_login
    test_blank_login

    Worker gw1:
Testing/Checkbox/test_checkbox.py
    test_select_one_checkbox
    test_select_multiple_checkbox
    test_unselect_checkbox
    test_verify_checkbox_result