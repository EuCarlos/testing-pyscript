def shouldDisplayNameInUppercase(name):
    return name.upper()

names = [
    'Carlos',
    'Marcelo',
    'Roger',
    'Claudio'
]

for name in names:
    print("<li>{}</li>".format(shouldDisplayNameInUppercase(name)))