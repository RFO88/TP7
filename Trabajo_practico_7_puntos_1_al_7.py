# #Punto 1

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura
    
print("Para calcular el área de su rectángulo, por favor ingrese los siguientes parámetros")
largo= float(input("Largo en cm: "))
ancho= float(input("Ancho en cm: "))
rectangulo1 = Rectangulo(largo, ancho)
print(f"El área del rectángulo es: {rectangulo1.area()}")

# #Punto 2

class Mate:
    def __init__(self, n):
        self.n = 5 
        self.cebadas_restantes = n
        self.estado = "vacío"  

    def cebar(self):
        if self.estado == "lleno":
            raise Exception("¡Cuidado! ¡Te quemaste!")
        else:
            self.estado = "lleno"

    def beber(self):
        if self.estado == "vacío":
            raise Exception("¡El mate está vacío!")
        else:
            self.estado = "vacío"
            if self.cebadas_restantes > 0:
                self.cebadas_restantes -= 1
            else:
                print("Advertencia: el mate está lavado.")

mi_mate = Mate(5)

try:
    mi_mate.cebar("lleno")
    mi_mate.beber(1)
    
except Exception as e:
    print(e)


for _ in range(1):
    try:
        mi_mate.cebar()
        mi_mate.beber()
    except Exception as e:
        print(e)
        
#Punto 3

class Corcho:
    def __init__(self, bodega):
        self.bodega = "Bodega UVA"
        
class Botella:
    def __init__(self, corcho=None):
        self.corcho = corcho
        
class Sacacorchos:
    def __init__(self):
        self.corcho = None  

    def destapar(self, botella):
        if botella.corcho is None:
            raise Exception("La botella ya está destapada.")
        if self.corcho is not None:
            raise Exception("El sacacorchos ya contiene un corcho.")
        
        
        self.corcho = botella.corcho
        botella.corcho = None
        print("Botella destapada correctamente.")

    def limpiar(self):
        if self.corcho is None:
            raise Exception("El sacacorchos no tiene ningún corcho.")
        
     
        self.corcho = None
        print("Sacacorchos limpiado correctamente.")
        
        

corcho = Corcho("Bodega UVA")

botella = Botella(corcho)

sacacorchos = Sacacorchos()

#destapar la botella
try:
    sacacorchos.destapar(botella)
except Exception as e:
    print(e)
    
#limpiar sacacorchos
try:
    sacacorchos.limpiar()
except Exception as e:
    print(e)
#volvemos a intentar destapar
try:
    sacacorchos.destapar(botella)
except Exception as e:
    print(e)
    
#Punto 4

class Restaurante:
    def __init__(self, restaurante_nombre, tipo_comida):
        self.restaurante_nombre = restaurante_nombre
        self.tipo_comida = tipo_comida

    def describir_restaurante(self):
        print(f"Restaurante: {self.restaurante_nombre}")
        print(f"Tipo de comida: {self.tipo_comida}")

    def abrir_restaurante(self):
        print(f" {self.restaurante_nombre} ahora está abierto.")
        
class Heladeria(Restaurante):
    def __init__(self, restaurante_nombre, tipo_comida, sabores):
        super().__init__(restaurante_nombre, tipo_comida)
        self.sabores = sabores

    def mostrar_sabores(self):
        print(f"Sabores disponibles en {self.restaurante_nombre}:")
        for sabor in self.sabores:
            print(f"- {sabor}")

mi_heladeria = Heladeria("Heladería Copo´s", "Heladería", ["Vainilla", "Chocolate", "Fresa", "Menta"])

mi_heladeria.describir_restaurante()

mi_heladeria.abrir_restaurante()

mi_heladeria.mostrar_sabores()

#Punto 4

class Personaje:
    def __init__(self, vida, posicion, velocidad):
        self.vida = vida
        self.posicion = posicion
        self.velocidad = velocidad

    def recibir_ataque(self, cantidad):
        self.vida -= cantidad
        if self.vida <= 0:
            raise Exception("El personaje ha muerto.")
        else:
            print(f"Le queda {self.vida} % de vida restantes.")

    def mover(self, direccion):
        if direccion == "izquierda":
            self.posicion -= self.velocidad
        elif direccion == "derecha":
            self.posicion += self.velocidad
        elif direccion == "arriba":
            self.posicion += self.velocidad
        elif direccion == "abajo":
            self.posicion -= self.velocidad
        print(f"Movimiento a la posición {self.posicion}.")
        
        
class Soldado(Personaje):
    def __init__(self, vida, posicion, velocidad, ataque):
        super().__init__(vida, posicion, velocidad)
        self.ataque = ataque

    def atacar(self, objetivo):
        print(f"El soldado ataca al objetivo en la posición {objetivo.posicion} con {self.ataque} puntos de daño.")
        objetivo.recibir_ataque(self.ataque)
        
class Campesino(Personaje):
    def __init__(self, vida, posicion, velocidad, cosecha):
        super().__init__(vida, posicion, velocidad)
        self.cosecha = cosecha

    def cosechar(self):
        print(f"El campesino ha cosechado {self.cosecha} unidades.")
        return self.cosecha
    
    
soldado = Soldado(100, 0, 10, 20)

campesino = Campesino(100, 10, 0, 150)

# movimiento a la izquierda
soldado.mover("izquierda")

# cosecha de 150 und
campesino.cosechar()

# ataque al campesino con 20 puntos
try:
    soldado.atacar(campesino)
except Exception as e:
    print(e)

# movimiento a la izquierda
campesino.mover("izquierda")

# nuevo ataque
try:
    soldado.atacar(campesino)
except Exception as e:
    print(e)


#Punto 5

class Usuario:
    def __init__(self, nombre, apellido, edad, correo_electronico, celular):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.correo_electronico = correo_electronico
        self.celular = celular

    def describir_usuario(self):
        print(f"Nombre: {self.nombre} {self.apellido}")
        print(f"Edad: {self.edad}")
        print(f"Correo Electrónico: {self.correo_electronico}")
        print(f"N° de celular: {self.celular}")

    def saludar_usuario(self):
        print(f"Hola, {self.nombre} {self.apellido}! Como estas?, te damos una calida bienvenida!!!.")
        
        
# instancias de usuario
usuario1 = Usuario("René", "Ortega", 36, "rene_ortega@gmail.com", 38751234567)
usuario2 = Usuario("Paula", "Arias", 22, "paula_arias@hotmail.com", 3877654321)
usuario3 = Usuario("Carlos", "Pérez", 48, "carlos_perez@outlook.com", 38750005554)

usuarios = [usuario1, usuario2, usuario3]

for usuario in usuarios:
    usuario.describir_usuario()
    usuario.saludar_usuario()
    print()  
    

#Punto 6

class Admin(Usuario):
    def __init__(self, nombre, apellido, edad, correo_electronico, celular, privilegios):
        super().__init__(nombre, apellido, edad, correo_electronico, celular)
        self.privilegios = privilegios

    def mostrar_privilegios(self):
        print(f"Privilegios del administrador {self.nombre} {self.apellido}:")
        for privilegio in self.privilegios:
            print(f"- {privilegio}")

privilegios_admin = [
    "puede postear en el foro",
    "puede borrar un post",
    "puede banear usuario",
    "puede modificar configuraciones",
    "puede añadir usuarios"
]

admin = Admin("Rene", "Ortega", 36, "rene_ortega@gmail.com", 38751234567, privilegios_admin)

admin.describir_usuario()

admin.mostrar_privilegios()  

#Punto 7