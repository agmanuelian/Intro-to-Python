IN_FILE_NAME = "/Users/amanueli/Documents/DevNet/Scripts/DevNet/Exercises/input_text.rtf"  
OUT_FILE_NAME = "/Users/amanueli/Documents/DevNet/Scripts/DevNet/Exercises/output_text.txt"

file_in = open (IN_FILE_NAME, "r")
file_out = open (OUT_FILE_NAME, "w")

lista= ["hola","como", "estas"]
for l in lista:  
	file_out.write(l)

file_in.close()  
file_out.close()
print("Copied " + str (IN_FILE_NAME) + " to " + str(OUT_FILE_NAME) )
