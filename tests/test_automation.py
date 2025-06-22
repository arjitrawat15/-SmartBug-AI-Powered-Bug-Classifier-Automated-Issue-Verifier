def test_ui_script_runs():
    from automation.ui_bug_test import run_ui_bug_test
    assert run_ui_bug_test() == "UI Bug test passed"