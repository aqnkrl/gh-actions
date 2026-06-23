import os 

name = os.getenv('NAME')
age = int(os.getenv('EDAD', 0)) 

if age >= 18:
    print(f'Hola "{name}", eres mayor de edad.')
else:
    print(f'Hola "{name}", eres menor de edad.')