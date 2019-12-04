
from io import StringIO

from flask import *
# from project import db, invertedIndex
from app.forms import QueryForm, NewDocForm
from app.createindex import InvertedIndex, Database

# PDF Miner imports
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage


app_blueprint = Blueprint('app',__name__)

db = Database()
invertedIndex = InvertedIndex(db)

@app_blueprint.route('/', methods=['POST', 'GET'])
def landingPage():
    form = QueryForm()
    if form.validate_on_submit():
        query = form.query.data
        if query:
            query = query.lower()
            return redirect(url_for('app.resultPage', query=query, invertedIndex=invertedIndex))
    return render_template('index.html', form=form)


"""@app_blueprint.route('/loaddocs', methods=['GET', 'POST'])
def addNewPage():
    return render_template('loaddocs.html')
"""

@app_blueprint.route('/loaddocs', methods=['POST', 'GET'])
def loadNewDocPage():
    newDocForm2 = NewDocForm()
    if newDocForm2.validate_on_submit():
        document = newDocForm2.document.data
        if document:
            documents = []
            document = document.replace('\r', '').split('\n\n')
            for document in document:
                documents.append(document.lower())
            for eachDocument in documents:
                invertedIndex.index_document(eachDocument)
            return redirect(url_for('app.landingPage'))
    return render_template('loaddocs.html', form=newDocForm2)



@app_blueprint.route('/<query>/search', methods=['POST', 'GET'])
def resultPage(query):
    searchResults = []
    result = invertedIndex.lookup_query(query)
    if result[0]:
        for term in result[1].keys():
            for appearance in result[1][term]:
                document = db.get(appearance.docId)
                searchResults.append(document)
    else:
        print('No documents match your search')
    searchResults = list(set(searchResults))
    if searchResults:
        return render_template('search.html', searchResults=searchResults)
    else:
        return render_template('notfound.html')


@app_blueprint.route('/viewdocs', methods=['POST', 'GET'])
def viewAllDocs():
    searchResults = []
    for _, v in db.db.items():
        searchResults.append(v)
    searchResults = list(set(searchResults))
    if searchResults:
        return render_template('viewdocs.html', searchResults=searchResults)
    else:
        return render_template('notfound.html')

@app_blueprint.route('/erasedocs', methods=['POST', 'GET'])
def eraseAllDocs():
    db.db = dict()
    invertedIndex.index = dict()
    invertedIndex.db = db 
    invertedIndex.uniqueID = 0   
    return render_template('erasedocs.html')