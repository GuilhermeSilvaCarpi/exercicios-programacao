frase = 'Curso em Vídeo Python'
print(frase[:8:2])
print(frase.upper().count('O'))
print('curso' in frase.lower())

frase_div = frase.split()
print(frase_div[0][0::2])
print(frase.split()[2])

print("""Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Nunc sodales ac ex quis ultricies. Morbi tincidunt sagittis tellus at fermentum.
Suspendisse lacinia vestibulum imperdiet. Donec iaculis luctus euismod.
Morbi vitae orci et nibh placerat dictum id eu velit.
Curabitur eu lorem finibus, mollis sem sed, vehicula augue. Sed ut nulla lacus.
Pellentesque eget arcu eget enim rutrum pretium.""")

