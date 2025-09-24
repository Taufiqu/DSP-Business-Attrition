from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'vercel-secret-key-business-attrition')

# Vercel Configuration - Simplified
class VercelConfig:
    DEBUG = False  # Always False for production
    # Vercel handles PORT automatically, no need to specify

app.config.from_object(VercelConfig)

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
        'platform': 'Vercel Serverless',
        'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })

@app.route('/health')
def health():
    """Health check endpoint for Vercel"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'platform': 'vercel'
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

# Vercel serverless function handler
# This is important for Vercel deployment
if __name__ == '__main__':
    app.run(debug=False)