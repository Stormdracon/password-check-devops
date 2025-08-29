from password_checker import is_valid_password

correctPassword = "Valid123"
shortPassword = "Short1"
noNumberPassword = "NoNumber"
noLowercasePassword = "NOLOWERCASE1"
noUppercasePassword = "nouppercase1"


def test_correct_password():
    assert is_valid_password("Valid123") == True

def test_short_password():
    assert is_valid_password("Short1") == False

def test_no_number_password():
    assert is_valid_password("NoNumber") == False

def test_no_lowercase_password():
    assert is_valid_password("NOLOWERCASE1") == False

def test_no_uppercase_password():
    assert is_valid_password("nouppercase1") == False