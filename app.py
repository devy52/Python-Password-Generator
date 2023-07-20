from flask import Flask, render_template, request
import random as rd
import string as st

def gen_pass(length,numbers=True,special_Characters=True):
    letters=st.ascii_letters
    special=st.punctuation
    digits=st.digits

    characters=letters
    if numbers:
        characters +=digits
    if special_Characters:
        characters+=special

    pwd=""
    meet_criteria=False
    has_number=False
    has_special=False

    while not meet_criteria or len(pwd)<length:
        new_char=rd.choice(characters)
        pwd+=new_char

        if new_char in digits:
            has_number=True
        elif new_char in special:
            has_special=True

        meet_criteria=True
        if numbers:
            meet_criteria=has_number
        if special_Characters:
            meet_criteria=meet_criteria and has_special

    if (len(pwd) > length):
        pwd=pwd[:length]

    return pwd

app = Flask(__name__, static_url_path='/static')

@app.route('/', methods=['GET', 'POST'])
def password_generator():
    if request.method == 'POST':
        length = int(request.form['length'])
        has_number = request.form.get('numbers') == 'on'
        has_special = request.form.get('special') == 'on'
        password = gen_pass(length, has_number, has_special)
        return render_template('app.html', password=password)
    return render_template('app.html')

if __name__ == '__main__':
    app.run(debug=True)
