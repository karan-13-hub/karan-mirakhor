#!/bin/bash

echo "🚀 Migrating Portfolio to Clean URL: https://karan-mirakhor.github.io/"
echo ""

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "❌ Git repository not initialized. Please run 'git init' first."
    exit 1
fi

echo "📋 Migration Steps:"
echo "1. Create new repository 'karan-mirakhor.github.io' on GitHub"
echo "2. Clone the new repository"
echo "3. Copy all files to the new repository"
echo "4. Push to the new repository"
echo "5. Configure GitHub Pages"
echo ""

read -p "Have you created the new repository 'karan-mirakhor.github.io' on GitHub? (y/n): " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Please create the repository first:"
    echo "1. Go to https://github.com/new"
    echo "2. Name it 'karan-mirakhor.github.io'"
    echo "3. Make sure it's under your personal account (not organization)"
    echo "4. Initialize with README (optional)"
    echo "5. Click 'Create repository'"
    exit 1
fi

echo "📁 Setting up new repository..."

# Create a temporary directory for the new repository
TEMP_DIR="/tmp/karan-mirakhor-portfolio-migration"
if [ -d "$TEMP_DIR" ]; then
    rm -rf "$TEMP_DIR"
fi

echo "🔄 Cloning new repository..."
git clone https://github.com/karan-mirakhor/karan-mirakhor.github.io.git "$TEMP_DIR"

if [ $? -ne 0 ]; then
    echo "❌ Failed to clone repository. Please check:"
    echo "   - Repository exists: https://github.com/karan-mirakhor/karan-mirakhor.github.io"
    echo "   - You have access to the repository"
    echo "   - Repository name is exactly 'karan-mirakhor.github.io'"
    exit 1
fi

echo "📂 Copying files to new repository..."
# Copy all files except .git directory
rsync -av --exclude='.git' --exclude='node_modules' --exclude='out' --exclude='.next' . "$TEMP_DIR/"

echo "🚀 Pushing to new repository..."
cd "$TEMP_DIR"

# Add all files
git add .

# Commit changes
git commit -m "Initial portfolio setup - migrated for clean URL"

# Push to main branch
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Migration completed successfully!"
    echo ""
    echo "🌐 Your portfolio will be available at:"
    echo "   https://karan-mirakhor.github.io/"
    echo ""
    echo "📋 Next steps:"
    echo "1. Go to https://github.com/karan-mirakhor/karan-mirakhor.github.io"
    echo "2. Go to Settings > Pages"
    echo "3. Under 'Source', select 'GitHub Actions'"
    echo "4. Click 'Save'"
    echo "5. Go to Actions tab and wait for deployment to complete"
    echo ""
    echo "🔄 Future updates:"
    echo "   - Edit files in this directory"
    echo "   - Run: git add . && git commit -m 'Update portfolio' && git push"
    echo "   - Changes will be automatically deployed"
    echo ""
    echo "🧹 Cleanup:"
    echo "   - You can now delete the old repository if desired"
    echo "   - Update any bookmarks or links to use the new URL"
else
    echo "❌ Failed to push to new repository. Please check your permissions."
    exit 1
fi

# Cleanup
cd ..
rm -rf "$TEMP_DIR"

echo "🎉 Migration complete! Your portfolio is now at https://karan-mirakhor.github.io/"
