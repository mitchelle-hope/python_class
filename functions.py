def greet(name,age):
 year=2022-age
 return f"Hello {name} you were born in {year}"

 

def my_country(name, country="Kenya" ):
    return f"hello {name}from {country}" 
 
def hello(name):
     return f"hello {name}"

def hello_multi(*names):
    print(names)

def greet_multi (**kwargs):
    keys=kwargs.keys()
    if"name" in keys:
        print("Hello{kwargs}['name']}")
    elif "country"in keys:  
        print("hello from{kwargs['country' ")
    else:
               print("hello anonymous")
def  sum_and_greet(*args,**kwargs): 
     print(args)
     print(kwargs)

     
     def details_multi (*args,**kwargs):
        multiply=1
        for num in args:
            multiply*=num
            print(multiply)
     print(f"Hello{kwargs}")

 