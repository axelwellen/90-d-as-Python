# Separador de emails

# dada una lista de emails, separar los que son de gmail, outlook y otros
# extra, contar cuantos hay de cada tipo

emails = [
        "ana@gmail.com", 
        "pepe@outlook.com",
        "admin@empresa.de", 
        "test@gmail.com"
        ]

emails_separados = {"gmail":[], "outlook":[], "otros":[]}

for mail in emails:
    mail_div = mail.replace("@"," ").replace("."," ").split()
    if "gmail" in mail_div[1]:
        emails_separados["gmail"].append(mail)
    elif "outlook" in mail_div[1]:
        emails_separados["outlook"].append(mail)
    else:
        emails_separados["otros"].append(mail)
print(emails_separados)

# otra opcion sería no desmontar el email sino: 
   
emails_separados_2 = {"gmail":[], "outlook":[], "otros":[]}
#for mail in emails:
#    if mail.endswith("@gmail.com")

for mail in emails:
    if "@gmail." in mail: 
        emails_separados_2["gmail"].append(mail)
    elif "@outlook." in mail:
        emails_separados_2["outlook"].append(mail)
    else:
        emails_separados_2["otros"].append(mail)

print(emails_separados_2)

for clave, lista in emails_separados_2.items():
    print(clave, lista, "-->",len(lista))
