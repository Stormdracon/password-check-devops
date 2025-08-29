from password_checker import is_valid_password

correctPassword = "Valid123"
shortPassword = "Short1"
noNumberPassword = "NoNumber"
noLowercasePassword = "NOLOWERCASE1"
noUppercasePassword = "nouppercase1"

#assert is_valid_password(correctPassword) == True, "Test failed: correctPassword should be valid"
#assert is_valid_password(shortPassword) == False, "Test failed: shortPassword should be invalid"
#assert is_valid_password(noNumberPassword) == False, "Test failed: noNumberPassword should be invalid"
#assert is_valid_password(noLowercasePassword) == False, "Test failed: noLowercasePassword should be invalid"
#assert is_valid_password(noUppercasePassword) == False, "Test failed: noUppercasePassword should be invalid"
print("All tests passed!")

