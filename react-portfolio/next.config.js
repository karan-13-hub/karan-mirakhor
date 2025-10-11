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
  ...(process.env.NODE_ENV === 'production' && {
    assetPrefix: '/mirakhor_karan_portfolio',
    basePath: '/mirakhor_karan_portfolio',
  }),
}

module.exports = nextConfig
