with open('file_demo.txt', 'r') as open_file:
    all_text = open_file.read()
open_file.close()

open_file = open('file_demo.txt', 'w')
open_file.write('A string to write2'+"\n"+all_text)
open_file.close()