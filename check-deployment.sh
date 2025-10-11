#!/bin/bash

echo "🔍 Checking GitHub Pages deployment status..."
echo ""

# Check if the site is accessible
echo "Testing site accessibility..."
if curl -s -o /dev/null -w "%{http_code}" https://karan-mirakhor.github.io | grep -q "200"; then
    echo "✅ Site is live and accessible!"
    echo "🌐 Your portfolio is available at: https://karan-mirakhor.github.io"
    echo ""
    echo "📋 Site details:"
    curl -I https://karan-mirakhor.github.io 2>/dev/null | head -5
else
    echo "❌ Site is not yet accessible (HTTP 404 or other error)"
    echo "⏳ This might mean:"
    echo "   - GitHub Pages is still deploying (wait 2-5 minutes)"
    echo "   - GitHub Pages is not configured yet"
    echo "   - There's an issue with the deployment"
    echo ""
    echo "🔧 To configure GitHub Pages:"
    echo "   1. Go to https://github.com/karan-13-hub/karan-mirakhor.github.io"
    echo "   2. Click 'Settings' tab"
    echo "   3. Click 'Pages' in the left sidebar"
    echo "   4. Under 'Source', select 'Deploy from a branch'"
    echo "   5. Choose 'main' branch and '/ (root)' folder"
    echo "   6. Click 'Save'"
    echo "   7. Wait 2-5 minutes for deployment"
fi

echo ""
echo "🔗 Direct links to check:"
echo "   - Main site: https://karan-mirakhor.github.io"
echo "   - Simple portfolio: https://karan-mirakhor.github.io/simple-portfolio/"
echo "   - React portfolio: https://karan-mirakhor.github.io/react-portfolio/"
echo "   - Vue portfolio: https://karan-mirakhor.github.io/vue-portfolio/"
