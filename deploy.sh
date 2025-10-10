#!/bin/bash

echo "🚀 Deploying Karan Mirakhor Portfolio..."

# Install dependencies for both projects
echo "📦 Installing React dependencies..."
cd react-portfolio
npm install
cd ..

echo "📦 Installing Vue dependencies..."
cd vue-portfolio
npm install
cd ..

echo "✅ Setup complete! Run the following commands to start development:"
echo ""
echo "React Portfolio:"
echo "  cd react-portfolio && npm run dev"
echo ""
echo "Vue Portfolio:"
echo "  cd vue-portfolio && npm run dev"
echo ""
echo "🌐 Deploy to Vercel:"
echo "  npx vercel --prod"
