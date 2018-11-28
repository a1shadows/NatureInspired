from random import randint
from texttable import Texttable
import pickle
import numpy as np


class Organization:
    def __init__(self, P, S, Pe):
        self.numProj = P
        self.numSkill = S
        self.numPeop = Pe
        self._generateSkillReq()
        self._generateSocioMat()
        self._generateSkillDist()



    def _generateSocioMat(self):
        possibilities = [-1, 0, 1]
        self.socioMat = [[possibilities[randint(0, 2)] for _ in range(self.numPeop)] for _ in range(self.numPeop)]
        print([len(i) for i in self.socioMat], len(self.socioMat))

    def _generateSkillDist(self):
        temp = 1
        self.skillDist = []
        for i in self.skillReq.sum(axis = 0):
            self.skillDist.append(list(range(temp, temp + i - 1)))
            temp = temp + i


    def _generateSkillReq(self):
        lims = self.numPeop
        lis = [randint(1, lims) for _ in range(self.numProj * self.numSkill)]
        while sum(lis) != self.numPeop:
            lims = lims >> 1 if lims > (self.numPeop*2) / (self.numProj + self.numSkill) else lims
            del lis
            lis = [randint(0, lims) for _ in range(self.numProj * self.numSkill)]
            print(lis, sum(lis), lims)
            #dd = input()

        self.skillReq = np.reshape(lis, (self.numProj, self.numSkill))

    def display(self):
        print("Number of People :", self.numPeop)
        print("Number of Skills :", self.numSkill)
        print("Number of Projects :", self.numProj)
        self._printSkillDistTable()
        self._printSkillReqTable()
        #self._printSocioMat()

    def _printSocioMat(self):
        print("Sociometric Matrix")
        t = Texttable()
        t.add_row([""] + ["p" + str(i + 1) for i in range(self.numPeop)])
        for i in range(self.numPeop):
            t.add_row(["p" + str(i + 1)] + self.socioMat[i])
        print(t.draw())

    def _printSkillDistTable(self):
        print("Skill Distribution")
        t = Texttable()
        t.add_row(["s" + str(i + 1) for i in range(self.numSkill)])
        t.add_row([i for i in self.skillDist])
        print(t.draw())

    def _printSkillReqTable(self):
        print("Requirements")
        t = Texttable()
        t.add_row([""] + ["s" + str(i + 1) for i in range(self.numSkill)])
        for i in range(self.numProj):
            t.add_row(["p" + str(i + 1)] + list(self.skillReq[i]))
        print(t.draw())


if __name__ == "__main__":
    org = Organization(2, 10, 25)
    org.display()
    x = input()
    with open('filename3.pickle', 'wb') as handle:
        pickle.dump(org, handle)

