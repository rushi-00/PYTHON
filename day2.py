# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 09:12:47 2024

@author: SATYAM
"""

import re

chat1 = 'Hello, I am having an issue with my order #41240093'

pattern = 'order[^\d]*(\d*)'
matches = re.findall(pattern, chat1)
matches

############################################################

chat2 = 'I have a problem with my order number 412302992'
pattern = 'order[^\d]*(\d*)'
matches = re.findall(pattern, chat2)
matches

#############################################################

chat3 = 'My order is having an issue, I was charged'
pattern = 'order[^\d]*(\d*)'
matches = re.findall(pattern, chat3)
matches

#--------------------------------------------------------
def get_pattern_match(pattern, text):
    matches = re.findall(pattern, text)
    if matches:
        return matches[0]
    
get_pattern_match('order[^\d]*(\d*)' , chat1)

#-----------------------------------------------------
chat1='i am rushikesh and i am from ahmednagar - 414003'
chat2='pranit is from rahuri and his email is pranitborkar28@gmail.com'
chat3='akash is my roomate and his phone no is 9836710125'


def get_pattern_match(pattern,text):
    matches=re.findall(pattern,text)
    if matches:
        return matches[0]
    
get_pattern_match('[a-zA-Z0-9_]*@[a-zA-Z]*\.[a-z]*',chat1)
get_pattern_match('[a-zA-Z0-9_]*@[a-zA-Z]*\.[a-z]*',chat2)
get_pattern_match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*',chat3)

#---------------------------------------------------------------------


import re

pattern2='[a-zA-Z0-9]*@[a-zA-Z]*\.[a-z]*'
pattern3='\d{10}|\(\d{3}\)-\d{3}-\d{4}'
chat1='i am rushikesh and i am from ahmednagar - 414003'
chat2='pranit is from rahuri and his email is pranitborkar28@gmail.com'
chat3='akash is my roomate and his phone no is 9836710125'

def get_pattern_match(pattern,text):
    matches=re.findall(pattern,text)
    if matches:
        return matches[0]
    
 
    
########################################################################
text="""
Born	Elon Reeve Musk
June 28, 1971 (age 52)
Pretoria, Transvaal, South Africa
Citizenship	
South Africa
Canada
United States
Education	University of Pennsylvania (BA, BS)
Title	
Founder, CEO, and chief engineer of SpaceX
CEO and product architect of Tesla, Inc.
Owner, CTO and Executive Chairman of X (formerly Twitter)
President of the Musk Foundation
Founder of The Boring Company, X Corp., and xAI
Co-founder of Neuralink, OpenAI, Zip2, and X.com (part of PayPal)
Spouses	
Justine Wilson
​(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2012)​
​
​(m. 2013; div. 2016)​
Partners	
Grimes (2018–2021)[1]
Children	11[a][3]
Parents	
Errol Musk
Maye Musk
Relatives	
Kimbal Musk (brother)
Tosca Musk (sister)
Lyndon Rive (cousin)
Signature"""

    
get_pattern_match(r'age(\d+)', text)

get_pattern_match(r'Born(.*)\n' , text).strip()

get_pattern_match(r'Born.*\n(.*)\(age', text).strip()
       
###################################################

import re

text='''
Born	Dhirubhai Ambani
28 December 1932 (aged 69)
Chorwad, Junagadh State, British India
(present-day Gujarat, India)
Died	6 July 2002
Mumbai, Maharashtra, India
Citizenship	British India (1932–1947)
Dominion of India (1947–1950)
India (1950–2002)
Occupation	Businessman
Organization(s)	Reliance Industries
Reliance Capital
Reliance Infrastructure
Reliance Power
Spouse	Kokila Dhirubhai Ambani
​
​(m. 1955)​
Children	4, including Mukesh Ambani and Anil Ambani
Awards	Padma Vibhushan (2016) (posthumously)
'''
#pattrn6="Bron (.)*/n"
def get_pattern_match(pattern,text):
    matches=re.findall(pattern,text)
    if matches:
        return matches[0]
     
def newfun(text):
    aged=get_pattern_match('aged (\d+)', text)
    name=get_pattern_match('Born(.*)\n', text)
    birth=get_pattern_match('Born.*\n(.*)\(age', text)
    return{
        "aged":int(aged),
        "name":name.strip(),
        "birth":birth.strip()
        }
newfun(text)

#----------------------------------------------------------------

from PyPDF2 import PdfFileReader

from PyPDF2 import PdfReader

reader = PdfReader("E:/DATA SCIENCE 24/1-Python/matrix_basics.pdf")

print(len(reader.pages))

page=reader.pages[1]

text=page.extract_text()
print(text)

