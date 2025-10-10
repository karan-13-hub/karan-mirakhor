<template>
  <section id="contact" ref="sectionRef" class="py-20">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div 
        class="text-center mb-16"
        v-motion
        :initial="{ opacity: 0, y: 30 }"
        :visible="{ opacity: 1, y: 0 }"
        :transition="{ duration: 800 }"
      >
        <h2 class="section-title">Get In Touch</h2>
        <div class="w-24 h-1 bg-accent mx-auto mb-8"></div>
        <p class="text-lg text-lightSlate max-w-3xl mx-auto">
          I'm always interested in discussing new research opportunities, collaborations, 
          and innovative projects in AI and robotics.
        </p>
      </div>

      <div 
        class="max-w-4xl mx-auto"
        v-motion
        :initial="{ opacity: 0, y: 30 }"
        :visible="{ opacity: 1, y: 0 }"
        :transition="{ duration: 800, delay: 200 }"
      >
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <a
            v-for="(contact, index) in contactInfo"
            :key="index"
            :href="contact.href"
            target="_blank"
            rel="noopener noreferrer"
            class="card group cursor-pointer text-center hover:border-accent transition-all duration-300"
            v-motion
            :hover="{ 
              scale: 1.05, 
              y: -5,
              transition: { duration: 200 }
            }"
            :tap="{ scale: 0.95 }"
          >
            <div class="flex flex-col items-center space-y-4">
              <div class="text-accent group-hover:text-white transition-colors duration-200">
                <component :is="contact.icon" class="w-6 h-6" />
              </div>
              <div>
                <h3 class="text-lg font-semibold text-white group-hover:text-accent transition-colors duration-200">
                  {{ contact.type }}
                </h3>
                <p class="text-lightSlate group-hover:text-lightestSlate transition-colors duration-200">
                  {{ contact.value }}
                </p>
              </div>
            </div>
          </a>
        </div>

        <!-- Call to Action -->
        <div 
          class="text-center mt-12"
          v-motion
          :initial="{ opacity: 0, y: 20 }"
          :visible="{ opacity: 1, y: 0 }"
          :transition="{ duration: 800, delay: 400 }"
        >
          <a
            href="mailto:karanmirakhor@gmail.com"
            class="btn-primary text-lg px-8 py-4"
            v-motion
            :hover="{ scale: 1.05 }"
            :tap="{ scale: 0.95 }"
          >
            Send me an email
          </a>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { ref } from 'vue'

export default {
  name: 'Contact',
  setup() {
    const sectionRef = ref(null)

    const contactInfo = [
      {
        type: 'Email',
        value: 'karanmirakhor@gmail.com',
        href: 'mailto:karanmirakhor@gmail.com',
        icon: 'svg'
      },
      {
        type: 'Google Scholar',
        value: 'View Profile',
        href: 'https://scholar.google.com/citations?user=wpeFm64AAAAJ&hl=en',
        icon: 'svg'
      },
      {
        type: 'GitHub',
        value: 'karan-13-hub',
        href: 'https://github.com/karan-13-hub',
        icon: 'svg'
      },
      {
        type: 'LinkedIn',
        value: 'Connect',
        href: 'https://www.linkedin.com/in/karan-mirakhor-b065b7142/',
        icon: 'svg'
      },
      {
        type: 'CV',
        value: 'Download',
        href: 'https://drive.google.com/file/d/1KMUiU1Ze_I2ZgC0N5dFkpX_ucFn5C_G5/view?usp=sharing',
        icon: 'svg'
      }
    ]

    return {
      sectionRef,
      contactInfo
    }
  }
}
</script>
