# Deploy Portfolio to GitHub Pages

## 🎯 Target URL
Your portfolio will be available at: **https://karan-13-hub.github.io/karan-mirakhor/**

## 📋 Step-by-Step Instructions

### Step 1: Create GitHub Repository
1. Go to https://github.com/new
2. Repository name: `karan-13-hub.github.io`
3. Description: "Karan Mirakhor - Research Portfolio"
4. Make it **Public**
5. **DO NOT** initialize with README, .gitignore, or license
6. Click **"Create repository"**

### Step 2: Update Remote URL
```bash
cd /home/km13/Documents/mirakhor_karan_portfolio
git remote set-url origin https://github.com/karan-13-hub/karan-13-hub.github.io.git
```

### Step 3: Push to GitHub
```bash
git add .
git commit -m "Deploy portfolio to GitHub Pages"
git push -u origin main
```

### Step 4: Enable GitHub Pages
1. Go to your repository: https://github.com/karan-13-hub/karan-13-hub.github.io
2. Click **"Settings"** tab
3. Scroll to **"Pages"** in left sidebar
4. Under **"Source"**, select **"Deploy from a branch"**
5. Select **"main"** branch and **"/ (root)"** folder
6. Click **"Save"**

### Step 5: Wait for Deployment
- GitHub will build and deploy your site
- This usually takes 2-5 minutes
- You'll see a green checkmark when ready

### Step 6: Access Your Portfolio
Visit: **https://karan-13-hub.github.io/**

## 🔄 Alternative: Use Current Repository

If you prefer to keep the current repository name (`karan-mirakhor`), your portfolio will be available at:
**https://karan-13-hub.github.io/karan-mirakhor/**

To use this option:
1. Keep the current remote URL
2. Enable GitHub Pages in repository settings
3. Select "Deploy from a branch" → "main" → "/ (root)"

## 🚀 Quick Deploy Script

Run this command to automate the process:
```bash
./deploy-to-github-pages.sh
```

## ✅ Verification Checklist

- [ ] Repository created with correct name
- [ ] Code pushed to GitHub
- [ ] GitHub Pages enabled
- [ ] Site loads at target URL
- [ ] All content displays correctly
- [ ] Mobile responsive design works

## 🆘 Troubleshooting

### If deployment fails:
1. Check repository name is exactly `karan-13-hub.github.io`
2. Ensure repository is public
3. Verify GitHub Pages is enabled
4. Check Actions tab for build errors

### If site doesn't load:
1. Wait 5-10 minutes for DNS propagation
2. Clear browser cache
3. Check if files are in the root directory
4. Verify `index.html` exists in root

## 📞 Need Help?

The deployment process should take about 5-10 minutes total. If you encounter any issues, check the GitHub repository settings and ensure all steps were followed correctly.
