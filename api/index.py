from flask import Flask, render_template, jsonify
import os
from datetime import datetime

app = Flask(__name__, 
           template_folder='../templates', 
           static_folder='../static')

app.config.update(
    DEBUG=False,
    SECRET_KEY=os.environ.get('SECRET_KEY', 'vercel-secret-key')
)

@app.route('/')
def home():
    """Halaman utama aplikasi"""
    try:
        return render_template('home.html')
    except Exception as e:
        return jsonify({
            'error': 'Template error',
            'message': str(e),
            'templates_path': app.template_folder
        }), 500

@app.route('/dashboard')
def dashboard():
    """Halaman dashboard dengan embed Google Looker Studio"""
    try:
        return render_template('dashboard_view.html')
    except Exception as e:
        return jsonify({
            'error': 'Dashboard template error',
            'message': str(e)
        }), 500

@app.route('/about')
def about():
    """API endpoint tentang dashboard"""
    return jsonify({
        'title': 'Business Attrition Dashboard',
        'description': 'Dashboard untuk analisis Business Attrition menggunakan Google Looker Studio',
        'version': '1.0.0',
        'platform': 'Vercel Serverless',
        'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    })

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'platform': 'vercel',
        'templates_available': os.path.exists('../templates'),
        'static_available': os.path.exists('../static')
    })

@app.route('/test')
def test():
    """Test endpoint"""
    return jsonify({
        'message': 'Hello from Vercel!',
        'timestamp': datetime.now().isoformat(),
        'working': True
    })

@app.route('/debug')
def debug():
    """Debug endpoint to check file structure"""
    import glob
    import sys
    
    return jsonify({
        'current_working_dir': os.getcwd(),
        'templates_folder': app.template_folder,
        'static_folder': app.static_folder,
        'templates_exists': os.path.exists(app.template_folder),
        'static_exists': os.path.exists(app.static_folder),
        'template_files': glob.glob(os.path.join(app.template_folder, '*.html')) if os.path.exists(app.template_folder) else [],
        'python_version': sys.version,
        'flask_version': '3.0.0'
    })

@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Page not found', 'status': 404}), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({
        'error': 'Internal server error', 
        'status': 500,
        'details': str(e)
    }), 500

# This is required for Vercel
if __name__ == '__main__':
    app.run()