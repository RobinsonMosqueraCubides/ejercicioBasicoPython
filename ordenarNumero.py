import random 
nmr = list(range(1, 11))
random.shuffle(nmr)

ascendente = sorted(nmr)
descendente = sorted(nmr, reverse=True)

print(f"Lista Original:\n{nmr} \n \n Lista descendente:\n{descendente} \n \n Lista Ascendente:\n {ascendente}")
