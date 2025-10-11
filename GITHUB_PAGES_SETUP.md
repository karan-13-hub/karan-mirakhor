# GitHub Pages Setup Instructions

## 🔧 **Required Repository Settings**

To complete the GitHub Pages deployment, you need to configure the repository settings:

### **Step 1: Create New Repository**
1. Go to https://github.com/new
2. Create a new repository named **`karan-mirakhor.github.io`**
3. Make sure it's under your **personal account** (not an organization)
4. Initialize with README (optional)
5. Click **"Create repository"**

### **Step 2: Push Code to New Repository**
1. Clone the new repository locally:
   ```bash
   git clone https://github.com/karan-mirakhor/karan-mirakhor.github.io.git
   ```
2. Copy all files from this project to the new repository
3. Push to the new repository:
   ```bash
   git add .
   git commit -m "Initial portfolio setup"
   git push origin main
   ```

### **Step 3: Enable GitHub Pages**
1. Go to your new repository: https://github.com/karan-mirakhor/karan-mirakhor.github.io
2. Click on **"Settings"** tab (at the top of the repository)
3. Scroll down to **"Pages"** section in the left sidebar
4. Under **"Source"**, select **"GitHub Actions"**
5. Click **"Save"** to confirm

### **Step 4: Verify Workflow Permissions**
1. In the same **"Settings"** tab
2. Go to **"Actions"** → **"General"** in the left sidebar
3. Scroll down to **"Workflow permissions"**
4. Select **"Read and write permissions"**
5. Check **"Allow GitHub Actions to create and approve pull requests"**
6. Click **"Save"**

### **Step 5: Check Deployment Status**
1. Go to the **"Actions"** tab in your repository
2. Look for **"Deploy Portfolio to GitHub Pages"** workflow
3. Click on it to see the deployment progress
4. Wait for it to complete (should take 3-5 minutes)

## 🌐 **Your Portfolio URL**
Once deployment is complete, your portfolio will be available at:
```
https://karan-mirakhor.github.io/
```

## 🔄 **What the New Workflow Does**

### **Updated GitHub Actions Workflow:**
- ✅ Uses official GitHub Pages actions (more reliable)
- ✅ Proper permissions for deployment
- ✅ Static export with Next.js
- ✅ Automatic deployment on every push to `main`

### **Key Changes Made:**
1. **Permissions**: Added `pages: write` and `id-token: write`
2. **Actions**: Updated to use `actions/deploy-pages@v4`
3. **Next.js Config**: Added `output: 'export'` for static generation
4. **Output Directory**: Configured to use `out` directory

## 🚨 **If Deployment Still Fails**

### **Check These Common Issues:**
1. **Repository Name**: Ensure it's exactly `karan-mirakhor.github.io`
2. **Branch**: Make sure you're pushing to `main` branch
3. **Permissions**: Verify GitHub Pages is enabled with GitHub Actions source
4. **Workflow**: Check the Actions tab for any error messages

### **Manual Deployment (Alternative):**
If the automatic deployment continues to fail, you can deploy manually:

```bash
cd react-portfolio
npm run build
# The built files will be in the 'out' directory
# You can then upload these files to any static hosting service
```

## 📊 **Expected Timeline**
- **Build Time**: 2-3 minutes
- **Deploy Time**: 1-2 minutes
- **Total**: 3-5 minutes from push

## ✅ **Success Indicators**
- ✅ Workflow shows green checkmark in Actions tab
- ✅ Portfolio loads at the GitHub Pages URL
- ✅ All content displays correctly
- ✅ Responsive design works on mobile/desktop

## 🔄 **Future Updates**
After initial setup, updating your portfolio is simple:
1. Edit markdown files in `content/` directory
2. Commit and push changes to `main` branch
3. GitHub Actions automatically rebuilds and deploys
4. Changes go live in 3-5 minutes

---

**Need Help?** Check the GitHub Actions logs in the Actions tab for detailed error messages.
