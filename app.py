from flask import Flask, render_template, request

app = Flask(__FormOrder__)

@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        # Dapatkan data dari formulir
        name = request.form.get('name')
        email = request.form.get('email')
        product = request.form.get('product')
        quantity = request.form.get('quantity')

        return f'Terima kasih, {name}! Pesanan Anda untuk {quantity} {product} sudah kami terima.'
    
    return render_template('order_form.html')

if __name__ == '__main__':
    app.run()
