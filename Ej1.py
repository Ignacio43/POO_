class Email:
    def __init__(self,idCuenta,dominio,TipoDominio,contrasena):
        self.__idCuenta=idCuenta
        self.__dominio=dominio
        self.__TipoDominio=TipoDominio
        self.__contrasena=contrasena
        
    def retornaEmail(self):
       return self.__idCuenta + "@" + self.__dominio + "." + self.__TipoDominio
        
    def getDominio(self):
        return self.__dominio
   
    def CrearCuenta(self,direccion):
        partes=direccion.split("@")
        self.__idCuenta=partes[0]
        partes=partes[1].split(".")
        self.__dominio=partes[0]
        self.__TipoDominio=partes[1]
        self.__contrasena=input("ingrese la contraseña de la cuenta ")
    
    def ModContra(self):
        actual=input("ingrese la contraseña actual")
        if actual==self.__contrasena:
            nueva=input("ingresar la nueva contraseña")
            self.__contrasena=nueva
            print("la contraseña de cambio correctamente")
        else:
            print("la contraseña ingresada era incorrecta")
        print(f"{self.__contrasena}")
            
def CuentaArchi(archivo):
    validas=[]
    with open(archivo,"r")as archivo:
        for linea in archivo:
            direccion=linea.strip()
            if '@' in direccion and '.' in direccion:
                cuenta=Email("","","","")
                cuenta.CrearCuenta(direccion)
                validas.append(cuenta)
            else:
                print(f"la direccion {direccion} es invalida ")
    return validas 


if __name__=='__main__': 
    #Ejercicio 1
    nombre=input("ingrese su nombre ")
    direccion=input("ingrese su direccion de correo electronico ")
    cuenta=Email("","","","")
    cuenta.CrearCuenta(direccion)
    print (f"El correo electroico {nombre} corresponde a la cuenta {cuenta.retornaEmail()} . ")
    #Ejercicio 2
    cuenta.ModContra()
    #Ejercicio 3
    direc=input("ingrese su direccion de correo para crear un objeto")
    email=Email("","","","")
    email.CrearCuenta(direc)
    print(f"el correo creado a partir de la direccion es {email.retornaEmail()}")
    #Ejercicio 4
    archivo="archi1poo.txt" 
    cuentas_validas=CuentaArchi(archivo)
    print(f"el numero de cuentas validas es de {len(cuentas_validas)} y las cuentas validas son: \n")
    for cuenta in cuentas_validas:
        print(cuenta.retornaEmail())
        
        
        
        
        