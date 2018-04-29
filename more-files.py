from sys import argv
from os.path import exists

script ,from_filename , output_filename = argv

print(f"Copying content from {from_filename} to {output_filename}")

in_file = open(from_filename)
in_data_file = in_file.read()

print(f"The input file is {len(in_data_file)} bytes long")

print(f"Does the output file exist? {exists(output_filename)}")
print(f"If it exists press RETURN if not press CRTL-C to abort situation")
input()

out_file = open(output_filename,"w+")
out_file.write(in_data_file)

print("Alright all done baby.")

out_file.close()
in_file.close()

 