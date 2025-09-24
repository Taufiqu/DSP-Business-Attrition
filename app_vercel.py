from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime

# Create Flask app with explicit template and static folder paths
app = Flask(__name__, 
           template_folder='templates', 
           static_folder='static')
app.secret_key = os.environ.get('SECRET_KEY', 'vercel-secret-key-business-attrition')

# Vercel Configuration - Simplified
app.config.update(
    DEBUG=False,
    TESTING=False,
    SECRET_KEY=os.environ.get('SECRET_KEY', 'vercel-secret-key-business-attrition'),
    # Disable unnecessary features for serverless
    SEND_FILE_MAX_AGE_DEFAULT=0,
)

@app.route('/')
def home():
    """Halaman utama aplikasi"""
    try:
        return render_template('home.html')
    except Exception as e:
        return jsonify({'error': 'Template not found', 'message': str(e)}), 500

@app.route('/dashboard')
def dashboard():
    """Halaman dashboard dengan embed Google Looker Studio"""
    try:
        return render_template('dashboard_view.html')
    except Exception as e:
        return jsonify({'error': 'Dashboard template not found', 'message': str(e)}), 500

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
    try:
        return render_template('base.html', 
                             title='Page Not Found', 
                             error_message='Halaman yang Anda cari tidak ditemukan.'), 404
    except:
        return jsonify({'error': '404 Not Found', 'message': 'Page not found'}), 404

@app.errorhandler(500)
def internal_server_error(e):
    """Handler untuk error 500"""
    try:
        return render_template('base.html', 
                             title='Server Error', 
                             error_message='Terjadi kesalahan pada server.'), 500
    except:
        return jsonify({'error': '500 Internal Server Error', 'message': str(e)}), 500

# Add simple route for testing
@app.route('/test')
def test():
    """Simple test endpoint"""
    return jsonify({
        'status': 'success',
        'message': 'Vercel deployment is working!',
        'timestamp': datetime.now().isoformat()
    })

# Export app for Vercel
# This is the crucial part for Vercel serverless functions
app = app
if __name__ == '__main__':
    app.run(debug=False)