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
    assetPrefix: '',
    basePath: '',
  }),
}

module.exports = nextConfig
