dictionary = {"Bairros": ["Pavuna", "Guadalupe", "Anchieta"], 
              "Cidades": ["Seropédica", "Nova iguaçu", "Niterói"]}

lista = [["Pavuna", "Guadalupe", "Anchieta"],["Seropédica", "Nova iguaçu", "Niterói"]]

#print(lista[0])

# ou

#print(dictionary["Bairros"])

# adicionando valores:
dictionary["Bairros"].append("Lagoinha")
# adicionando chaves:
dictionary["Estados"] = ["RJ", "SP", "MG"]
print(dictionary["Estados"])