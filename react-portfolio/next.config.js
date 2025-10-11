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
  distDir: 'out',
  basePath: '/karan-mirakhor.github.io',
  assetPrefix: '/karan-mirakhor.github.io',
}

module.exports = nextConfig
