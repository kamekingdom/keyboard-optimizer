# Levenshtein距離で類似度を計算

import Levenshtein
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

array1 = ["T", "G", "H", "V", ",", ";", "J", "P", "I", "D", "X", "Y", ".", "/", "W", "S", "N", "A", "F", "O", "Q", "E", "B", "Z", "L", "U", "K", "C", "M", "R"]
array2 = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/']
array3 = ["S", "R", "M", "T", "W", "O", "V", ",", "N", "X", "Z", ".", "H", "D", "J", "P", "F", "G", ";", "I", "/", "A", "C", "E", "U", "Y", "B", "K", "L" ,"Q"]

string1 = ""
string2 = ""
string3 = ""

for word1, word2, word3 in zip(array1, array2, array3):
    string1 += word1
    string2 += word2
    string3 += word3

print(f"string1: {string1}")
print(f"string2: {string2}")
print(f"string3: {string3}")

def caliculate_levenshtein_similarity(string1, string2):
    distance = Levenshtein.distance(string1, string2)
    max_length = max(len(string1), len(string2))
    similarity = (max_length - distance) / max_length
    return similarity

def calculate_cosine_similarity(string1, string2):
    strings = [string1, string2]
    vectorizer = CountVectorizer().fit_transform(strings)
    vectors = vectorizer.toarray()
    
    # コサイン類似度を計算
    cosine_sim = cosine_similarity(vectors[0].reshape(1, -1), vectors[1].reshape(1, -1))
    
    return cosine_sim[0][0]

english_levenshtein_similarity = caliculate_levenshtein_similarity(string1, string2)
english_cosine_similarity = calculate_cosine_similarity(string1, string2)
japanese_levenshtein_similarity = caliculate_levenshtein_similarity(string1, string3)
japanese_cosine_similarity = calculate_cosine_similarity(string1, string3)

data = {
    "Method": ["cosine", "levenshtein"],
    "英語": [english_cosine_similarity, english_levenshtein_similarity],
    "日本語": [japanese_cosine_similarity, japanese_levenshtein_similarity]
}

df = pd.DataFrame(data)
print(df)
