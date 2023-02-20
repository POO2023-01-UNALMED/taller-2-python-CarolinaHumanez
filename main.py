class Asiento:
    def __init__(self,color,precio,registro):
        self.color=color
        self.precio=precio
        self.registro=registro

    def cambiarColor(self,color):
        if (color=="rojo" or color=="verde" or color=="amarillo" or color=="negro" or color=="blanco"):
            self.color=color


class Motor:
    def __init__(self,numeroCilindros, tipo, registro):
        self.numeroCilindros=numeroCilindros
        self.tipo=tipo
        self.registro=registro
    
    def cambiarRegistro(self, new_registro):
        self.registro=new_registro
    
    def asignarTipo(self,new_tipo):
        if(new_tipo=="electrico" or new_tipo=="gasolina"):
            self.tipo=new_tipo

class Auto:
    cantidadCreados=0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo=modelo
        self.precio=precio
        self.asientos=asientos
        self.marca=marca
        self.motor=motor
        self.registro=registro
    
    def cantidadAsientos(self):
        numAsientos=0
        
        for asiento in self.asientos:
            if isinstance(asiento,Asiento):
                numAsientos+=1
        return numAsientos

    def verificarIntegridad(self):
        for i in self.asientos:
            if i != None:
                if i.registro != self.registro:
                    return "La piezas no son originales"
                
        if (self.motor.registro != self.registro):
            return "Las piezas no son originales"
                        
        return "Auto original"

