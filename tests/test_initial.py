import os

def test_check_environment_variable():
    ns_status = os.getenv('NS_STATUS', "")
    assert ns_status == "Newton School is Awesome"
