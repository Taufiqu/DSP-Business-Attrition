from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key-here')

# Configuration
class Config:
    DEBUG = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    PORT = int(os.environ.get('PORT', 5000))
    HOST = os.environ.get('HOST', '0.0.0.0')

app.config.from_object(Config)

@app.route('/')
def home():
    """Halaman utama aplikasi"""
    return render_template('home.html')

@app.route('/dashboard')
def dashboard():
    """Halaman dashboard dengan embed Google Looker Studio"""
    return render_template('dashboard_view.html')

@app.route('/about')
def about():
    """Halaman informasi tentang dashboard"""
    return jsonify({
        'title': 'Business Attrition Dashboard',
        'description': 'Dashboard untuk analisis Business Attrition menggunakan Google Looker Studio',
        'version': '1.0.0',
        'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })

@app.errorhandler(404)
def page_not_found(e):
    """Handler untuk error 404"""
    return render_template('base.html', 
                         title='Page Not Found', 
                         error_message='Halaman yang Anda cari tidak ditemukan.'), 404

@app.errorhandler(500)
def internal_server_error(e):
    """Handler untuk error 500"""
    return render_template('base.html', 
                         title='Server Error', 
                         error_message='Terjadi kesalahan pada server.'), 500

if __name__ == '__main__':
    app.run(
        host=Config.HOST,
        port=Config.PORT,
        debug=Config.DEBUG
    )