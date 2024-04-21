from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

# Bellekte veri saklamak için basit bir liste
items = []

# Ana Sayfa: Öğeleri listele
@app.route('/')
def home():
    return render_template_string('''
    <h1>Items List</h1>
    <ul>
        {% for item in items %}
        <li>{{ item }} <a href="/delete/{{ loop.index0 }}">Delete</a> <a href="/edit/{{ loop.index0 }}">Edit</a></li>
        {% endfor %}
    </ul>
    <a href="/add">Add New Item</a>
    ''', items=items)

# Öğe Ekleme Sayfası
@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        item = request.form['item']
        items.append(item)
        return redirect(url_for('home'))
    return render_template_string('''
    <h1>Add New Item</h1>
    <form method="post">
        <input type="text" name="item" placeholder="Enter item here">
        <input type="submit" value="Add">
    </form>
    <a href="/">Cancel</a>
    ''')

# Öğe Silme
@app.route('/delete/<int:index>')
def delete_item(index):
    items.pop(index)
    return redirect(url_for('home'))

# Öğe Düzenleme
@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit_item(index):
    if request.method == 'POST':
        items[index] = request.form['item']
        return redirect(url_for('home'))
    return render_template_string('''
    <h1>Edit Item</h1>
    <form method="post">
        <input type="text" name="item" value="{{ current_item }}">
        <input type="submit" value="Update">
    </form>
    <a href="/">Cancel</a>
    ''', current_item=items[index])

if __name__ == '__main__':
    app.run(debug=True)
