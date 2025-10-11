#!/bin/bash

echo "🚀 Deploying Portfolio to GitHub Pages..."

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "❌ Git repository not initialized. Please run 'git init' first."
    exit 1
fi

# Add all files
echo "📁 Adding files to git..."
git add .

# Commit changes
echo "💾 Committing changes..."
git commit -m "Deploy portfolio to GitHub Pages - $(date)"

# Check if remote origin exists
if ! git remote get-url origin > /dev/null 2>&1; then
    echo "⚠️  No remote origin found. Please add your GitHub repository:"
    echo "   git remote add origin https://github.com/karan-mirakhor/karan-mirakhor.github.io.git"
    echo ""
    echo "📝 To create a new repository on GitHub:"
    echo "   1. Go to https://github.com/new"
    echo "   2. Name it 'karan-mirakhor.github.io' for automatic GitHub Pages"
    echo "   3. Make sure it's under your personal account (not organization)"
    echo "   4. Enable Pages in Settings > Pages > Source: GitHub Actions"
    echo ""
    read -p "Press Enter after setting up the repository..."
fi

# Push to main branch
echo "🚀 Pushing to GitHub..."
git push -u origin main

echo "✅ Deployment initiated!"
echo ""
echo "🌐 Your portfolio will be available at:"
echo "   https://karan-mirakhor.github.io/"
echo ""
echo "📋 Next steps:"
echo "   1. Go to your repository on GitHub"
echo "   2. Go to Settings > Pages"
echo "   3. Select 'Deploy from a branch'"
echo "   4. Choose 'main' branch and '/ (root)' folder"
echo "   5. Save and wait for deployment (usually 2-5 minutes)"
echo ""
echo "🎉 Your portfolio will be live shortly!"
