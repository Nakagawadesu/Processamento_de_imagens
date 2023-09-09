import numpy as np
import matplotlib.pyplot as plt
import cv2
import numpy as np
  
# creating a singly linked list
class Coordinate:
    def __init__(self, x,y):
        self.x = x
        self.y = y
        
class Connection:
    def __init__(self, matrix):
        self.image = matrix
        self.values_vector = self.create_vector()
        self.pixels_list = [ [] for _ in range(len(self.values_vector)) ]        

    def map_numbers(self ,value ,values_vector):
        
                exists  = value in values_vector
                if not exists:
                    values_vector.append(value)

    def create_vector(self):

        values_vector = []
    
        rows, cols  = self.image.shape
        for x in range(rows):
            for y in range(cols):
                self.map_numbers(self.image[x][y],values_vector)
            
        return values_vector
                 
                  
        
        
    def find_index(self, value):
        for x in range (len(self.values_vector)) :
            if(self.values_vector[x] == value):
                return x;                


    
    
    def get_connected_pixels_8(self ):
        
        rows, cols  = self.image.shape
        np.sort(self.values_vector )

        for x in range(rows):
            for y in range(cols):

                for dx in [-1,1]:

                    for dy in [-1,1]:
                        new_x = x + dx
                        new_y = y + dy

                        if( new_x <= 6  and new_x >= 0 and new_y <= 6  and new_y >= 0):
                            if (self.image[x][y] == self.image[new_x][new_y] ):
                                index = self.find_index(self.image[x][y])
                                coordinate = Coordinate(new_x,new_y)
                                self.pixels_list[index].append(coordinate)  

    def get_connected_pixels_4(self):
        
        rows, cols  = self.image.shape
        np.sort(self.values_vector )


        for x in range(rows):
            for y in range(cols):

                for dx in [-1,1]:
                    new_x = x + dx
                    

                    if( new_x <= 6  and new_x >= 0 ):
                        if (self.image[x][y] == self.image[new_x][y] ):
                            index = self.find_index(self.image[x][y])
                            coordinate = Coordinate(new_x,y)
                            self.pixels_list[index].append(coordinate) 
                for dy in [-1,1]:
                    
                    new_y = y + dy

                    if(  new_y <= 6  and new_y >= 0):
                        if (self.image[x][y] == self.image[x][new_y] ):
                            index = self.find_index(self.image[x][y])
                            coordinate = Coordinate(x,new_y)
                            self.pixels_list[index].append(coordinate) 


    def print_4_connected(self):
        
        self.get_connected_pixels_4()
        print(f"4 connected, Pixels Values Vector:{self.values_vector}") 
        for x in range (len(self.pixels_list)):
            for y in self.pixels_list[x]:
                print(f"x : {y.x} , y : {y.y} ")

    

    def print_8_connected(self):

        self.get_connected_pixels_4()
        print(f"8 connected , Pixels Values Vector:{self.values_vector}") 
        for x in range (len(self.pixels_list)):
            for y in self.pixels_list[x]:
                print(f"x : {y.x} , y : {y.y} ")        


   
    def histograms(self):

        
        gray_image = np.uint8(self.image)
        hist = cv2.calcHist([gray_image], [0], None, [13], [0, 13])
        accumulated_hist = np.cumsum(hist)
        normalized_hist = hist / hist.sum()


        plt.figure(figsize=(12, 5))
        plt.subplot(131)
        plt.bar(np.arange(13), hist.flatten())
        plt.title("Grayscale Image Histogram")
        plt.xlabel("Pixel Value")
        plt.ylabel("Frequency")

        plt.subplot(132)
        plt.bar(np.arange(13), accumulated_hist.flatten())
        plt.title("Accumulated Histogram")
        plt.xlabel("Pixel Value")
        plt.ylabel("Cumulative Frequency")

        plt.subplot(133)
        plt.bar(np.arange(13), normalized_hist.flatten())
        plt.title("Normalized Histogram")
        plt.xlabel("Pixel Value")
        plt.ylabel("Normalized Frequency")

        plt.tight_layout()
        plt.show()

    def find_stats(self):
        min = 255 
        max = 0
        rows, cols  = self.image.shape
        for x in range(rows):
            for y in range(cols):
               if(self.image[x][y] < min):
                    min = self.image[x][y]
               if(self.image[x][y] > max):
                    max = self.image[x][y]     
        a = 255.0/(max - min)
        b = a * min             
        stats = [a,b]
        return stats
    
    def calculate_contrast(self):
        stats = self.find_stats()
        a = stats[0]
        b = stats[1]
        contrasted_image =  np.zeros_like(self.image)
        rows, cols  = self.image.shape
        for x in range(rows):
            for y in range(cols):
                new_value = a * self.image[x][y] + b
                contrasted_image[x][y] =  new_value     
        return contrasted_image
    
    def print_matrix(self,matrix):
        
        rows, cols  = matrix.shape
        
        for x in range(rows):
            buffer = []
            for y in range(cols):
                buffer.append(matrix[x][y])
            print(f'{buffer} ')  
                
    
    def transform(self):

        transformed_image = np.zeros_like(self.image)        
        rows, cols  = self.image.shape

    
        for x in range(rows):
            for y in range(cols):
                if(self.image[x][y] <= 8):
                    new_value = 8
                   
                elif(self.image[x][y] >= 11  ):
                    new_value = 11
                       
                else:
                    new_value = 10  
                   
                transformed_image[x][y] =  new_value
         
        return transformed_image
    
image = np.array([
    [4,5,7,7,7,8,6],
    [7,6,7,5,7,7,7],
    [6,5,4,10,12,12,11],
    [10,9,8,7,5,5,6],
    [11,8,8,8,7,6,6],
    [5,6,7,6,6,6,6],
    [4,5,10,9,9,8,8]
])

connection_obj = Connection(image)
connection_obj.print_4_connected()
connection_obj.print_8_connected()
connection_obj.histograms()

print('contrasted:')
contrasted_image = connection_obj.calculate_contrast()
connection_obj.print_matrix(contrasted_image)

print('transformed:')
connection_obj.transform()
transformed_image = connection_obj.transform()
connection_obj.print_matrix(transformed_image)