# Portfolio Deployment Guide

This guide explains how to deploy the Karan Mirakhor portfolio to GitHub Pages.

## Repository Structure

```
mirakhor_karan_portfolio/
├── react-portfolio/          # Next.js application
│   ├── components/           # React components
│   ├── content/             # Markdown content files
│   ├── lib/                 # Utility functions
│   ├── public/              # Static assets
│   └── pages/               # Next.js pages
├── .github/workflows/       # GitHub Actions
└── DEPLOYMENT.md           # This file
```

## Deployment Process

### Automatic Deployment (Recommended)

1. **Push to main branch**: The portfolio automatically deploys when you push changes to the `main` branch
2. **GitHub Actions**: The workflow builds the Next.js app and deploys to GitHub Pages
3. **Access**: Your portfolio will be available at `https://karan-13-hub.github.io/mirakhor_karan_portfolio`

### Manual Deployment

If you need to deploy manually:

```bash
# Navigate to the react-portfolio directory
cd react-portfolio

# Install dependencies
npm install

# Build the application
npm run build

# The built files will be in the 'out' directory
# You can then deploy the 'out' directory to any static hosting service
```

## Configuration

### Next.js Configuration

The `next.config.js` file is configured for GitHub Pages:

- `output: 'export'` - Generates static files
- `trailingSlash: true` - Adds trailing slashes to URLs
- `basePath` and `assetPrefix` - Configured for the repository path

### Content Management

All content is managed through markdown files in the `content/` directory:

- `hero.md` - Hero section data
- `about.md` - About section data
- `contact.md` - Contact information
- `interests.md` - Research interests
- `navbar.md` - Navigation data
- `footer.md` - Footer data
- `awards/` - Individual award files
- `projects/` - Individual project files
- `publications/` - Individual publication files

## Updating Content

To update the portfolio content:

1. Edit the relevant markdown files in the `content/` directory
2. Commit and push changes to the `main` branch
3. GitHub Actions will automatically rebuild and deploy the site

## Troubleshooting

### Build Issues

If the build fails:

1. Check the GitHub Actions logs
2. Ensure all dependencies are installed
3. Verify that all markdown files have proper frontmatter

### Content Not Updating

If content changes aren't reflected:

1. Clear browser cache
2. Check that markdown files are properly formatted
3. Verify that the build completed successfully

## Local Development

To run the portfolio locally:

```bash
cd react-portfolio
npm install
npm run dev
```

The site will be available at `http://localhost:3000`

## GitHub Pages Settings

Ensure GitHub Pages is configured correctly:

1. Go to repository Settings
2. Navigate to Pages section
3. Source should be set to "GitHub Actions"
4. The workflow should be automatically detected

## Support

For issues or questions about the deployment process, please check:

1. GitHub Actions logs
2. Next.js documentation
3. GitHub Pages documentation