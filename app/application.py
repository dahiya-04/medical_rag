from flask import Flask,render_template,request,redirect,url_for,session
from app.components.retriever import create_qa_chain
from dotenv import load_dotenv
import os

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

app = Flask(__name__)
app.secret_key = os.urandom(24) 

from markupsafe import Markup

def nl2br(value):
    """Convert newlines in the input text to HTML line breaks."""
    return Markup(value.replace("\n", "<br>\n"))

app.jinja_env.filters['nl2br'] = nl2br

@app.route('/',methods=['GET','POST'])
def index():
    """Handle the main page of the application, processing user input and generating responses."""
    if "messages" not in session:
        session["messages"] = []
    if request.method == "POST":
        user_input = request.form.get("prompt")
        if user_input:
            messages = session["messages"]
            messages.append({"role": "user", "content": user_input})
            session["messages"] = messages
            try:
                qa_chain = create_qa_chain()
                response=qa_chain.invoke({"query":user_input})
                result = response.get("result", "Sorry, I couldn't find an answer to your question.")
                messages.append({"role": "assistant", "content": result})
                session["messages"] = messages
            except Exception as e:
                error_message = f"An error occurred while processing your request: {str(e)}"
                messages.append({"role": "assistant", "content": error_message})
                return render_template('index.html', messages=session.get("messages", []))
        return redirect(url_for('index'))
    return render_template('index.html', messages=session.get("messages", []))  

@app.route('/clear')

def clear():
    """Handle the route for clearing the conversation history."""
    session.pop("messages", None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=False,use_reloader=False)