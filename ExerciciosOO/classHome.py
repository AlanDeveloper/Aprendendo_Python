from classDoor import Door
from classWindow import Window

class Home():
    def __init__(self, color, doorList, windowList):
        self._color = color
        self._doorList = doorList
        self._windowList = windowList
    def __str__(self): return 'Cor: {}, Janelas: {}, Portas: {}'.format(self._color, self.allWindows(), self.allDoors())

    def insertDoor(self, door): self._doorList.append(door)
    def insertWindow(self, window): self._windowList.append(window)
    def removeDoor(self, position): self._doorList.remove(position)
    def removeWindow(self, position): self._windowList.remove(position)

    def setColor(self, color): self._color = color
    def getColor(self): return self._color
    def allWindowList(self): return self._windowList
    def allDoorList(self): return self._doorList

    def viewOpenDoors(self):
        counter = 0
        for i in range(0, self.allDoors()):
            if self._doorList[i].statusDoor() == True : counter += 1
        return counter
    def viewOpenWindows(self):
        counter = 0
        for i in range(0, self.allWindows()):
            if self._windowList[i].statusWindow() == True : counter += 1
        return counter

    def allDoors(self): return len(self._doorList)
    def allWindows(self): return len(self._windowList)

minhaCasa = Home('Vermelho', [], [])
minhaCasa.setColor('Verde')
print(minhaCasa.__str__())

porta1 = Door(False, 'Verde', 10, 5)
janela1 = Window('Azul', False, False, 10, 10)
minhaCasa.insertDoor(porta1)
minhaCasa.insertWindow(janela1)
print(minhaCasa.__str__())

print(minhaCasa.allDoorList()[0].__str__())
print(minhaCasa.allWindowList()[0].__str__())

print('Total de portas: {}, Total de Janelas: {}'.format(minhaCasa.allDoors(), minhaCasa.allWindows()))