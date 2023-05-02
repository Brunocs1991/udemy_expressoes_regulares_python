import re

# findall search sub
# compile

string = 'Este é um teste de expressoes teste regulares.'
print(re.search(r'teste', string))
print(re.findall(r'teste2', string))
print(re.sub(r'teste', 'ADCD',  string))

regexp = re.compile(r'teste')
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('DEF', string))
