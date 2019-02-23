from sys import argv
script, nFile = argv

file = open(nFile)
print(f"Aperto il file {nFile}")
print("contenuto:")
print(file.read())
print('-' * 64)

print(f"Stiamo per cancellare il fie {nFile}")
print("se non vuoi che ciò succeda premi CTRL+C, atrimenti premi INVIO:")
input("> ")
file.close()

file = open(nFile, 'w')
print("Cancellazione file ...")
file.truncate()
print('-' * 64)

print("Ora puoi scrivere quello che vuoi (per usire scrivi 'exit' in una nuova linea):\n")

while True:
    row = input('> ')
    if (row == "exit"):
        break
    file.write(row + '\n')

file.close()