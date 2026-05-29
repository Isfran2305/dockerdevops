from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Página Flask</title>

    <style>
        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
            font-family: Arial, sans-serif;
        }

        body{
            height:100vh;
            display:flex;
            justify-content:center;
            align-items:center;
            background: linear-gradient(135deg, #0f172a, #1e293b, #334155);
            overflow:hidden;
        }

        .card{
            width:420px;
            padding:40px;
            border-radius:25px;
            background: rgba(255,255,255,0.1);
            backdrop-filter: blur(15px);
            border:1px solid rgba(255,255,255,0.2);
            text-align:center;
            color:white;
            box-shadow:0 10px 40px rgba(0,0,0,0.4);
            animation: aparecer 1s ease;
        }

        h1{
            font-size:42px;
            margin-bottom:15px;
            background: linear-gradient(90deg,#38bdf8,#818cf8);
            -webkit-background-clip:text;
            -webkit-text-fill-color:transparent;
        }

        p{
            font-size:18px;
            opacity:0.9;
            margin-bottom:30px;
        }

        .btn{
            display:inline-block;
            padding:14px 28px;
            border-radius:12px;
            text-decoration:none;
            color:white;
            background: linear-gradient(90deg,#3b82f6,#8b5cf6);
            transition:0.3s;
            font-weight:bold;
        }

        .btn:hover{
            transform:scale(1.08);
            box-shadow:0 0 20px rgba(139,92,246,0.6);
        }

        .circulo{
            position:absolute;
            border-radius:50%;
            filter: blur(60px);
            opacity:0.4;
        }

        .c1{
            width:300px;
            height:300px;
            background:#3b82f6;
            top:-100px;
            left:-100px;
        }

        .c2{
            width:250px;
            height:250px;
            background:#8b5cf6;
            bottom:-80px;
            right:-80px;
        }

        @keyframes aparecer{
            from{
                opacity:0;
                transform:translateY(30px);
            }
            to{
                opacity:1;
                transform:translateY(0);
            }
        }
    </style>
</head>

<body>

    <div class="circulo c1"></div>
    <div class="circulo c2"></div>

    <div class="card">
        <h1>Flask App</h1>
        <p>
            Página moderna creada con Flask + Python
            en un solo archivo.
        </p>

        <a href="#" class="btn">Explorar</a>
    </div>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)