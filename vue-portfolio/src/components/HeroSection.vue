<template>
  <section class="min-h-screen flex items-center justify-center relative overflow-hidden">
    <!-- Background Pattern -->
    <div class="absolute inset-0 opacity-10">
      <div class="absolute top-1/4 left-1/4 w-64 h-64 bg-accent rounded-full blur-3xl"></div>
      <div class="absolute bottom-1/4 right-1/4 w-96 h-96 bg-accent rounded-full blur-3xl"></div>
    </div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center relative z-10">
      <div 
        class="space-y-8"
        v-motion
        :initial="{ opacity: 0, y: 30 }"
        :animate="{ opacity: 1, y: 0 }"
        :transition="{ duration: 800 }"
      >
        <!-- Profile Image Placeholder -->
        <div 
          class="w-32 h-32 mx-auto rounded-full bg-gradient-to-br from-accent to-accent/50 flex items-center justify-center text-4xl font-bold text-navy"
          v-motion
          :initial="{ scale: 0 }"
          :animate="{ scale: 1 }"
          :transition="{ duration: 800, delay: 200 }"
        >
          KM
        </div>

        <!-- Name and Title -->
        <div 
          class="space-y-4"
          v-motion
          :initial="{ opacity: 0, y: 20 }"
          :animate="{ opacity: 1, y: 0 }"
          :transition="{ duration: 800, delay: 400 }"
        >
          <h1 class="text-4xl md:text-6xl lg:text-7xl font-bold text-white">
            Karan Mirakhor
          </h1>
          <p class="text-xl md:text-2xl lg:text-3xl text-accent font-medium">
            Graduate Researcher in Reinforcement Learning and Robotics
          </p>
          <p class="text-lg md:text-xl text-lightSlate max-w-3xl mx-auto">
            Advancing multi-agent systems through belief modeling and strategic decision-making
          </p>
        </div>

        <!-- Social Links -->
        <div 
          class="flex flex-wrap justify-center gap-6"
          v-motion
          :initial="{ opacity: 0, y: 20 }"
          :animate="{ opacity: 1, y: 0 }"
          :transition="{ duration: 800, delay: 600 }"
        >
          <a
            v-for="link in socialLinks"
            :key="link.name"
            :href="link.href"
            target="_blank"
            rel="noopener noreferrer"
            class="flex items-center space-x-2 text-lightSlate hover:text-accent transition-colors duration-200"
            v-motion
            :hover="{ scale: 1.1, y: -2 }"
            :tap="{ scale: 0.95 }"
          >
            <component :is="link.icon" class="w-5 h-5" />
            <span>{{ link.name }}</span>
          </a>
        </div>

        <!-- Scroll Down Indicator -->
        <div 
          class="pt-8"
          v-motion
          :initial="{ opacity: 0 }"
          :animate="{ opacity: 1 }"
          :transition="{ duration: 800, delay: 800 }"
        >
          <button
            @click="scrollToAbout"
            class="text-accent hover:text-white transition-colors duration-200"
            v-motion
            :hover="{ y: -5 }"
          >
            <div class="flex flex-col items-center space-y-2">
              <span class="text-sm">Scroll Down</span>
              <div
                v-motion
                :animate="{ y: [0, 5, 0] }"
                :transition="{ duration: 1500, repeat: Infinity }"
              >
                <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 14l-7 7m0 0l-7-7m7 7V3" />
                </svg>
              </div>
            </div>
          </button>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'HeroSection',
  setup() {
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
      },
      {
        name: 'CV',
        href: 'https://drive.google.com/file/d/1KMUiU1Ze_I2ZgC0N5dFkpX_ucFn5C_G5/view?usp=sharing',
        icon: 'svg'
      }
    ]

    const scrollToAbout = () => {
      const element = document.querySelector('#about')
      if (element) {
        element.scrollIntoView({ behavior: 'smooth' })
      }
    }

    return {
      socialLinks,
      scrollToAbout
    }
  }
})
</script>
