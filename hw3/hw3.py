class Naive_Bayes_Classifier:
    def __init__(self, training_file_name, testing_file_name):
        self.training_file_name = training_file_name
        self.testing_file_name = testing_file_name
        self.DB = []
        self.testDB = []
        self.PCi = [0, 0, 0, 0] # ['Basic', 'Normal', 'Silver', 'Gold']
    
    def Readfile(self, f_name):
        tmp_DB = []
        file = open(f_name, 'r')
        for i in file.readlines():
            line = []
            for j in i[1:len(i)-2].split(','): # j = '1 1' or '3 39'
                int_j = []
                int_j.append(int(j.split(" ")[0]))
                int_j.append(j.split(" ")[1])
                line.append(int_j) # int_j = [1, '1'] or [2, 'Silver']
            tmp_DB.append(line) # line = [1, '1'], [3, '39'], [4, '100000']
        #print(self.DB[0])
        file.closed
        return tmp_DB

    def Print_DB(self, DB):
        for i in DB:
            print(i)



    def Generate_PCi(self):
        for i in self.DB: # i = [[1, '1'], [3, '39'], [4, '100000']]
            notice = 0
            for j in i: # j = [1, '1']
                if j == [2, 'Basic']:
                    self.PCi[0] = self.PCi[0] + 1
                    notice = 1
                elif j == [2, 'Normal']:
                    self.PCi[1] = self.PCi[1] + 1
                    notice = 1
                elif j == [2, 'Silver']:
                    self.PCi[2] = self.PCi[2] + 1
                    notice = 1
                elif j == [2, 'Gold']:
                    self.PCi[3] = self.PCi[3] + 1
                    notice = 1
            if notice == 0:
                self.PCi[0] = self.PCi[0] + 1
        print(self.PCi)


    def Predict(self):
        for i in self.testDB:
            initial = self.PCi.copy()
            all = 0
            for j in initial:
                all = all + j
            for j in range(len(initial)):
                initial[j] = initial[j] / all
            print(initial)


    def DB_Augmentation(self, DB):
        new_DB = []
        for i in DB:
            


    def Train(self):
        self.DB = self.Readfile(self.training_file_name)
        self.DB = self.DB_Augmentation(self.DB)
        #self.Print_DB(self.DB)
        self.Generate_PCi()

    def Test(self):
        self.testDB = self.Readfile(self.testing_file_name)
        #self.Print_DB(self.testDB)
        self.Predict()





training_file_name = "training.txt"
testing_file_name = "test.txt"

simulate = Naive_Bayes_Classifier(training_file_name, testing_file_name)
Naive_Bayes_Classifier.Train(simulate)
#Naive_Bayes_Classifier.Test(simulate)