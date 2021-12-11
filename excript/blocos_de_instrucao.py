

a = 10
if(True): # Como a condição do 'if' é verdadeira a variável é criada...
    a = 15
    b = 20
    print(a,b)

print(a,b) # ... Portanto a variável é declarada e pode ser usada.

if (False): # Todavia, se a condição for falsa, a variável não será declarada...
    a = 20
    c = 30
    print(a,b,c)

# print(c) # ... Portanto, haverá um erro.