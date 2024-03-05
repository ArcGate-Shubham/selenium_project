import pytest

@pytest.mark.usefixtures("setup")
class Test_login1:    
    def test_1sttest(self):
        print("this is my first test")
           
    def test_3rdtest(self):
        print("this is my third test")
        
        
@pytest.mark.usefixtures("setup")
class Test_login2:    
    def test_1sttest(self):
        print("this is my second test")
           
    def test_3rdtest(self):
        print("this is my fourth test")