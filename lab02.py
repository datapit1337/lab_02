import math

#variables
name = "Nick Pollock"
age = 35
height = 5.75
favorite_color = "purple"

#one variable at a time
print(name)
print(age)
print(height)
print(favorite_color)

#print as one statement with commas
print(name, age, height, favorite_color)

#format specifieres
print(f"Hello: my name is {name} my favorite color is {favorite_color} and my age is {age} years old and my height is {height} feet")
print(f"Age as integer: {age:d}")
print(f"Height default float: {height:f}")
print(f"Height with 2 decimals: {height:.2f}")
print(f"Height padded width with 2 decimals: {height:6.2f}")
print(f"Age with zero-padded width: {age:05d}")
print("Mix with format(): name={0:s}, age={1:d}, height={2:.1f}".format(name, age, height))
print(f"""
 Name: {name}
 Age: {age}
 Height: {height}
 favorite_color: {favorite_color}
""")

#Area of a  circle with a radius of 5
r_circle = 5
circle_area = math.pi * r_circle ** 2
print(f"Area of circle with 2 decimals: {circle_area:.2f}")

#square root of age
print(f"""
 age square root= {math.sqrt(age)}
""")

#sine and cosine
print(f"""
   sine= {math.sin(height)}
   cosine= {math.cos(height)}
""")

#expression operators
print(f"""
      age plus 5= {age+5}
      difference between height and 4= {height-4}
      product of age and height= {age+height}
      Quotient of height and 2= {height/2}
      The remainder of age/3= {age/3}
      Age raised to the power of 2= {age**2}
""")

#tempurature conversion
print("Welcome to the temperature converter please enter current temperature in fahrenheit!")
input_temperature = float(input("Please enter your current temperature in fahrenheit: "))
celsius = (input_temperature - 32) * 5 / 9
print(f"{celsius:.2f} °C")