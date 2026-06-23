import os 

name= os.getenv('NAME')
age = os.getenv('EDAD')

import os

if age >= 18:
         print(f'Hola "{name}", eres mayor de edad.')
else:
        print(f'Hola "{name}", eres menor de edad.')
