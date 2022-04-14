# Entrada:[('str1',40),('str2',60),('str3',10),('str4',20),('str5',30),]
# Saida: 160 <- Soma de todos os valores

lista = [('str1',40),('str2',60),('str3',10),('str4',20),('str5',30),]
print(sum([x[1] for x in lista]))