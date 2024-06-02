def bacon_com_ovos(n):
    assert isinstance(n, int), 'n deve ser int'
    if n % 3 == 0 and n % 5 == 0:
        return 'Bacon com ovos'
    # Continue com a lógica da função aqui, se houver
