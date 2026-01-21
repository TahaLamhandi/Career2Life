# 🚀 Deployment Checklist for Career2Life

Use this checklist to ensure your project is ready for deployment to Vercel and Render.

## ✅ Pre-Deployment Checklist

### 1. Git & GitHub Setup
- [ ] Git repository initialized (`git init`)
- [ ] All files committed locally
- [ ] GitHub repository created
- [ ] Local repo connected to GitHub (`git remote add origin ...`)
- [ ] Code pushed to GitHub (`git push -u origin main`)

### 2. Backend Configuration (Render)
- [ ] `requirements.txt` includes all dependencies (including `gunicorn`)
- [ ] `render.yaml` configuration file created
- [ ] Model files (*.pkl) are committed to git
- [ ] `api.py` has CORS enabled
- [ ] Flask app runs locally without errors

### 3. Frontend Configuration (Vercel)
- [ ] `vercel.json` configuration file created
- [ ] `src/environments/environment.ts` created (for local dev)
- [ ] `src/environments/environment.prod.ts` exists
- [ ] Environment imports added to all API components
- [ ] Angular build completes successfully (`npm run build`)
- [ ] `angular.json` has file replacement configured

### 4. Environment Variables
- [ ] API URL in `environment.ts` points to `http://localhost:5000`
- [ ] API URL in `environment.prod.ts` ready for Render URL update

## 📋 Deployment Steps

### Step 1: Deploy Backend to Render ⚙️
1. [ ] Sign up/login at https://render.com
2. [ ] Create new "Web Service"
3. [ ] Connect GitHub repository
4. [ ] Configure:
   - Environment: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn api:app`
   - Free plan selected
5. [ ] Deploy and wait for completion
6. [ ] Copy your Render API URL (e.g., `https://career2life-api.onrender.com`)
7. [ ] Test the API: Visit `https://YOUR-URL.onrender.com/` (should show API info)

### Step 2: Update Frontend with Backend URL 🔗
1. [ ] Open `src/environments/environment.prod.ts`
2. [ ] Replace `'https://your-backend.onrender.com'` with your actual Render URL
3. [ ] Save the file
4. [ ] Commit: `git add . && git commit -m "Update production API URL"`
5. [ ] Push: `git push`

### Step 3: Deploy Frontend to Vercel 🌐
1. [ ] Sign up/login at https://vercel.com
2. [ ] Click "Add New..." → "Project"
3. [ ] Import your GitHub repository
4. [ ] Configure:
   - Framework Preset: Angular
   - Build Command: `npm run build`
   - Output Directory: `dist/landing/browser`
5. [ ] Click "Deploy"
6. [ ] Wait for deployment to complete
7. [ ] Visit your live site!

## 🧪 Post-Deployment Testing

Test all features on your live site:
- [ ] Salary Prediction form works
- [ ] Car Affordability checker works
- [ ] House Price Estimator works
- [ ] No CORS errors in browser console
- [ ] All pages load correctly
- [ ] Theme switching works
- [ ] Mobile responsiveness looks good

## 🔄 Future Updates

When you make changes:
1. [ ] Make your code changes
2. [ ] Test locally
3. [ ] Commit: `git add . && git commit -m "Your message"`
4. [ ] Push: `git push`
5. [ ] Both Vercel and Render will automatically redeploy

Or use the helper script:
```bash
./deploy.ps1
```

## 🆘 Troubleshooting

### Backend Issues:
- Check Render logs in dashboard
- Verify all model files are in repository
- Ensure `gunicorn` is in requirements.txt
- Test API endpoints manually

### Frontend Issues:
- Check Vercel deployment logs
- Verify environment.prod.ts has correct API URL
- Check browser console for errors
- Ensure build succeeds locally

### CORS Issues:
- Verify `flask-cors` is installed
- Check CORS is enabled in `api.py`
- Ensure API URL in environment.prod.ts is correct

## 📚 Resources

- **Vercel Docs**: https://vercel.com/docs
- **Render Docs**: https://render.com/docs
- **Angular Deployment**: https://angular.dev/tools/cli/deployment
- **Project Deployment Guide**: See DEPLOYMENT_GUIDE.md

---

**Ready to deploy?** Start with Step 1 above! 🚀
