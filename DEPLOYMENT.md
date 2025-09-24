# Deployment Guide - Business Attrition Dashboard

## Project Structure
```
Business_Attrition/
├── app.py                    # Original Flask app (untuk Heroku, Fly.io, dll)
├── app_vercel.py            # Flask app khusus untuk Vercel
├── requirements.txt         # Dependencies lengkap (untuk platform lain)
├── requirements_vercel.txt  # Dependencies minimal (untuk Vercel)
├── vercel.json             # Konfigurasi Vercel
├── .vercelignore           # File yang diabaikan Vercel
└── templates/              # HTML templates
```

## Deployment Options

### 1. Vercel (Serverless)
**Files used:**
- `app_vercel.py`
- `requirements_vercel.txt`
- `vercel.json`

**Steps:**
1. Push ke GitHub repository
2. Connect repository ke Vercel
3. Vercel akan auto-detect dan deploy

**Advantages:**
- Gratis dengan limits generous
- Auto-scaling
- CDN global built-in
- HTTPS otomatis

### 2. Heroku, Fly.io, Koyeb (Container/Traditional)
**Files used:**
- `app.py`
- `requirements.txt`
- `Procfile` / `fly.toml` / `koyeb.yaml`

**Advantages:**
- Full server control
- Persistent connections
- Background tasks support

## Environment Variables
```
SECRET_KEY=your-secret-key-here
FLASK_ENV=production
```

## Testing Locally

### For Vercel version:
```bash
python app_vercel.py
```

### For traditional version:
```bash
python app.py
```

## URLs
- Home: `/`
- Dashboard: `/dashboard`
- About: `/about`
- Health Check (Vercel only): `/health`