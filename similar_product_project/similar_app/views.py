from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.contrib import messages
import pandas as pd # data processing
import matplotlib.pyplot as plt # visualization
import fuzzyset
from sklearn.model_selection import train_test_split # data split

amazone_data = pd.read_csv('C:/Users/ashis/OneDrive/Desktop/house/similar_product_project/similar_app/amz_com_ecommerce_sample.csv', encoding= 'unicode_escape')
flipkart_data = pd.read_csv('C:/Users/ashis/OneDrive/Desktop/house/similar_product_project/similar_app/flipkart_com_ecommerce_sample.csv', encoding= 'unicode_escape')
# Create your views here.

def matched_data(request):
	if request.method == 'POST':
		search_product = request.POST.get('user_input')
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

		# search_product = "FDT Women's Leggings Pants"
		print(search_product)
		final_amz_product = amazone_set.get(search_product)[0][1]
		final_flip_product = flipkart_set.get(search_product)[0][1]

		final_retail_price_amz = amazone_data.loc[amazone_data['product_name'] == final_amz_product, 'retail_price'].iloc[0]
		final_discount_price_amz = amazone_data.loc[amazone_data['product_name'] == final_amz_product, 'discounted_price'].iloc[0]

		final_retail_price_flip = flipkart_data.loc[flipkart_data['product_name'] == final_flip_product, 'retail_price'].iloc[0]
		final_discount_price_flip = flipkart_data.loc[flipkart_data['product_name'] == final_flip_product, 'discounted_price'].iloc[0]
	final_output=[]
	temp_dict = {
		'final_amz_product': final_amz_product,
		'final_flip_product': final_flip_product,
		'final_retail_price_amz':final_retail_price_amz,
		'final_discount_price_amz':final_discount_price_amz,
		'final_retail_price_flip': final_retail_price_flip,
		'final_discount_price_flip':final_discount_price_flip,
	}
	final_output.append(temp_dict)
	return render(request, 'similar_app/index.html', {'context':final_output})


def index(request):
	return render(request, 'similar_app/index.html')