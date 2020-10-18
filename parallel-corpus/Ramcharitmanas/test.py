with open('ramcharitramanas_shloks.txt','r+') as file:
    for line in file:
        if not line.isspace():
            file.write(line)