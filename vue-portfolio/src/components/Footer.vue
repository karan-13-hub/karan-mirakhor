<template>
  <footer class="bg-navy border-t border-lightestNavy">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div 
        class="text-center"
        v-motion
        :initial="{ opacity: 0, y: 20 }"
        :animate="{ opacity: 1, y: 0 }"
        :transition="{ duration: 800 }"
      >
        <div class="flex flex-col md:flex-row items-center justify-between space-y-4 md:space-y-0">
          <div class="text-lightSlate">
            © {{ currentYear }} Karan Mirakhor. All rights reserved.
          </div>
          
          <div class="flex items-center space-x-6">
            <a
              v-for="link in socialLinks"
              :key="link.name"
              :href="link.href"
              target="_blank"
              rel="noopener noreferrer"
              class="text-lightSlate hover:text-accent transition-colors duration-200"
              :aria-label="link.name"
              v-motion
              :hover="{ scale: 1.1, y: -2 }"
              :tap="{ scale: 0.95 }"
            >
              <component :is="link.icon" class="w-5 h-5" />
            </a>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>

<script>
import { ref } from 'vue'

export default {
  name: 'Footer',
  setup() {
    const currentYear = new Date().getFullYear()

    const socialLinks = [
      {
        name: 'Google Scholar',
        href: 'https://scholar.google.com/citations?user=wpeFm64AAAAJ&hl=en',
        icon: 'svg'
      },
      {
        name: 'GitHub',
        href: 'https://github.com/karan-13-hub',
        icon: 'svg'
      },
      {
        name: 'LinkedIn',
        href: 'https://www.linkedin.com/in/karan-mirakhor-b065b7142/',
        icon: 'svg'
      }
    ]

    return {
      currentYear,
      socialLinks
    }
  }
}
</script>
