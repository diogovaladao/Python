from abc import ABC, abstractclassmethod

class Monitor(ABC):
    pass

class MonitorFullHD(Monitor):
    def aumentar_claridade(self, valor):
        print(f'Aumentando claridade em {valor} pontos')

    def reduzir_claridade(self, valor):
        print(f'Reduzindo claridade em {valor} pontos')

monitor = MonitorFullHD()
monitor.aumentar_claridade(5)
monitor.reduzir_claridade(15)
