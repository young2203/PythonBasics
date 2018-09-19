class LogicGate:
    def __init__(self, label):
        self.label = label
        #self.gatetype = gatetype
        self.output = None

    def getLabel(self, label):
        return self.label

    def getOutput(self):
        #self.output=runGateLogic()
        return self.output


class BinaryGate(LogicGate):
    def __init__(self, label):
        super().__init__(label)
        self.pinA = None
        self.pinB = None

    def getPinA(self):
        pass

    def getPinB(self):
        pass


class UnaryGate(LogicGate):
    def __init__(self, label):
        super().__init__(label)
        self.pinA = None

    def getPinA(self):
        pass


class AndGate(BinaryGate):
    def __init__(self,label):
        super().__init__(label)

myGate = BinaryGate('g1')
print(myGate.label)
print(myGate.pinA)
print(myGate.pinB)
print(myGate.getOutput())
