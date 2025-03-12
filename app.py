from flask import Flask, render_template_string

app = Flask(__name__)

# HTML template with inline CSS and JavaScript
html = """
<!DOCTYPE html>
<html>
<head>
    <title>Hello World</title>
    <style>
        body {
            background-color: white;
            transition: background-color 0.5s;
            font-family: Arial, sans-serif;
            text-align: center;
            padding-top: 50px;
        }
        .button {
            padding: 10px 20px;
            font-size: 16px;
            margin: 5px;
            border: none;
            cursor: pointer;
        }
        .green { background-color: green; color: white; }
        .yellow { background-color: yellow; color: black; }
        .red { background-color: red; color: white; }
    </style>
</head>
<body>
    <h1>Hello, World!</h1>
    <button class="button green" onclick="changeColor('green')">Green</button>
    <button class="button yellow" onclick="changeColor('yellow')">Yellow</button>
    <button class="button red" onclick="changeColor('red')">Red</button>

    <script>
        function changeColor(color) {
            document.body.style.backgroundColor = color;
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
