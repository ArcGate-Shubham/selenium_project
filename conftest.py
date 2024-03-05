import pytest
import pytest_html

@pytest.fixture(scope="module")
def setup():
    print("this will run first")
    yield
    print("this will run last")
    
def pytest_html_report_title(report):
    report.title = "My very own title!"
    
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call":
        # always add url to report
        extras.append(pytest_html.extras.url("http://www.example.com/"))
        extras.append(pytest_html.extras.json({'name': 'pytest'}))
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            extras.append(pytest_html.extras.html("<div>Additional HTML</div>"))
            extras.append(pytest_html.extras.text('Add some simple Text'))
        report.extras = extras