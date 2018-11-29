from Organization import *
import pickle
import random
import numpy as np

class Genetic:
    def __init__(self, org):
        self.org = org
        for i in range(len(self.org.skillDist)):
            random.shuffle(self.org.skillDist[i])
        org.display()
        self.randpnts = []
        self.initPop = []
        self.initPop.append(self._generateInitChrom())
        self.initPop.append(self._generateInitChrom())
        self._evalFitness()

    def _evalFitness(self):
        self.efficiency = []
        for chrom in self.initPop:
            E = 0
            i = 0
            for proj in self.org.skillReq:
                mems = []
                M = 0
                for j in range(sum(proj)):
                    mems.append(chrom[i])
                    i += 1
                for x in range(len(mems) - 1):
                    for y in range(i + 1, len(mems)):
                       M += self.socioMat[mems[x]][mems[y]]
                E += 1 + (M/(sum(proj) ** 2))
            self.efficiency.append(E)


    def _generateInitChrom(self):
        self.randpnts = []
        initChrom = []
        indices = [0 for _ in range(self.org.numSkill)]
        for i in self.org.skillReq:
            for j, ele in enumerate(i):
                temp = []
                for k in range(ele):
                    temp.append(self.org.skillDist[j][indices[j]])
                    indices[j] += 1
                random.shuffle(temp)
                for xx in temp:
                    initChrom.append(xx)
                self.randpnts.append(len(initChrom) - 1)

        return initChrom


    def crossover(self):
        newPop = []
        random.shuffle(self.initPop)
        for i in range(len(self.initPop) - 1):
            newChrom1 = self.initPop[i].copy()
            newChrom2 = self.initPop[i + 1].copy()
            #print(self.randpnts)
            x = np.random.choice(self.randpnts, 2, replace = False)
            #print(x)
            c1, c2 = x
            c1, c2 = (c2, c1) if c2 < c1 else (c1, c2)

            for ind in range(c1, c2 + 1):
                newChrom1[ind], newChrom2[ind] = newChrom2[ind], newChrom1[ind]

            newPop.append(newChrom1.copy())
            newPop.append(newChrom2.copy())
        self.initPop += newPop
        self._evalFitness()

    def mutation(self):
        #------

if __name__ == "__main__":
    with open('filename3.pickle', 'rb') as handle:
        org = pickle.load(handle)
        gen = Genetic(org)
        print(len(gen.initPop))
        gen.crossover()
        for i in gen.efficiency:
            print(i)
