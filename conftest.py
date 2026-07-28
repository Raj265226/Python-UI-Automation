import pytest
import pytest_html
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    report = outcome.get_result()

    if item.name == "test_screenshot_on_failure_report":
        if report.when == "call" and report.failed:
            driver = item.funcargs["driver"]
            if driver:
                screenshot = f"Screenshots_capture_test/{item.name}.png"
                driver.save_screenshot(screenshot)
                extras = getattr(report, "extras", [])
                extras.append(pytest_html.extras.image(screenshot))
                report.extras = extras