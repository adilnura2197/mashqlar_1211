#1-misol
ism = input("Ism kirit: ")
print(ism)
print(ism.upper())


#2-misol
matn = "SaLoM"
print(matn)
print(matn.lower())


#3-misol
parol = input("Parolni kiriting: ")
parol_l = parol.lower()

if "admin" in parol_l:
    print("Xavfsiz parol emas")
else:
    print("Parol qabul qilindi:", parol_l)


#4-misol
matn = "  salom dunyo   "
print(matn)
print(matn.rstrip())
print(matn.lstrip())


#5-misol
email = input("Email kirit: ")
print(email)
print(email.strip())


#6-misol
matn = "    salom"
print(matn)
print(matn.lstrip())


#7-misol
matn = "salom    "
print(matn)
print(matn.rsplit())
