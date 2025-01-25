class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        # Constructor: inicializa la cuenta con el titular y el saldo inicial
        self.titular = titular
        self.saldo = saldo_inicial
        print(f"Cuenta creada para {self.titular} con un saldo inicial de ${self.saldo:.2f}.")

    def depositar(self, monto):
        # Permite depositar dinero en la cuenta
        self.saldo += monto
        print(f"Se depositaron ${monto:.2f}. Saldo actual: ${self.saldo:.2f}.")

    def retirar(self, monto):
        # Permite retirar dinero de la cuenta si hay saldo suficiente
        if monto <= self.saldo:
            self.saldo -= monto
            print(f"Se retiraron ${monto:.2f}. Saldo actual: ${self.saldo:.2f}.")
        else:
            print(f"Saldo insuficiente para retirar ${monto:.2f}. Saldo actual: ${self.saldo:.2f}.")

    def __del__(self):
        # Destructor: notifica el cierre de la cuenta y muestra el saldo final
        print(f"La cuenta de {self.titular} ha sido cerrada. Saldo final: ${self.saldo:.2f}.")


# Ejemplo de uso
cuenta = CuentaBancaria("Juan Pérez", 1000)
cuenta.depositar(500)
cuenta.retirar(300)
del cuenta  # Activa el destructor
