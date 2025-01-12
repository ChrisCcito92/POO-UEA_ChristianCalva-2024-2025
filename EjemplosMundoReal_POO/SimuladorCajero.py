# Cajero
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular # Nombre del titular de la cuenta
        self.saldo = saldo_inicial # Saldo inicial de la cuenta
        print(f"Bienvenido, {self.titular} a tu cuenta bancaria.") # Mensaje de bienvenida

    def depositar(self, monto):
        # Metodo para depositar dinero en la cuenta
        if monto > 0:
            self.saldo += monto
            print(f"Depósito exitoso. Nuevo saldo: ${self.saldo:.2f}")
        else:
            print(f"El monto a depositar debe ser mayor que cero.")

    def retirar(self, monto):
        # Metodo para retirar dinero de la cuenta
        if monto > self.saldo:
            print(f"Fondos insuficientes para realizar el retiro.\n")
        elif monto > 0:
            self.saldo -= monto
            print(f"Retiro exitoso. Nuevo saldo: ${self.saldo:.2f}\n")
        else:
            print(f"El monto a retirar debe ser mayor que cero.\n")

    def consultar_saldo(self):
        # Metodo para mostrar el saldo actual
        print(f"Tu saldo actual es: ${self.saldo:.2f}")


# Ingreso de cuenta ahorristas
#Cuenta 1
cuenta = CuentaBancaria("Juan Pérez", 1000) # Crea la cuenta del titular y su saldo inicial
cuenta.consultar_saldo() # Muestra el saldo inicial
cuenta.depositar(500) # Realiza un depósito
cuenta.retirar(1600) # Realiza un retiro

cuenta = CuentaBancaria("Carlos Yepez", 300) # Crea la cuenta del titular y su saldo inicial
cuenta.consultar_saldo() # Muestra el saldo inicial
cuenta.depositar(800) # Realiza un depósito
cuenta.retirar(250) # Realiza un retiro

cuenta = CuentaBancaria("Pepe Cruz", 500) # Crea la cuenta del titular y su saldo inicial
cuenta.consultar_saldo() # Muestra el saldo inicial
cuenta.depositar(15000) # Realiza un depósito
cuenta.retirar(6000) # Realiza un retiro