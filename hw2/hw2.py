import itertools

class Apriori_like:
    def __init__(self, min_support, input_file_name, ouput_file_name):
        self.min_support = min_support
        self.input_file_name = input_file_name
        self.output_file_name = output_file_name
        self.DB = []
        self.Pre_itemset = []
        self.max_of_items = 0

    def Line_put_into_DB(self, input):
        line_outside = []  #ex.[[30], [90], [40, 70]]最外層的[]
        i = 1
        for a in range(1, len(input), 2):
            if i < len(input): 
                #print(i)
                line_inside = [int(input[i+1])]  #[[30], [90], [40, 70]]最內層30的[]，先將30加進去
                for j in range(i+2, len(input), 2):
                    if input[j] == input[i]:
                        line_inside.append(int(input[j+1]))  #70跟40在同個[]裡
                        i = i + 2  #下次不用再看70
                line_outside.append(line_inside)
                i = i + 2
        #print(line_outside)
        self.DB.append(line_outside)


    def Readfile(self):
        fp = open(self.input_file_name, "r")
        line = fp.readline()
        while line:
            line_string_list = line.split()  #照空格分開 ex.['1', '11', '30', '15', '90', '24', '40', '24', '70']
            self.Line_put_into_DB(line_string_list) #DB建好
            line = fp.readline()  #下一行

    def Combination_generator(self, stuff):#generator of the combination
        j_combination = []
        for L in range(0, len(stuff)+1):
            for subset in itertools.combinations(stuff, L):
                if list(subset) != []:
                    #print(list(subset))
                    j_combination.append(list(subset))
        #print(j_combination)
        return j_combination

    def DBtoC(self):
        itemset1 = []
        for i in self.DB:  #i = [[30], [90], [40, 70]]
            for j in i:          #j = [40, 70]
                j_combination = self.Combination_generator(j) #j_combination = [[40], [70], [40, 70]]
                for k in j_combination:      #k = [40, 70] or [40] or [70]
                    notice = 0
                    for g in range(len(itemset1)): #index of (g = [[10], 3])
                        if k == itemset1[g][0]:
                            itemset1[g][1] = itemset1[g][1] + 1
                            notice = 1
                    if notice == 0:
                        itemset1.append([k, 1])
        return itemset1

    def CtoL(self):  #delete item in C that is not enough to reach  min_support
        L = []
        for i in self.Pre_itemset:  #i = [[40, 70], 3]
            if i[1] >= self.min_support:
                L.append(i)
        return L

    def OldDB_to_newDB(self):
        for i in range(len(self.DB)):  #i = index of ([[30], [90], [40, 70]])
            outside = []  #[3, 6, [4, 5, 7]]
            for j in self.DB[i]:  #j = [30] or [90] or [40, 70]
                inside = []  #[4, 5, 7]
                j_combination = self.Combination_generator(j)
                for k in j_combination:  #k = [40, 70] or [40] or [70]
                    for g in range(len(self.Pre_itemset)):  #g = index of ([[30], 4] or [[90], 4])
                        if k == self.Pre_itemset[g][0]:
                            inside.append(g+1)
                            self.max_of_items = max(g+1, self.max_of_items)
                outside.append(inside)
            self.DB[i] = outside
        print(self.DB)

    def Tuple_to_list_in_list(self,a): #[(1, 2), (1, 3)] -> [[1, 2], [1, 3]]
        for i in range(len(a)):
            a[i] = list(a[i])
        return a

    def Generate_ans(self):
        notice = 0
        length = 2
        while notice == 0:
            Itemset = self.Tuple_to_list_in_list(list(itertools.permutations(list(range(1,self.max_of_items+1)),length))) #generate permutations from 1 to 7 with length = 2
            for i in self.DB:  #i = [[3], [6], [4, 5, 7]]
                i_combination = self.Tuple_to_list_in_list(list(itertools.combinations(i,length)))
                for j in i_combination:  #j = [[3], [4, 5, 7]]
                    ans = []
                    for k in range(len(j)):  #k = index of ([3] or [4, 5, 7])
                        for m in j[k]: #m = 4, 5, 7
                            ans.append(m)
                            print(ans)
                            


            notice = 1


                            
    def run(self):
        self.Readfile()
        self.Pre_itemset = self.DBtoC()
        self.Pre_itemset = self.CtoL()
        self.OldDB_to_newDB()
        self.Generate_ans()


path = ""
input_file_name = path + 'input3.txt'
output_file_name = path + 'output.txt'
#min_support = int(input("Please input min support:"))
min_support = 2

simulate = Apriori_like(min_support, input_file_name, output_file_name)
Apriori_like.run(simulate)