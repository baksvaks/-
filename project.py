from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def sample_file_upload():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                             <link rel="stylesheet"
                             href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                             integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                             crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>увеличение</title>
                          </head>
                          <body>
                            <h1>Загрузите фотографию</h1>
                            <form class="login_form" method="post" enctype="multipart/form-data">
                                    <label for="photo">Приложите фотографию</label>
                                <div class="form-group">
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                </div>
                                <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        f = request.files['file']
        with open(f'static/img/{f.filename}', 'wb') as f1:
            f1.write(f.read())
        file = f"{url_for('static', filename='img/' + f.filename)}"
        return f"""<!doctype html>
                    <html lang='en'>
                        <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                            crossorigin="anonymous"> 
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}"/>
                            <title>увеличение</title>
                        </head>
                        <body>
                         <h1>Загрузите фотографию</h1>
                            <form class="login_form" method="post" enctype="multipart/form-data">
                                    <label for="photo">Приложите фотографию</label>
                                <div class="form-group">
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                </div>
                                <img src="/static/img/{f.filename}" width="420" height="10000"
                                alt="здесь должна быть картинка, но не нашлось">
                                <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                        </body>
                    </html>"""

if __name__ == "__main__":
    app.run(port=8080, host='127.0.0.1')