from recommend_utils.nearest_neighbour import *
from recommend_utils.recommender_ch2 import *

print("recommend by nearest neighbour:")
n=recommand_nearest_neighbour("Chan",get_user_list(),2)
print(n)

r = recommender(get_user_list())
r.loadBookDB(path="/Users/sorahjy/Desktop/github/Book-Recommendation-System/datasets/")
print(r.recommend('171118'))
print(r.recommend('171118',5))

