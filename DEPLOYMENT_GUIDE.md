# Career2Life Deployment Guide

This guide will walk you through deploying your Career2Life application to Vercel (frontend) and Render (backend) for free.

## Prerequisites

1. A GitHub account
2. A Vercel account (sign up at https://vercel.com)
3. A Render account (sign up at https://render.com)
4. Git installed on your machine

## Step 1: Prepare Your Repository

1. **Initialize Git (if not already done):**
   ```bash
   git init
   git add .
   git commit -m "Initial commit for deployment"
   ```

2. **Create a GitHub repository:**
   - Go to https://github.com/new
   - Create a new repository (e.g., "Career2Life")
   - **Don't** initialize with README (you already have one)

3. **Push your code to GitHub:**
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/Career2Life.git
   git branch -M main
   git push -u origin main
   ```

## Step 2: Deploy Backend to Render

1. **Log in to Render:** https://render.com

2. **Create a New Web Service:**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select the "Career2Life" repository

3. **Configure the service:**
   - **Name:** career2life-api
   - **Environment:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn api:app`
   - **Plan:** Free

4. **Add Environment Variables (if needed):**
   - Click "Advanced" → "Add Environment Variable"
   - Add any required variables

5. **Deploy:**
   - Click "Create Web Service"
   - Wait for the deployment to complete
   - Copy your API URL (e.g., `https://career2life-api.onrender.com`)

## Step 3: Update Frontend with Backend URL

1. **Update the environment file** with your Render API URL:
   - Open `src/environments/environment.prod.ts`
   - Replace `'https://your-backend.onrender.com'` with your actual Render URL

2. **Commit the changes:**
   ```bash
   git add .
   git commit -m "Update API URL for production"
   git push
   ```

## Step 4: Deploy Frontend to Vercel

1. **Log in to Vercel:** https://vercel.com

2. **Import your project:**
   - Click "Add New..." → "Project"
   - Import your GitHub repository "Career2Life"

3. **Configure the project:**
   - **Framework Preset:** Angular
   - **Build Command:** `npm run build`
   - **Output Directory:** `dist/landing/browser`
   - **Install Command:** `npm install`

4. **Deploy:**
   - Click "Deploy"
   - Wait for the deployment to complete
   - Your app will be live at a Vercel URL (e.g., `https://career2life.vercel.app`)

## Step 5: Configure Custom Domain (Optional)

### For Vercel:
1. Go to your project settings → Domains
2. Add your custom domain
3. Follow DNS configuration instructions

### For Render:
1. Go to your service settings → Custom Domain
2. Add your custom domain
3. Follow DNS configuration instructions

## Important Notes

### Render Free Plan Limitations:
- Services spin down after 15 minutes of inactivity
- First request after inactivity may take 30-50 seconds (cold start)
- 750 hours/month free (enough for one service running 24/7)

### Vercel Free Plan Limitations:
- 100 GB bandwidth/month
- Unlimited deployments
- Automatic HTTPS

## Troubleshooting

### Backend Issues:
1. Check Render logs: Dashboard → Your Service → Logs
2. Ensure all `.pkl` model files are committed to Git
3. Verify `requirements.txt` has all dependencies

### Frontend Issues:
1. Check Vercel logs: Dashboard → Your Project → Deployments → Click on deployment
2. Verify the API URL in `environment.prod.ts` is correct
3. Check browser console for CORS errors

### CORS Issues:
If you see CORS errors, verify that `flask-cors` is installed and configured in `api.py`.

## Automatic Deployments

Both Vercel and Render will automatically redeploy when you push changes to your main branch:

```bash
git add .
git commit -m "Your changes"
git push
```

## Environment Variables

If you need to add sensitive data (API keys, secrets):
- **Never commit them to Git**
- Add them in Render/Vercel dashboard under Environment Variables
- Use a `.env` file locally (already in `.gitignore`)

## Support

- Vercel Documentation: https://vercel.com/docs
- Render Documentation: https://render.com/docs
- Angular Deployment: https://angular.dev/tools/cli/deployment

---

**Need help?** Check the logs in both platforms for detailed error messages.
