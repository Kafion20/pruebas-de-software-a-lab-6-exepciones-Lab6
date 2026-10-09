import pytest
from Exceptions import ExceptionsDemo, MyException  

def test_dvision_cero():
    demo = ExceptionsDemo()
    with pytest.raises(ZeroDivisionError):
        demo.divide(10,0)



def test_division_string():
    demo = ExceptionsDemo()
    with pytest.raises(TypeError):
        demo.divide("3",0) 



def test_access_list():
    demo = ExceptionsDemo()
    with pytest.raises(IndexError):
        demo.access_list([1,3,4],7)



def test_access_dict():
    demo = ExceptionsDemo()
    with pytest.raises(KeyError):
        demo.access_dict({"color": "rojo","forma":"round"},"sabor")  



def test_read_file():
    demo = ExceptionsDemo()
    with pytest.raises(FileNotFoundError):
        demo.read_file("cocacola.txt")

def test_read_files():
    demo = ExceptionsDemo()
    with pytest.raises(IOError):
        demo.read_file("tex.txt")



def test_acces_atribute():
    demo = ExceptionsDemo()
    with pytest.raises(AttributeError):
        demo.access_attribute(object())



def test_check_positive():
    demo = ExceptionsDemo()
    with pytest.raises(MyException):
        demo.check_positive(-3)