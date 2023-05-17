from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def test_index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        favorite_movie = request.form['favorite_movie']
        
        test_output = f'Name: {name}<br><br>Email: {email}<br><br>Favorite Movie: {favorite_movie}'
        
        return '''
        <html>
        <head>
            <style>
                .center {{
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    text-align: center;
                }}
            </style>
        </head>
        <body>
            <div class="center">
                <div>
                    {output}
                </div>
            </div>
        </body>
        </html>
        '''.format_map({'output': output})
    
    return '''
        <html>
        <head>
            <style>
                .center {{
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    text-align: center;
                }}
            </style>
        </head>
        <body>
            <div class="center">
                <form method="POST">
                    <input type="text" name="name" placeholder="Enter your name"><br>
                    <input type="email" name="email" placeholder="Enter your email address"><br>
                    <input type="text" name="favorite_movie" placeholder="What's your favorite movie series"><br>
                    <input type="submit" value="Submit">
                </form>
            </div>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
