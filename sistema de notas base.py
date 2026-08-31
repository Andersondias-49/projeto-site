colegio = []
while True:
    print('1 - Cadastrar aluno\n'
          '2 - Listar alunos\n'
          '3 - Calcular média\n'
          '4 - Mostrar quem foi aprovado/reprovado\n'
          '5 - Sair')
    try:
        opcao = int(input('Qual sua escolha? '))
    except ValueError:
        print('ERRO! Por favor digite um NÚMERO de 1 a 5.')
    if opcao == 1:
        nome = str(input('Qual nome do aluno? '))
        notas = list(map(float, input('digite as 3 notas separadas por vírgula: ').split(',')))
        colegio.append({'nome': nome,
                        'notas': notas})
    elif opcao == 2:
        print('NOME     NOTAS')
        for a in colegio:
            print(a['nome'],    a['notas'])
    elif opcao == 3:
        for a in colegio:
            media = sum(a['notas']) / len(a['notas'])
            print(f"{a['nome']}    {media:.2f}")
    elif opcao == 4:
        for n in colegio:
            medi = sum(n['notas']) / len(n['notas'])
            if medi >= 5:
                print(f"{n['nome']}  APROVADO")
            else:
                print(f"{n['nome']}   REPROVADO ")
    elif opcao == 5:
        break
    else:
        print('ERRO! Por favor digite um NÚMERO de 1 a 5')
print('Programa encerrado!')
