from flask import Flask, jsonify


app = Flask(__name__)


books = [
	{
		'id': "0",
		'title': 'A Fire Upon the Deep',
		'author': 'Vernor Vinge',
		'first_sentence': 'The coldsleep itself was dreamless.',
		'year_published': '1992'
	},
	{
		'id': "1",
		'title': 'The Ones Who Walk Away From Omelas',
		'author': 'Ursula K. Le Guin',
		'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
		'published': '1973'
	},
	{
		'id': "2",
		'title': 'Dhalgren',
		'author': 'Samuel R. Delany',
		'first_sentence': 'to wound the autumnal city.',
		'published': '1975'
	}
]

@app.route("/", methods=["GET"])
def index():
    return "<h1>Simple Flask API</h1>"
    

@app.route("/api/v1/resources/books/all", methods=["GET"])
def get_all_books():
    return jsonify({'data' : books})
    

@app.route("/api/v1/resources/books/book/id=<book_id>", methods=["GET"])
def get_book(book_id):
    book = [book for book in books if book["id"] == book_id]
    if not book:
        return jsonify({'data':None})
    return jsonify({'data':book})
    
    
if __name__ == "__main__":
    app.run(debug=True)

