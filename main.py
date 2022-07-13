# import rsa
#
# pubkey, privkey = rsa.newkeys(5120)
#
# str1 = "FGFGF2@HFGDHGH2H5H*/T*H-G9HGG6+G6HFG5H65DGH45+9FS$%&gJ/"
#
# enctex = rsa.encrypt(str1.encode(), pubkey)
#
# dectex = rsa.decrypt(enctex, privkey).decode()
# print("TEXTO SIN ENCRIPTAR: ", str1)
# print("MENSAJE ENCRIPTADO: ", enctex)
# print("MENSAJE DESENCRIPTADO: ", dectex)


# from simplecrypt import encrypt, decrypt
# passkey = 'wow'
# str1 = 'I am okay'
# cipher = encrypt(passkey, str1)
# print(cipher)

# --------------------------------POSIBLE SOLUCION A ENCRIPTADOS-----------------------------------------
import cryptocode

str_encoded = cryptocode.encrypt("EL DESENCRIPTADO ES:  tcp:qa-centrolaboral-db.6ff6bdb9798a.database.windows.net,1433;DATABASE=CONTROL_DE_ASISTENCIA;UID=dtictiusr;PWD=P'T.j$4hdFU5X}u%m.gU","ENCRIPTADO")

## And then to decode it:
str_decoded = cryptocode.decrypt(str_encoded, "ENCRIPTADO")
print("\n")
print("ESTE ES EL DESENCRIPTADO: ",str_decoded)
print("\n")

print("ESTE ES EL ENCRIPTADO",str_encoded)

file = open("prueba.txt", "w")
file.write("\n")
print("ESTE ES EL ENCRIPTADO")
print("\n")
file.write(str_encoded)
file.write("\n")
print("ESTE ES EL DESENCRIPTADO")
file.write(str_decoded)

#  https://www.delftstack.com/es/howto/python/python-encrypt-string/
# ---------------------------------------------------------------------------------------------------------------