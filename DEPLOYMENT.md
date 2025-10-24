# 🚀 Deployment Guide for Emotion Detector

## Backend Deployment (Vercel)

### 1. Environment Variables Setup in Vercel

Add these environment variables in your Vercel project:

- `BASE44_API_URL` = `https://app.base44.com/api/apps/YOUR_APP_ID_HERE`
- `BASE44_API_KEY` = `your_actual_base44_api_key`

### 2. Get Your Base44 API Details

1. Go to https://app.base44.com/
2. Open your Emotion Detector app
3. Find your **App ID** and **API Key**
4. Replace in environment variables

### 3. Deploy to Vercel

\`\`\`bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel --prod
\`\`\`

## Frontend Deployment

### 1. Update API URLs

Make sure your frontend uses the deployed backend URL:

\`\`\`javascript
// In Scanner.jsx
const API_BASE_URL = "https://your-app-name.vercel.app";
\`\`\`

### 2. Push to GitHub

\`\`\`bash
git add .
git commit -m "deploy: ready for production"
git push origin main
\`\`\`

### 3. Connect GitHub to Vercel

1. Go to vercel.com
2. Import your GitHub repository
3. Add environment variables
4. Deploy

## Security Notes

- ✅ Never commit real API keys to GitHub
- ✅ Use .env.local for development
- ✅ Use Vercel environment variables for production
- ✅ .gitignore protects your local environment files
