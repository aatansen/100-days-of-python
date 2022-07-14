Here we manually created a file named `another_module.py`:
```
another_variable=12
```
Now we are importing that manually created `another_module.py` in `main.py` and print `another_variable` value:
```
import another_module
print(another_module.another_variable)
```

Now Let's do this with `Turtle Module`, Here `Turtle()` is a `Class` and `timmy` is a `Object`:
```
from turtle import Turtle
timmy=Turtle()
print(timmy)
```
We can create as much object we need from that same class , for example:
```
from turtle import Turtle

timmy=Turtle()
timmy2=Turtle()
timmy3=Turtle()
```
Now let's access the `attribute`, Here we import `Screen` from `turtle module` and created a Object `my_screen` from `Screen()` Class ,here in `my_screen.canvheight` where `canvheight` is an `attribute`
```
from turtle import Screen
my_screen = Screen()
print(my_screen.canvheight)
```
Now let's access the `method`, Here `exitonclick()` is a `method` which is being accessed by `my_screen` object. `NOTE: Method-->Function`
```
from turtle import Screen
my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
```
Learned:
- How module work
- What is Class,Object
- How to create class , object
- How to access attribute and method by object
- Difference between Method and Class