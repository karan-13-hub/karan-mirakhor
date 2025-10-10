# 🚀 GitHub Pages Deployment Guide

This guide will help you deploy Karan Mirakhor's research portfolio to GitHub Pages.

## 📋 Prerequisites

- GitHub account
- Git installed on your system
- Terminal/Command line access

## 🎯 Quick Start (5 minutes)

### Step 1: Create GitHub Repository

1. Go to [GitHub.com](https://github.com) and sign in
2. Click the **"+"** button → **"New repository"**
3. **Repository name**: `karan-mirakhor.github.io` (replace with your username)
4. **Description**: "Research Portfolio - Karan Mirakhor"
5. Set to **Public**
6. **Don't** initialize with README (we already have files)
7. Click **"Create repository"**

### Step 2: Connect Local Repository

```bash
# Add your GitHub repository as remote origin
git remote add origin https://github.com/YOUR_USERNAME/karan-mirakhor.github.io.git

# Push to GitHub
git push -u origin main
```

### Step 3: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **"Settings"** tab
3. Scroll down to **"Pages"** section
4. Under **"Source"**, select **"Deploy from a branch"**
5. Choose **"main"** branch and **"/ (root)"** folder
6. Click **"Save"**

### Step 4: Access Your Portfolio

- **URL**: `https://YOUR_USERNAME.github.io`
- **Wait**: 2-5 minutes for deployment
- **Refresh**: Check if it's live

## 🔧 Alternative: Custom Repository Name

If you want a different repository name:

1. Create repository with any name (e.g., `portfolio`)
2. Follow steps above
3. Your URL will be: `https://YOUR_USERNAME.github.io/portfolio`

## 📁 Portfolio Versions

The repository includes **3 portfolio versions**:

### 1. Simple Portfolio (Default for GitHub Pages)
- **Location**: `/simple-portfolio/`
- **URL**: `https://YOUR_USERNAME.github.io/simple-portfolio/`
- **Features**: Pure HTML/CSS/JS, works everywhere

### 2. React Portfolio
- **Location**: `/react-portfolio/`
- **Features**: Next.js, Tailwind CSS, Framer Motion
- **Build**: `npm run build` (requires Node.js 12+)

### 3. Vue Portfolio
- **Location**: `/vue-portfolio/`
- **Features**: Vue 3, Vite, Tailwind CSS
- **Build**: `npm run build` (requires Node.js 14+)

## 🛠️ Customization

### Update Content
1. Edit files in `/content/` folder
2. For simple portfolio, edit `/simple-portfolio/index.html`
3. Commit and push changes:
   ```bash
   git add .
   git commit -m "Update portfolio content"
   git push
   ```

### Change Portfolio Version
1. Edit root `/index.html`
2. Change redirect URL from `./simple-portfolio/` to your preferred version
3. Commit and push

### Custom Domain
1. Add `CNAME` file to root directory
2. Add your domain name in the file
3. Configure DNS with your domain provider

## 🔄 Automated Deployment

The repository includes GitHub Actions for automatic deployment:

- **File**: `.github/workflows/deploy.yml`
- **Triggers**: Push to main branch
- **Action**: Automatically builds and deploys all versions

## 🐛 Troubleshooting

### Portfolio Not Loading
1. Check GitHub Pages settings
2. Ensure main branch is selected
3. Wait 5-10 minutes for propagation
4. Check repository Actions tab for errors

### Build Errors
1. Check Node.js version compatibility
2. Review package.json dependencies
3. Check GitHub Actions logs

### Custom Domain Issues
1. Verify CNAME file exists
2. Check DNS configuration
3. Wait for DNS propagation (up to 24 hours)

## 📞 Support

If you encounter issues:

1. Check GitHub Pages documentation
2. Review repository Actions tab
3. Check browser console for errors
4. Verify all files are committed and pushed

## 🎉 Success!

Once deployed, your portfolio will be available at:
- **Primary**: `https://YOUR_USERNAME.github.io`
- **Simple**: `https://YOUR_USERNAME.github.io/simple-portfolio/`
- **React**: `https://YOUR_USERNAME.github.io/react-portfolio/`
- **Vue**: `https://YOUR_USERNAME.github.io/vue-portfolio/`

Share your portfolio with the world! 🌍
