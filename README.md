Web app deployed on heroku: https://atapsearch.herokuapp.com/ (It crashes sometimes, it's a bit buggy)
TapSearch is a search engine in python. It can do the following:
   
1.  It takes in multiple paragraphs of text, assigns a unique ID To each paragraph and stores the words to paragraph mappings on an inverted index. This is similar to what elasticsearch does. This paragraph can also be referred to as a ‘document’

2.  Given a word to search for, it lists out the top 10 paragraphs in which the word is present
  
Tech Stack:
1. Flask
2. HTML & CSS

How to use:

1. Clone the project using git clone 

2. Install required dependencies using pip install -r requirements.txt

3. Navigate to the root directory

4. open terminal, there type : python3 app.py

5. open a web browser, type: localhost:5000 in the search bar.

6. Add a new document using add new 

7. Search for a word by going to the homepage and submitting the query in textbox

8. Delete all documents by clicking on the delete all button on the navigation bar
