<template>
  <nav 
    :class="[
      'fixed top-0 left-0 right-0 z-50 transition-all duration-300',
      isScrolled ? 'bg-navy/90 backdrop-blur-md' : 'bg-transparent'
    ]"
    v-motion
    :initial="{ y: -100 }"
    :animate="{ y: 0 }"
  >
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16">
        <!-- Logo -->
        <div 
          class="flex-shrink-0"
          v-motion
          :hover="{ scale: 1.05 }"
        >
          <span class="text-xl font-bold text-accent">KM</span>
        </div>

        <!-- Desktop Navigation -->
        <div class="hidden md:block">
          <div class="ml-10 flex items-baseline space-x-8">
            <button
              v-for="item in navItems"
              :key="item.name"
              @click="scrollToSection(item.href)"
              class="text-lightSlate hover:text-accent px-3 py-2 text-sm font-medium transition-colors duration-200"
              v-motion
              :hover="{ scale: 1.05 }"
              :tap="{ scale: 0.95 }"
            >
              {{ item.name }}
            </button>
          </div>
        </div>

        <!-- Mobile menu button -->
        <div class="md:hidden">
          <button
            @click="toggleMobileMenu"
            class="text-lightSlate hover:text-accent p-2"
            v-motion
            :tap="{ scale: 0.95 }"
          >
            <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path
                v-if="!isMobileMenuOpen"
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M4 6h16M4 12h16M4 18h16"
              />
              <path
                v-else
                stroke-linecap="round"
                stroke-linejoin="round"
                stroke-width="2"
                d="M6 18L18 6M6 6l12 12"
              />
            </svg>
          </button>
        </div>
      </div>
    </div>

    <!-- Mobile Navigation -->
    <div
      v-if="isMobileMenuOpen"
      class="md:hidden bg-navy/95 backdrop-blur-md"
      v-motion
      :initial="{ opacity: 0, height: 0 }"
      :animate="{ opacity: 1, height: 'auto' }"
      :exit="{ opacity: 0, height: 0 }"
    >
      <div class="px-2 pt-2 pb-3 space-y-1 sm:px-3">
        <button
          v-for="item in navItems"
          :key="item.name"
          @click="scrollToSection(item.href)"
          class="text-lightSlate hover:text-accent block px-3 py-2 text-base font-medium w-full text-left"
          v-motion
          :hover="{ scale: 1.05 }"
          :tap="{ scale: 0.95 }"
        >
          {{ item.name }}
        </button>
      </div>
    </div>
  </nav>
</template>

<script>
import { ref, onMounted, onUnmounted } from 'vue'

export default {
  name: 'Navbar',
  setup() {
    const isScrolled = ref(false)
    const isMobileMenuOpen = ref(false)

    const navItems = [
      { name: 'About', href: '#about' },
      { name: 'Research', href: '#research' },
      { name: 'Publications', href: '#publications' },
      { name: 'Projects', href: '#projects' },
      { name: 'Awards', href: '#awards' },
      { name: 'Contact', href: '#contact' },
    ]

    const handleScroll = () => {
      isScrolled.value = window.scrollY > 50
    }

    const scrollToSection = (href) => {
      const element = document.querySelector(href)
      if (element) {
        element.scrollIntoView({ behavior: 'smooth' })
      }
      isMobileMenuOpen.value = false
    }

    const toggleMobileMenu = () => {
      isMobileMenuOpen.value = !isMobileMenuOpen.value
    }

    onMounted(() => {
      window.addEventListener('scroll', handleScroll)
    })

    onUnmounted(() => {
      window.removeEventListener('scroll', handleScroll)
    })

    return {
      isScrolled,
      isMobileMenuOpen,
      navItems,
      scrollToSection,
      toggleMobileMenu
    }
  }
}
</script>
