from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        # Dapatkan data dari formulir
        name = request.form.get('name')
        email = request.form.get('email')
        product = request.form.get('product')
        quantity = request.form.get('quantity')

        return f'Terima kasih, {name}! Pesanan Anda untuk {quantity} {product} sudah kami terima.'
    
    return render_template('order_form.html')


list_order = [
    {
        "nama": "Roy",
        "email": 'a@a',
        "produk": "Nasgor",
        "jumlah": 5
    },
    {
        "nama": "Roy2",
        "email": 'a@33a',
        "produk": "N323asgor",
        "jumlah": 3
    },
    {
        "nama": "Roy3",
        "email": 'a@add',
        "produk": "Nasgasdsador",
        "jumlah": 1
    },
]

@app.route('/order')
def orderPage():
    return render_template('listOrder.html', list_order=list_order)


if __name__ == '__main__':
    app.run()
