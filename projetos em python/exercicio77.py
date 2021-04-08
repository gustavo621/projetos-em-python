palavras = ("cabo", "daciolo", "jair", "bolsonaro", "galo", "cego", "pesadaum", "michel", "temer", "merda", "pipoca", "fodase")
for p in palavras:
    print(f"\nna palavra {p.upper()} temos ", end="")
    for letra in p:
        if letra.lower() in "aiueo":
            print(letra, end=" ")