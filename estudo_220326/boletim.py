nome = str(input("Digite o nome do aluno\n"))
notas = []
notas.append(float(input("Digite a primeira nota\n")))
notas.append(float(input("Digite a segunda nota\n")))
notas.append(float(input("Digite a terceira nota\n")))

Aluno = {
    "nome": nome,
    "notas": notas,
}
nome = Aluno["nome"]
notas = Aluno["notas"]
media = sum(notas) / len(notas)
print(f"Nome: {nome} | Notas: {notas} | Média: {media}")