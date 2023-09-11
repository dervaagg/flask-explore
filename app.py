from flask import Flask, render_template, request

list_order = []

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
        
        list_order.append(request.form)

        return f'Terima kasih, {name}! Pesanan Anda untuk {quantity} {product} sudah kami terima.'
    
    return render_template('order_form.html')




@app.route('/order')
def orderPage():
    return render_template('listOrder.html', list_order=list_order)


if __name__ == '__main__':
    app.run()
