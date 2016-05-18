#!/usr/bin/python3

import os
import sys
import math
import numpy as np
import array

import statistics



import matplotlib.pyplot as plt
 

class WikiGraph:
    '''функция load_from_file загружает граф из файла'''
    def load_from_file(self, filename):
        print('Загружаю граф из файла: ' + filename)

        with open(filename) as f:
            (self.n, self._nlinks) = (map(int, f.readline().split()))
            
            self._titles = []  # список названий статей
            self._sizes = array.array('L', [0]*self.n) # список с размерами i-ой статьи
            self._links = array.array('L', [0]*self._nlinks) #список ссылок на статьи - метод Compressed Sparse Row
            self._redirect = array.array('B', [0]*self.n) # флаг перенаправления 
            self._offset = array.array('L', [0]*(self.n+1)) #  в i-ой ячейке содержится информация с какого номера начинаются ссылки в self._links  для i-й статьи
            current_link = 0
            for i in range(self.n):
                __title = f.readline()
                self._titles.append(__title.rstrip())
                (size, redirect, amout_links) = (map(int, f.readline().split()))
                self._sizes[i] = size
                self._redirect[i] = redirect
                for j in range(current_link, current_link + amout_links):
                    self._links[j] = int(f.readline())
                current_link += amout_links
                if self.n > 0:
                    self._offset[i+1] = self._offset[i] + amout_links

        print('Граф загружен')
        

  

    def get_id(self, title):
        _id = 0
        for name in self._titles:
            if name == title:
                return int(_id)
                 
            else:
                 _id += 1
    def get_number_of_links_from(self, _id):
        return int(self._offset[_id+1] - self._offset[_id]) 
                    
    def get_links_from(self, _id):
        return self._links[self._offset[_id]:self._offset[_id+1]]
        
    def get_number_of_pages(self):
        return len(self._titles)

    def is_redirect(self, _id):
        if self._redirect[_id]:
            return True
        else:
            return False
            
    def get_title(self, _id):
        return self._titles[_id]

    def get_page_size(self, _id):
        return self._sizes[_id]
        
'''третье упражнение из задания на judje_mipt'''
def task_3_from_Hiryanov(self):
      f = open('task_3_from_Hiryanov.txt', 'w')
      
      '''внутренний анализ статей'''
      '''зададим необходимые переменные'''
      redirected_titels = 0
      number_of_links = []
      amount_of_pages_with_min_number_of_links = 0   
      amount_of_pages_with_max_number_of_links = 0 
      list_of_articels_with_max_links = ''
      
      '''циклы'''   
      for i in range(self.get_number_of_pages()):
           if self.is_redirect(i):
               redirected_titels += 1
           number_of_links.append(self.get_number_of_links_from(i))
      max_number_of_links = max(number_of_links)                    
      min_number_of_links = min(number_of_links) 
      
                         
      for i in  range(self.get_number_of_pages()):
           if self.get_number_of_links_from(i) == min_number_of_links:
                amount_of_pages_with_min_number_of_links  += 1
           if self.get_number_of_links_from(i) == max_number_of_links:
                amount_of_pages_with_max_number_of_links +=1
                list_of_articels_with_max_links += str(self._titles[i]) 
             
      global   dict_amount_of_links_from_page       
      dict_amount_of_links_from_page = {}
      for i in range (self.get_number_of_pages()):
           if not G.get_number_of_links_from(i) in dict_amount_of_links_from_page:
               dict_amount_of_links_from_page[G.get_number_of_links_from(i)] = 1
           else:
               dict_amount_of_links_from_page[G.get_number_of_links_from(i)] += 1            
      
      '''внешний анализ статей'''
      num_of_links_to_page = [0 for i in range(G.get_number_of_pages())]
      for i in range(G.get_number_of_pages()): # пробегаемся по каждой статье
          for elem in G.get_links_from(i): # смотрим на какие статьи ссылается i-я статья, и к этим статьям добавляем +1 к количеству ссылок на них
                      
             num_of_links_to_page[int(elem)] += 1
             if G.is_redirect(i):
                  num_of_links_to_page[int(elem)] -= 1
                  
      pages_with_max_num_of_to_links = [G.get_title(i) for i in range(G.get_number_of_pages()) if num_of_links_to_page[i] == max(num_of_links_to_page)]  

      global dict_num_of_links_to_page 
      dict_num_of_links_to_page = {}
      for i in range(len(num_of_links_to_page)):
         if  num_of_links_to_page[i] not in  dict_num_of_links_to_page:
            dict_num_of_links_to_page[num_of_links_to_page[i]] = 1
         else:
            dict_num_of_links_to_page[num_of_links_to_page[i]] += 1
      
      ''' анализ перенаправлений'''
      global redirects_to_page
      redirects_to_page = [0 for i in range(G.get_number_of_pages())]
      for i in range(G.get_number_of_pages()):
          for elem in G.get_links_from(i):
               if G.is_redirect(i) == 1:
                   redirects_to_page[elem] += 1
      pages_with_max_num_of_redirects  = [G.get_title(i) for i in range(G.get_number_of_pages()) if redirects_to_page[i] == max(redirects_to_page) ]
      global max_amount_of_redirected_pages 
      max_amount_of_redirected_pages = max(redirects_to_page)
      
      '''путь '''
      way = bfs(G, 'Python','Список_файловых_систем')
      way = [G.get_title(way[i]) for i in range(len(way)) ]
      
      
              
                 
      f.write('количество статей с перенаправлением: ' + str(redirected_titels) + '\n' +
              'минимальное количество ссылок из статьи: ' + str(min_number_of_links) + '\n' +
              'количество статей с минимальным количеством ссылок: ' + str(amount_of_pages_with_min_number_of_links) + '\n' + 
              'максимальное количество ссылок из статьи: ' + str(max_number_of_links) + '\n' +
              'количество статей с максимальным количеством ссылок: ' + str(amount_of_pages_with_max_number_of_links) + '\n' +
              'cтатьи с наибольшим количеством ссылок: '+ list_of_articels_with_max_links + '\n' + 
              'среднее количество ссылок в статье: ' + str(round(self._nlinks / self.n)) + '\n'  +
              'Минимальное количество ссылок на статью: ' + str(min(num_of_links_to_page)) + '\n'  +
              'Количество статей с минимальным количеством внешних ссылок: ' + str(sum(elem == min(num_of_links_to_page) for elem in num_of_links_to_page )) + '\n' + 
              'Максимальное количество ссылок на статью: ' + str(max(num_of_links_to_page)) + '\n'  +
              'Количество статей с максимальным количеством внешних ссылок: ' + str(sum(elem == max(num_of_links_to_page) for elem in num_of_links_to_page )) + '\n' +
              'Статья с наибольшим количеством внешних ссылок' + str(pages_with_max_num_of_to_links) + '\n' + 
              "Среднее количество внешних ссылок на статью: %0.2f  (ср. откл. : %0.2f)" %(statistics.mean(num_of_links_to_page), statistics.stdev(num_of_links_to_page)) + '\n' + 
              'Минимальное количество перенаправлений на статью: ' + str(min(redirects_to_page)) + '\n' +
              'Количество статей с минимальным количеством внешних перенаправлений: ' + str(sum(elem == min(redirects_to_page) for elem in redirects_to_page)) + '\n' + 
              'Максимальное количество перенаправлений на статью: ' + str(max(redirects_to_page)) + '\n'  +
              'Количество статей с максимальным количеством внешних перенаправлений: ' + str(sum(elem == max(redirects_to_page) for elem in redirects_to_page)) + '\n' +        'Статья с наибольшим количеством внешних перенаправлений:' + str(pages_with_max_num_of_redirects)  + '\n' + 
              "Среднее количество внешних перенаправлений на статью: %0.2f  (ср. откл. : %0.2f)" %(statistics.mean(redirects_to_page), statistics.stdev(redirects_to_page)) + '\n' + 'путь, по которому можно добраться от статьи Python до статьи Список_файловых_систем: ' + str(way) )


# отдельно оформим функицию обхода в ширину
def bfs(G, start, finish):  
    start, finish = G.get_id(start), G.get_id(finish)  
    parent = {start: None}
    i = 1
    queue = [start]
    while queue:
          new_queue = []
          for current in queue:
               for v in G.get_links_from(current):
                    if v not in parent:
                       parent[v] = current
                       new_queue.append(v)
                    if v == finish:
                       break                   
          queue = new_queue 
              
    _way = [finish]
    current = parent[finish]
    while  current:
        _way.append(current) 
        current = parent[current]
    _way = _way[::-1]   
    
    return _way                
           
    

                   
def hist(objects, data, liamda, xlabel, ylabel, title, facecolor='green', alpha=0.5, transparent=True):
    
    x_pos = np.arange(len(objects))
    
 
    x_pos_im = np.arange( 0, max(objects), liamda)
    
    plt.bar(x_pos, data, align='center', alpha=0.5)
    plt.xticks(x_pos_im)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.title(title)
    
    plt.plot()
    



'''задание 4 - гистограммы'''
def task_4_hists(self):
     
     ''' 1 --- распределение количества ссылок из статьи'''

     x, y = [], []      
     liamda = len(dict_amount_of_links_from_page) / 10   
     for elem in dict_amount_of_links_from_page:
          x.append(elem)
          y.append(dict_amount_of_links_from_page[elem])
     plt.figure(1)
     hist(x, y, liamda,'кол-во ссылок', 'кол-во статей ','распределение количества ссылок из статьи')  # распределение количества ссылок из статьи 

     ''' 2 --- распределение количества ссылок на статью'''
     x, y = [], []
     liamda = len(dict_num_of_links_to_page)/10
     for elem in dict_num_of_links_to_page:
        x.append(elem)
        y.append(dict_num_of_links_to_page[elem])
     plt.figure(2)
     hist(x, y,liamda, 'кол-во внешних ссылок', 'кол-во статей ','распределение количества ссылок на статью')  


     ''' 3  --- распределение размеров статей'''
     liamda = 8000 
     interval = [[(i*liamda),((i+1)*liamda)] for i in range(max(self._sizes)//liamda)]
     size_hist = {}
     for i in range(self.get_number_of_pages()):
          for j in range(len(interval)):
              if (self.get_page_size(i) > interval[j][0]) and (self.get_page_size(i) < interval[j][1]):
                     if j not in  size_hist:
                         size_hist[j] = 1
                     else:
                         size_hist[j] += 1   
     x,y  = [0 for i in range(len(interval))], [0 for i in range(len(interval))]
     y_log = [0 for i in range(len(interval))]
     for j in size_hist:
          x[j] = interval[j][1]
          y[j] = size_hist[j]       
          y_log[j] =  math.log(size_hist[j]) 
     plt.figure(3)     
        
          
     hist(x, y, liamda, 'размер статей', 'кол-во статей ','распределение размеров статей') 
     
     ''' 4  --- распределение размеров статей в логарифмическом масшате'''
     plt.figure(4)
     hist(x, y_log, liamda,'размер статей', 'кол-во статей в логарифмическом масштабе ','распределение размеров статей')
     ''' 5  --- распределение количества перенаправлений на статью''' 
     plt.figure(5)
     liamda = 1 
    
     hist_redirects_to_page = {}
     for elem in redirects_to_page:
         if elem not in hist_redirects_to_page:
             hist_redirects_to_page[elem] = 1
         else:
             hist_redirects_to_page[elem] += 1
     x,y = []*len(hist_redirects_to_page),[]*len(hist_redirects_to_page) 
     
     for j in hist_redirects_to_page:
         x.append(j)
         y.append(hist_redirects_to_page[j])
         
     hist(x, y, liamda, 'кол-во перенаправлений', 'кол-во статей ','распределение количества перенаправлений на статью')      
             
     plt.show()
   
        
'''создадим граф под названием G '''         
G = WikiGraph()    
G.load_from_file('wiki_small.txt')        
'''запустим функцию 3-го задания'''
task_3_from_Hiryanov(G) 
'''запустим функцию 4-го задания'''   
task_4_hists(G)      


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Использование: wiki_stats.py <файл с графом статей>')
        sys.exit(-1)

    if os.path.isfile(sys.argv[1]):
        wg = WikiGraph()
        wg.load_from_file(sys.argv[1])
    else:
        print('Файл с графом не найден')
        sys.exit(-1)
    
      

   
