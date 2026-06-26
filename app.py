from flask import Flask, render_template, request, redirect, url_for, flash
from models import Mahasiswa
import file_handler as fh
import algorithms as algo

app = Flask(__name__)
app.secret_key = "kunci_rahasia_untuk_flash_message" # Diperlukan untuk notifikasi error/sukses

@app.route('/')
def dashboard():
    data = fh.muat_data()
    # Fitur Pengurutan dari URL (contoh: /?sort=ipk)
    sort_by = request.args.get('sort')
    if sort_by == 'nim':
        data = algo.insertion_sort_nim(data)
    elif sort_by == 'ipk':
        data = algo.bubble_sort_ipk(data)
        
    return render_template('dashboard.html', mahasiswa=data)

@app.route('/tambah', methods=['GET', 'POST'])
def tambah():
    if request.method == 'POST':
        nim = request.form['nim']
        nama = request.form['nama']
        jurusan = request.form['jurusan']
        ipk = request.form['ipk']
        
        try:
            Mahasiswa.validasi_nim(nim) # Validasi Regex
            mhs_baru = Mahasiswa(nim, nama, jurusan, ipk)
            
            data = fh.muat_data()
            # Cek apakah NIM sudah ada
            if any(d['nim'] == nim for d in data):
                flash("NIM sudah terdaftar!", "error")
                return redirect(url_for('tambah'))
                
            data.append(mhs_baru.to_dict())
            fh.simpan_data(data)
            flash("Data berhasil ditambahkan!", "sukses")
            return redirect(url_for('dashboard'))
            
        except ValueError as e: # Tangkap error dari class
            flash(str(e), "error")
            
    return render_template('tambah.html')

@app.route('/hapus/<nim>')
def hapus(nim):
    data = fh.muat_data()
    data = [d for d in data if d['nim'] != nim]
    fh.simpan_data(data)
    flash("Data berhasil dihapus!", "sukses")
    return redirect(url_for('dashboard'))

@app.route('/cari', methods=['GET'])
def cari():
    keyword = request.args.get('q', '')
    metode = request.args.get('metode', 'linear')
    data = fh.muat_data()
    
    if keyword:
        if metode == 'binary':
            hasil = algo.binary_search_nim(data, keyword)
        else:
            hasil = algo.linear_search_nama(data, keyword)
    else:
        hasil = []
        
    return render_template('cari.html', mahasiswa=hasil, keyword=keyword)

if __name__ == '__main__':
    app.run(debug=True)