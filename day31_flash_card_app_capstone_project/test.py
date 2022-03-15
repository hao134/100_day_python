import pandas
import random

data = pandas.read_csv("./flash-card-project-start/data/french_words.csv")

dict_data = data.to_dict('records')
# #print(dict_data[random.randint(0,99)]['French'])
#
# random_num = random.randint(0,len(data)-1)
# print(random_num)
# print(dict_data[random_num]['French'])
#
# # print(current_card)
# # print(data)
#
# data = data.drop([random_num])
# print(data)
# data.to_csv("test.csv",index = False)
current_card = random.choice(dict_data)
current_card_index = dict_data.index(current_card)
print(current_card_index)

