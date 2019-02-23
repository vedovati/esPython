from sys import argv
from os.path import exists

script, from_file, to_file = argv

in_file = open(from_file)
data = in_file.read()

print(f"{from_file} contents copied")
print(f"Does the output file exist? {exists(to_file)}")
print("hit RETURN to continue, CTRL+C to abort")
input()

out_file = open(to_file, 'w')
out_file.write(data)

in_file.close()
out_file.close()