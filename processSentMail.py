# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 16:24:21 2017

@author: bmyers
"""
#Websites and example code I used to figure this out:
#https://github.com/rogerhoward/nltk-examples/blob/f0648168983f813199e0381047f3a19875239288/freqdist_top_words.py
#https://stackoverflow.com/questions/952914/making-a-flat-list-out-of-list-of-lists-in-python
#http://n-chandra.blogspot.com/2014/06/collocation-extraction-using-nltk.html
#https://pythonspot.com/en/matplotlib-bar-chart/


import nltk
import csv
import itertools
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from nltk.tokenize import word_tokenize,wordpunct_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.collocations import *
import re


#-----------------------------------------------
#open file, create csv reader, set up stopword lists
#-----------------------------------------------
with open("sent final.csv", "r", encoding="utf8") as csvfile:
    reader = csv.reader(csvfile)
    stop_words = set(nltk.corpus.stopwords.words('english'))
    stopwords_file = './stopwords.txt'
    stop_words2 = set(open(stopwords_file, 'r').read().splitlines())
    all_stopwords = stop_words | stop_words2
    
#-----------------------------------------------
#create lists of topic words
#-----------------------------------------------
    citation_words = ['endnote', 'zotero', 'citation']
    literature_searching_words = ['pubmed', 'cinahl', 'database', 'databases', 'literature', 'review','search']
    access_words = ['access', 'vpn', 'proxy', 'ILL', 'interlibrary loan', 'card', 'number']
    policy_words = ['room', 'checking', 'check', 'hours', 'fine', 'fines', 'account', 'laptop', 'laptops']
    knownitem_words = ['article', 'articles', 'book', 'books', 'ebook', 'ebooks', 'e-book', 'e-books', 'journal', 'journals']
    systematic_words = ['systematic','meta','analysis','meta-analysis']
    consultation_words = ['appointment','meet','meeting','available','date']
    
#-----------------------------------------------
#create lists of department words
#-----------------------------------------------    
    nursing_words = ['cinahl', 'nursing', 'nurse']
    publichealth_words = ['public', 'epidemiology', 'biostatistics', 'environmental', 'management', 'community']
    dentistry_words = ['dental', 'dentistry', 'dentist', 'oral']
    medicine_words = ['medicine', 'mednet']
    psych_words = ['psychiatry', 'psychology', 'behavioral', 'dsm', 'cognitive']
    lifesci_words = ['molecular', 'ecology', 'biology', 'life', 'protocol', 'protocols']
    
#-----------------------------------------------
#create list to store word results
#-----------------------------------------------
    result = []
    
#-----------------------------------------------
#create variables for holding email topic counts
#-----------------------------------------------
    citation_management = 0
    litsearch = 0
    access = 0
    policy = 0
    knownitem = 0
    systematic = 0
    consultation = 0
    
#-----------------------------------------------
#create variables for holding email departmental counts
#-----------------------------------------------
    nursing = 0
    publichealth = 0
    dentistry = 0
    medicine = 0
    psych = 0
    lifesci = 0
    
#-----------------------------------------------
#iterate through each row and field in the csv: the indentation of this section continues
#-----------------------------------------------
    for row in reader:
        for field in row:
               
#-----------------------------------------------
#tokenize (break into word units)
#-----------------------------------------------                
            tokens = word_tokenize(field)
            tokens = [token.lower() for token in tokens]
            tokens = [word for word in tokens if word not in all_stopwords]
            
#-----------------------------------------------
#tokenize (break into word units) and increment a counter to keep track of words in email topic categories
#-----------------------------------------------             
            tokens = [word for word in tokens if len(word) >= 5] #1 gets rid of punctuation, longer = more useful?
            if any(word in citation_words for word in tokens): #these lines count number of emails that any words related to citation management appear in
                citation_management += 1 #these lines count number of emails that any words related to citation management appear in
            if any(word in literature_searching_words for word in tokens): #these lines count number of emails that any words related to lit searching appear in
                litsearch += 1
            if any(word in access_words for word in tokens): #these lines count number of emails that any words related to known item access appear in
                access += 1
            if any(word in policy_words for word in tokens): #these lines count number of emails that any words related to policy appear in
                policy += 1
            if any(word in knownitem_words for word in tokens): #these lines count number of emails that any words related to policy appear in
                knownitem += 1
            if any(word in systematic_words for word in tokens): #these lines count number of emails that any words related to policy appear in
                systematic += 1
            if any(word in consultation_words for word in tokens): #these lines count number of emails that any words related to policy appear in
                consultation += 1
 
#-----------------------------------------------
#tokenize (break into word units) and increment a counter to keep track of words in dept topic categories
#-----------------------------------------------  
            if any(word in nursing_words for word in tokens): #these lines count number of emails that any words related to nursing appear in
                nursing += 1 
            if any(word in publichealth_words for word in tokens): #these lines count number of emails that any words related to public health appear in
                publichealth += 1 
            if any(word in dentistry_words for word in tokens): #these lines count number of emails that any words related to dentistry appear in
                dentistry += 1
            if any(word in medicine_words for word in tokens): #these lines count number of emails that any words related to medicine appear in
                medicine += 1
            if any(word in psych_words for word in tokens): #these lines count number of emails that any words related to psych appear in
                psych += 1
            if any(word in lifesci_words for word in tokens): #these lines count number of emails that any words related to life sciences appear in
                lifesci += 1
            result.append(tokens)
#-----------------------------------------------
#flatten the result list (results is a list full of lists right now)
#-----------------------------------------------

flat_list = list(itertools.chain(*result))

#-----------------------------------------------
#take user input to count specific words
#-----------------------------------------------

#wordin = input("What word would you like to count? ")
#if any(word in wordin for word in flat_list):
#    print(wordin + " was found " + str(flat_list.count(wordin)) + " times.")
#else:
#    print("Word not found.")

#-----------------------------------------------
#find and plot frequency distributions of words
#-----------------------------------------------

#fdist = nltk.FreqDist(flat_list)
#fdist.plot(20, cumulative=False)

#for word,frequency in fdist.most_common(50):
#    print('{};{}'.format(word, frequency))

#-----------------------------------------------
#print counts for email topic categories
#-----------------------------------------------
print("There were " + str(citation_management) + " emails that mentioned citation management.") #how many emails are related to citation management?
print("There were " + str(litsearch) + " emails that mentioned literature search topics.") #how many emails are related to literature searching?
print("There were " + str(access) + " emails that mentioned access topics.") #how many emails are related to access?
print("There were " + str(policy) + " emails that mentioned policy topics.") #how many emails are related to policy?
print("There were " + str(knownitem) + " emails that mentioned known item topics.") #how many emails are related to known items?
print("There were " + str(systematic) + " emails that mentioned systematic review topics.") #how many emails are related to systematic reviews?
print("There were " + str(consultation) + " emails that mentioned consultation topics.") #how many emails are related to consultations?           

#-----------------------------------------------
#plot email topic categories
#----------------------------------------------- 
objects = ('Citation\nmanagement', 'Literature\nsearching', 'Access', 'Policy', 'Known\nItem\nLookup', 'Systematic\nReviews', 'Consultation\nRequests')
y_pos = np.arange(len(objects))
counts = [citation_management, litsearch, access, policy, knownitem, systematic, consultation]

plt.bar(y_pos, counts, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.xlabel('Topics')
plt.ylabel('Number of emails')
plt.title('Topics by number of emails')
fig = plt.gcf()
fig.set_size_inches(12,6)
plt.show()

#-----------------------------------------------
#print counts for email departmental categories
#-----------------------------------------------
print("There were " + str(nursing) + " emails that mentioned nursing topics.") #how many emails are related to nursing?
print("There were " + str(publichealth) + " emails that mentioned public health topics.") #how many emails are related to public health?
print("There were " + str(dentistry) + " emails that mentioned dentistry topics.") #how many emails are related to dentistry?
print("There were " + str(medicine) + " emails that mentioned medicine topics.") #how many emails are related to medicine?
print("There were " + str(psych) + " emails that mentioned psychology/psychiatry topics.") #how many emails are related to psych?
print("There were " + str(lifesci) + " emails that mentioned life sciences topics.") #how many emails are related to life sciences?

#-----------------------------------------------
#plot dept topic categories
#----------------------------------------------- 
objects = ('Nursing', 'Public\nHealth', 'Dentistry', 'Medicine', 'Psychology/\nPsychiatry', 'Life\nSciences')
y_pos = np.arange(len(objects))
counts = [nursing, publichealth, dentistry, medicine, psych, lifesci]

plt.bar(y_pos, counts, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.xlabel('Topics')
plt.ylabel('Number of emails')
plt.title('Topics by number of emails')
fig = plt.gcf()
fig.set_size_inches(12,6)
plt.show()

#-----------------------------------------------
#most likely collocations
#-----------------------------------------------

#bigram_measures = nltk.collocations.BigramAssocMeasures()
#finder = BigramCollocationFinder.from_words(flat_list, 5)
#print(finder.apply_freq_filter(5))
#print(finder.nbest(bigram_measures.likelihood_ratio, 20))