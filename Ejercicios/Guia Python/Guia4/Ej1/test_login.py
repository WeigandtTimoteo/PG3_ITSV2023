from login import validate_password
import pytest

class test_validate_password():
    def SetUp(self):
        self.validate_password = validate_password()
    
    def test_validate_password():
        validate_password = validate_password()
        assert validate_password("Pato1234") == True