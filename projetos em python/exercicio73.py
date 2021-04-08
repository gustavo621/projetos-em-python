times = ("são paulo", "internacional", "paumeiras", "flamengo", "gremio",
         "atlético mineiro", "cruzeiro", "corintians", "santos", "america mineiro",
         "fluminence", "atlético paranaence", "vitória", "bahia", "bota-fogo",
         "chapecoense", "ceará", "vasco da gama", "sport", "paraná")
print("-="*15)
print(f"lista de times do brasileirão: {times}")
print("-="*15)
print(f"os 5 primeiros times são: {times[0:5]}")
print("-="*15)
print(f"os 4 ultimos times são {times[-4:]}")
print("-="*15)
print(f"os times em ordem alphabetica: {sorted(times)}")
print("-="*15)
print(f'a chapecoence está na {times.index("chapecoense")+1} posiçãoª')
print("-="*15)