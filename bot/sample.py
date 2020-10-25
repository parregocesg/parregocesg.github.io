from flask import Flask,render_template,request
from chatterbot import ChatBot
from chatterbot import ChatterBotCorpusTrainer


app= Flask(__name__) # nombre del modulo o el paquete
spa_bot=ChatBot("Chatterbot",storage_adapter="chatterbot.stprage.SQLStorageAdapted")
trainer = ChatterBotCorpusTrainer(spa_bot)
trainer.train("chatterbot.corpus.spanish")
trainer.train("datos/datos.yml")


@app.route('/')
def index():
    return render_template("index.html")  #ENVIAR A HTML

@app.route('/get')
def get_bot_response():
    userText=request.args.get("msg")  #tomar datos de la entrada
    return str(spa_bot.get_response(userText))


if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True)
