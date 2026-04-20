# Python Logical Exercises – Answers
x = 5 
y = "5" 
print(x + int(y) * 2)

"""Answer:** 15  
Explanation: int("5") = 5 → 5 * 2 = 10 → 5 + 10 = 15"""

## 2. Variable Mutation Logic
x = 10 
y = x 
x = x + 5 
y = y * 2 
print(x, y)
"""Jawaab: 15 20  
Explanation: y keeps original value (10), then changes separately."""

## 3. Unpacking Challenge
data = ["Python", 3, 8.5] 
a, b, c = data 
print(a * b)
"""Answer: PythonPythonPython  
Explanation: string * 3 repeats the string."""

## 4. Fix the Error
x = 10
y = "20"
print(x + y)
"""Qalad: lama isku dari karo int + string"""
"""Fix 1:
```python
print(x + int(y))
```
Fix 2:
```python
print(str(x) + y)"""

## 5. Global Variable Trap
x = "Hello"
def change():
 x = "World"
change()
print(x)
"""Jawaab: Hello
Sabab: x gudaha function-ka waa local"""
"""Fix:
```python
def change():
    global x
    x = "World"""

## 6. Complex Print
print("Age:", 20 + 5, "Years" + " Old")
"""Jawaab: Age: 25 Years Old
✔️ Kani hore ayuu sax u yahay"""

## 7. Multi Assignment
x = y = z = 10 
x += 5 
y *= 2 
z -= 3 
print(x, y, z)
""" Jawaab: 15 20 7"""

## 8. Case-Sensitive Bug
age = 25 
Age = 30 
print(age + Age)

"""Answer:** 55
Sabab: Python waa case-sensitive (age ≠ Age)"""


## 9. Unpacking Error
fruits = ["apple", "banana"] 
x, y, z = fruits

"""Fix 1:
```python
x, y = fruits
```
Fix 2:
```python
fruits = ["apple", "banana", "orange"]
x, y, z = fruits"""

## 10. Mixed Operations
x = "3" 
y = 2 
z = float(x) * y + int(x)
"""Jawaab: 9.0
3.0 * 2 = 6
6 + 3 = 9.0"""

## 11. Print Without New Line
print("Hello", end="-") 
print("World", end="-") 
print("Python")
"""Answer:** Hello-World-Python"""

## 12. Hidden Casting
x = "10" 
y = "5" 
print(int(x) + int(y) * int(x))
"""Jawaab: 60
5 * 10 = 50
50 + 10 = 60"""

## 13. Reassign & Track
my_var = 10 
myVar = 20 
print(my_var + myVar)
"""Jawaab: 30
Sabab: magacyadu way kala duwan yihiin"""

## 14. Logical Naming
x, y = 5, 10 
x, y = y, x + y 
print(x, y)
"""Jawaab: 30
Sabab: magacyadu way kala duwan yihiin"""


## 15. Advanced Challenge
x, y = 5, 10 
x, y = y, x + y 
print(x, y)
"""Jawaab: 10 15
Sharaxaad:
x → y (10)
y → x + y (5 + 10 = 15)"""
