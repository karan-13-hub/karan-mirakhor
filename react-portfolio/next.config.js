/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
  images: {
    domains: ['drive.google.com'],
  },
  // GitHub Pages configuration
  output: 'export',
  trailingSlash: true,
  assetPrefix: process.env.NODE_ENV === 'production' ? '/mirakhor_karan_portfolio' : '',
  basePath: process.env.NODE_ENV === 'production' ? '/mirakhor_karan_portfolio' : '',
}

module.exports = nextConfig
