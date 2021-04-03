import re

pattern = r'([a-e]*)[a-z]' # o padrão corresponde à string “000”
test_string = 'ez' # a string de teste é “000”

result = re.fullmatch(pattern, test_string)
if result is not None:
    print("String '%s' : aceita"%test_string)
else:
    print("String '%s': rejeitada"%test_string)