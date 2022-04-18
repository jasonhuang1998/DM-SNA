import matplotlib.pyplot as plt
import math

class Agglomerative_Nesting:
    def __init__(self, input_file_name, output_file_name, final_cluster_num):
        self.input_file_name = input_file_name
        self.output_file_name = output_file_name
        self.final_cluster_num = final_cluster_num
        self.DB = []
        self.clusterDB = []


    def Readfile(self):
        input_file = open(self.input_file_name)

        for i in input_file.readlines(): # i = 60.429691757606356 71.37031119462944\n
            coordinate = i.split(" ") # coordinate = ['60.429691757606356', '71.37031119462944\n']
            coordinate[0] = float(coordinate[0])
            coordinate[1] = float(coordinate[1][:-1])

            #coordinate = [60.429691757606356, 71.37031119462944]
            self.DB.append(coordinate)

        input_file.closed


    def Show_DB_Graph(self): #Show DB in xy graph
        x, y = zip(*self.DB)
        plt.scatter(x, y)
        plt.show()

    def Show_ClusterDB(self):
        x, y = zip(*self.clusterDB[0])
        plt.scatter(x, y, color = ['red'])
        x, y = zip(*self.clusterDB[1])
        plt.scatter(x, y, color = ['blue'])
        x, y = zip(*self.clusterDB[2])
        plt.scatter(x, y, color = ['green'])
        x, y = zip(*self.clusterDB[3])
        plt.scatter(x, y, color = ['brown'])

        plt.show()


    def Print_DB(self, input): #Print DB line by line
        for i in input:
            print(i)


    def Print_DB_graph(self):
        self.Readfile()
        self.Show_DB_Graph()


    def Create_cluster(self):
        for i in self.DB: # i = [60.429691757606356, 71.37031119462944]
            tmp = [i] # tmp = [[60.429691757606356, 71.37031119462944]]
            self.clusterDB.append(tmp)


    def Put_list2_in_list1_and_Delete_list2(self, list1_index, list2_index):
        for i in self.clusterDB[list2_index]:
            self.clusterDB[list1_index].append(i)
        
        del self.clusterDB[list2_index]
        
        

    def Clust(self):
        while len(self.clusterDB) > self.final_cluster_num:
            min_dist = [self.Average_Linkage_Agglomerative_Algorithm(self.clusterDB[0], self.clusterDB[1]), 0, 1]
            #if dist(list_i, list_j) is shortest, min_dist = [dist(list_i, list_j), i, j]
            for i in range(len(self.clusterDB)):
                for j in range(len(self.clusterDB)):
                    if i != j:
                        dist = self.Average_Linkage_Agglomerative_Algorithm(self.clusterDB[i], self.clusterDB[j])
                        if dist < min_dist[0]:
                            min_dist = [dist, i, j]

            self.Put_list2_in_list1_and_Delete_list2(min_dist[1], min_dist[2])
            

    def Average_Linkage_Agglomerative_Algorithm(self, list1, list2):
        sum = 0
        for i in list1:
            for j in list2:
                x1 = i[0]
                y1 = i[1]
                x2 = j[0]
                y2 = j[1]
                sum = sum + math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 )
        return sum


    def Print_output_in_File(self):
        of = open(self.output_file_name, "a")
        for i in range(len(self.clusterDB)):
            for j in self.clusterDB[i]:
                of.write(str(j[0]))
                of.write(" ")
                of.write(str(j[1]))
                of.write(" ")
                of.write("ClusterID = ")
                of.write(str(i))
                of.write("\n")

        of.close()


    def Run(self):
        self.Readfile()
        self.Create_cluster()
        self.Clust()
        #self.Print_DB(self.clusterDB)
        self.Show_ClusterDB()
        self.Print_output_in_File()


input_file_path = "dataset/"
output_file_path = ""

dataset_id = 5
input_file_name = "Clustering_test" + str(dataset_id)
output_file_name = input_file_name + "_output.txt"

final_cluster_num = 4

simulate = Agglomerative_Nesting(input_file_path + input_file_name,output_file_path + output_file_name, final_cluster_num)
#simulate.Print_DB_graph()
simulate.Run()