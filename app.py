from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def index():
    try:
        with open("/app/data/info.txt", "r") as file:
            content = file.read()
    except FileNotFoundError:
        content = "Файл не найден. Создайте 'info.txt'."
    return render_template_string("<h1>Содержимое файла:</h1><pre>{{ content }}</pre>", content=content)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
