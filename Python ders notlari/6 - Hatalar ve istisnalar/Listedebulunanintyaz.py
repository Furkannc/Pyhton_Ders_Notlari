liste = ["345","sadas","324a","14","kemal"]
liste1=list()
for i in liste:
    try:
 
        liste1.append(int(i))

    except ValueError:
        pass
print(liste1)