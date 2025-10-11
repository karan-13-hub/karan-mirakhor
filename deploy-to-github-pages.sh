#!/bin/bash

echo "🚀 Deploying Portfolio to GitHub Pages..."
echo "Target URL: https://karan-13-hub.github.io/"
echo ""

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "❌ Git repository not initialized. Please run 'git init' first."
    exit 1
fi

# Update remote URL to GitHub Pages repository
echo "🔗 Updating remote URL to GitHub Pages repository..."
git remote set-url origin https://github.com/karan-13-hub/karan-13-hub.github.io.git

# Add all files
echo "📁 Adding files to git..."
git add .

# Commit changes
echo "💾 Committing changes..."
git commit -m "Deploy portfolio to GitHub Pages - $(date)"

# Push to main branch
echo "🚀 Pushing to GitHub..."
git push -u origin main

echo ""
echo "✅ Code pushed to GitHub!"
echo ""
echo "📋 Next steps:"
echo "   1. Go to https://github.com/karan-13-hub/karan-13-hub.github.io"
echo "   2. Click 'Settings' tab"
echo "   3. Scroll to 'Pages' in left sidebar"
echo "   4. Under 'Source', select 'Deploy from a branch'"
echo "   5. Select 'main' branch and '/ (root)' folder"
echo "   6. Click 'Save'"
echo ""
echo "🌐 Your portfolio will be available at:"
echo "   https://karan-13-hub.github.io/"
echo ""
echo "⏱️  Deployment usually takes 2-5 minutes"
echo "🎉 Check back in a few minutes to see your live portfolio!"
