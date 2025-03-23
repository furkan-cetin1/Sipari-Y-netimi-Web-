from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('urunler.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS urunler (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            isim TEXT NOT NULL,
            fiyat REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/urun-ekle', methods=['POST'])
def urun_ekle():
    data = request.get_json()
    isim = data['isim']
    fiyat = data['fiyat']

    conn = sqlite3.connect('urunler.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO urunler (isim, fiyat) VALUES (?, ?)', (isim, fiyat))
    conn.commit()
    conn.close()

    return jsonify({'status': 'success', 'message': 'Ürün başarıyla kaydedildi!'})

@app.route('/urunler')
def urunleri_goster():
    conn = sqlite3.connect('urunler.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, isim, fiyat FROM urunler')
    urunler = cursor.fetchall()
    conn.close()

    return render_template('urunler.html', urunler=urunler)

@app.route('/urun-sil/<int:id>', methods=['DELETE'])
def urun_sil(id):
    conn = sqlite3.connect('urunler.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM urunler WHERE id=?', (id,))
    conn.commit()
    conn.close()

    return jsonify({'status':'success'})

@app.route('/urun-duzenle/<int:id>', methods=['POST'])
def urun_duzenle(id):
    data = request.get_json()
    isim = data['isim']
    fiyat = data['fiyat']

    conn = sqlite3.connect('urunler.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE urunler SET isim=?, fiyat=? WHERE id=?', (isim, fiyat, id))
    conn.commit()
    conn.close()

    return jsonify({'status':'success'})

@app.route('/urunlerimiz')
def urunlerimiz():
    conn = sqlite3.connect('urunler.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, isim, fiyat FROM urunler')
    urunler = cursor.fetchall()
    conn.close()

    return render_template('urunlerimiz.html', urunler=urunler)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
