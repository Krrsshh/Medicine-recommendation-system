# Medicine-recommendation-system

This is my personal project where I experimented with Content based recommnedation system using "Bag of Words" concept. This project deals with medicine_data (https://www.kaggle.com/datasets/mohneesh7/indian-medicine-data) that I got from kaggle. 

I deal with data preprocessing and preparing tags for each medicine and then perform vecotrization and write a recommendation function that recommends medicines based on similarity of vectors.

**Data Preprocessing**

The data comes with columns  "sub_category	product_name	salt_composition	product_price	product_manufactured	medicine_desc	side_effects ". I eliminated columns 'product_price', 'sub_category', 'product_manufactured', 'drug_interactions' as they are not that usedful for our recommendation system.
Then the duplicate rows and nulls are eliminated and we are left with 7477 rows of data. We then use the columns medicines salt composition, medicine description and side effects to create tags. The columns are converted nto list and a new column is created called tags with a list combining all the three required columns. The we perform stemming to eliminate similar words using the library nltk. We use PorterStemmer from nltk and create a function to stem our tags. Then we make all our tags lower cased for better performance of algorithm.

**Vectorization**

I created vectors for each tag using featureextraction from sklearn library. CountVectorizer from this library creates set no.of vectors for each tag by ignoring stop words. We perform this function on all vectors to create an array of vectors. Then we applu cosine_similarity() from sklearn to create a similarity matrix for each tag with all the other tags. The similarity score ranges from 0 to 1, 0 beaing most dissimilar and 1 being the most similar tag. We use this matrix to write a function to extract top 5 medicines with high similarity index when compared to input medicine.

**Demo Website**

I further include medicine_recommnedation_app.py file where we create a demo website usng streamlit. We pickle the data from our main code to deploy this website.

If you got a medicine with you and are interested to explore your options with similar medicines before using it, here you go!!!  This is a perfect tool built with a database of 7000 medicines.
