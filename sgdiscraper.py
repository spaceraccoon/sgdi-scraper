import re
import requests
from bs4 import BeautifulSoup
from urlparse import urljoin
import csv

output = []
BASE_URL = 'https://www.gov.sg'

def parse(names):
    for name in names:
        if len(name.contents) < 2:
            continue

        print name.contents[1]
        text = name.contents[1].split()
        salutation = ''
        firstname = ''
        lastname = ''
        gender = ''
        person = {}
        for word in text:
            word = word.encode('ascii', 'ignore')
            male_salutations = {'Mr'}
            female_salutations = { 'Mrs', 'Mdm', 'Ms', 'Miss'}
            neutral_salutations = {'Dr', 'Dr.', 'Prof', 'A/Prof', 'Professor', 'Assoc Prof', 'Adjunct Assoc Prof', 'Prof.'}
            forbidden = {'PPS', 'PPA(E)', 'PPA(S)', 'PPA(G)', 'PPA(P)', 'PBS', 'PPA(P)(T)', 'PPA(P)(L)', 'PPA(E)(L)', 'PPA(EMAS)', 'PJG', 'A/P',
                         'BBM', 'PBM', 'BBM(L)', 'PB', 'PJG', 'PPA (G)', 'PPA(G),', 'PPA(E),', 'PPA(P),', 'PB,'}
            if word in forbidden:
                continue
            elif word in male_salutations:
                salutation = word
                gender = 'Male'
            elif word in female_salutations:
                salutation = word
                gender = 'Female'
            elif word in neutral_salutations:
                salutation = word                    
            elif word == word.upper():
                lastname = lastname + word[0] + word[1:].lower() + ' '
                
            else:
                if word.isalpha():
                    print word
                    firstname = firstname + word +  ' '
        
        print 'Salutation: ' + salutation
        print 'First Name: ' + firstname[:-1]
        print 'Last Name: ' + lastname[:-1]
        print 'Gender: ' + gender
        person['Salutation'], person['First Name'], person['Last Name'], person['Gender'] = salutation, firstname[:-1], lastname[:-1], gender

        output.append(person)
        print person
        print len(output)

def process(url):
    r = requests.get(BASE_URL + url)
    soup = BeautifulSoup(r.text, 'xml')

    # Scraping code hidden due to terms of use

    if names is not None:
        parse(names)

r = requests.get('https://www.gov.sg/sgdi/ministries')
soup = BeautifulSoup(r.text, "lxml")

# Scraping code hidden due to terms of use

for ministry in ministries:
    process(ministry['href'])

keys = output[0].keys()
with open('people.csv', 'wb') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(output)
