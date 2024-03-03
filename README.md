## Rewordify : Rephrasing Web Application 📝🔄<br>
# Overview<br>
The Sentence Rephrasing Web Application is a Flask-based web application designed to provide users with the ability to input a sentence and choose a rephrasing style. The application uses the NLTK library for basic synonym replacement, offering four rephrasing styles: Simple English, Academic English, Fluency, and Technical English.


# Implementation Details<br>

Text Processing: Input text is tokenized to individual words, and synonyms are identified using NLTK's WordNet corpus or pre-trained word embeddings models. 📝➡️🔤🔄<br>
Paraphrase Styles: Different styles of paraphrasing are implemented by adjusting synonym selection criteria. For example, simple paraphrasing selects basic synonyms, while academic paraphrasing prioritizes formal language. 🎨🔄📚<br>

# Features<br>
•	Web Interface: Users can interact with the application through a simple web interface.<br>
•	Synonym Replacement: The application utilizes the NLTK library to replace words in the input sentence with their synonyms based on the selected rephrasing style.<br>
•	Rephrasing Styles:<br>
•	Simple English: Uses basic synonyms suitable for simple language.<br>
•	Academic English: Focuses on more formal and academic synonyms.<br>
•	Fluency: Allows for a mix of synonyms to enhance language fluency.<br>
•	Technical English: Utilizes technical synonyms for a more specialized vocabulary.<br>
# Dependencies<br>
•	Flask: Web framework for Python.<br>
•	NLTK: Natural Language Toolkit for language processing.<br>
# Usage<br>
1.	Install dependencies: pip install Flask nltk  <br>
2.	Run the Flask application: python app.py<br>
3.	Access the application in a web browser at http://127.0.0.1:5000/.<br>
4.	Enter a sentence, choose a rephrasing style, and click the "Rephrase" button.<br>
# Future Enhancements<br>
•	Explore additional language processing libraries or algorithms for more advanced rephrasing capabilities.<br>
•	Implement user authentication and storage for rephrased sentences.<br>
•	Enhance the user interface for improved user experience.<br>
# Notes •	Ensure that the NLTK data is downloaded before running the application.






## output 

<img src="https://github.com/codeasarjun/paraphraser-/blob/main/img/rephrase1.png">
