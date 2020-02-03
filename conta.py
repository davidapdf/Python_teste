class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo
    @titular.setter
    def titular(self, titular):
        self.__titular = titular
    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    def __pode_sacar(self, valor):
        valor_disponivel = self.saldo + self.limite
        return valor <= valor_disponivel

    def extrato(self):
        print("Saldo {} Titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor
    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("Valor insuficiente {}".format(valor))

    def trasferir(self,valor,conta):
        self.saca(valor)
        conta.deposita(valor)

    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}




