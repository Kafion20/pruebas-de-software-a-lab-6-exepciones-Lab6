class MyException(Exception):
    pass

class ExceptionsDemo:
    
    def divide(self, a, b):
        try:
            result = a / b
            print("Division result:", result)
        except ZeroDivisionError:
            print("division entre cero no")
        except TypeError:
            print("error de tipografia noo")
    
    def access_list(self, lst, index):
        try:
            print("Element:", lst[index])
        except IndexError:
            print("index error detectado")
        except TypeError:
            print("type error detactado")
    
    def access_dict(self, dic, key):
        try:
            print("Value:", dic[key])
        except KeyError:
            print("key error detected")
        except TypeError:
            print("type error detected")
    
    def read_file(self, filename):
        try:
            with open(filename, "r") as f:
                content = f.read()
                print(content)
        except FileNotFoundError:
            print("file not found error detected")
        
    
    def access_attribute(self, obj):
        try:
            print(obj.tnonexistent_attribue)
        except AttributeError:
            print("atribute erro found")
    
    def check_positive(self, number):
        try:
            if number < 0:
                raise MyException("The number must be positive.")
            else:
                print("Valid number:", number)
        except MyException:
            print("my Exeption error found")


class MyException(Exception):
    pass

if __name__ == "__main__":

    demo = ExceptionsDemo()

    demo.divide(10, 0)   
    demo.divide("10", 2)  

    demo.access_list([1,2,3], 5)   
    demo.access_list(1, 0)   

    demo.access_dict({"a": 1, "b": 2, "c": 3}, "d")  
    demo.access_dict("not_a_dict", "b")  

    demo.read_file("text_2.txt") 
    demo.read_file("text.txt") 

    demo.access_attribute(object())  

    try:
        demo.check_positive(-5)
    except MyException as e:
        print(" Custom error:", e)
