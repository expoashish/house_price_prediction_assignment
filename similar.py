import pandas as pd # data processing
import matplotlib.pyplot as plt # visualization
import fuzzyset
from sklearn.model_selection import train_test_split # data split

amazone_data = pd.read_csv('amz_com_ecommerce_sample.csv', encoding= 'unicode_escape')
flipkart_data = pd.read_csv('flipkart_com_ecommerce_sample.csv', encoding= 'unicode_escape')
# print(amazone_data.head())
# print(amazone_data.shape)
# print(amazone_data.describe()) #mean, median, standard deviation
# print(amazone_data.isnull().sum())
# print(amazone_data.duplicated().sum())
# print(amazone_data.dtypes)

amazone_set = fuzzyset.FuzzySet()
flipkart_set = fuzzyset.FuzzySet()

amazone = amazone_data[["product_name"][0]].tolist()
# amazone=amazone[0:100]
flipkart = flipkart_data[["product_name"][0]].tolist()
# flipkart=flipkart[0:100]
for text in amazone:
    amazone_set.add(text.strip())
for text in flipkart:
    flipkart_set.add(text.strip())

search_product = "FDT Women's Leggings"
print('searching .....',search_product)
final_amz_product = amazone_set.get(search_product)[0][1]
final_flip_product = flipkart_set.get(search_product)[0][1]

final_retail_price_amz = amazone_data.loc[amazone_data['product_name'] == final_amz_product, 'retail_price'].iloc[0]
final_discount_price_amz = amazone_data.loc[amazone_data['product_name'] == final_amz_product, 'discounted_price'].iloc[0]

final_retail_price_flip = flipkart_data.loc[flipkart_data['product_name'] == final_flip_product, 'retail_price'].iloc[0]
final_discount_price_flip = flipkart_data.loc[flipkart_data['product_name'] == final_flip_product, 'discounted_price'].iloc[0]

print("Amz Product Name = ",final_amz_product)
print("Amz Retail Price = ",final_retail_price_amz)
print("Amz Discount Price = ",final_discount_price_amz)
print("Flip Product Name = ",final_flip_product)
print("Flip Retail Price = ",final_retail_price_flip)
print("Flip Discount Price = ",final_discount_price_flip)
