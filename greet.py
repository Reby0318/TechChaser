def greet(lang):
        if lang == 'es':
            return 'Hola'
        elif lang == 'fr':
            return 'Bonjour'
        else:
            return 'Hello'

print(greet('en'), 'Glenn')
#Hello Glenn
print(greet('es'), 'Sally')
#Hola Sally
print(greet('fr'), 'Michael')
#Bonjour Michael
 