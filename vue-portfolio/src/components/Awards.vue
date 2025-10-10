<template>
  <section id="awards" ref="sectionRef" class="py-20 bg-lightNavy/30">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div 
        class="text-center mb-16"
        v-motion
        :initial="{ opacity: 0, y: 30 }"
        :visible="{ opacity: 1, y: 0 }"
        :transition="{ duration: 800 }"
      >
        <h2 class="section-title">Awards & Recognition</h2>
        <div class="w-24 h-1 bg-accent mx-auto mb-8"></div>
        <p class="text-lg text-lightSlate max-w-3xl mx-auto">
          Recognition for academic excellence and research contributions.
        </p>
      </div>

      <div 
        class="max-w-4xl mx-auto"
        v-motion
        :initial="{ opacity: 0, y: 30 }"
        :visible="{ opacity: 1, y: 0 }"
        :transition="{ duration: 800, delay: 200 }"
      >
        <div v-if="awards.length > 0" class="relative">
          <!-- Timeline line -->
          <div class="absolute left-8 top-0 bottom-0 w-0.5 bg-accent/30"></div>
          
          <div class="space-y-8">
            <div
              v-for="(award, index) in awards"
              :key="index"
              class="relative flex items-start"
              v-motion
              :initial="{ opacity: 0, x: -20 }"
              :visible="{ opacity: 1, x: 0 }"
              :transition="{ duration: 600, delay: index * 100 }"
            >
              <!-- Timeline dot -->
              <div class="absolute left-6 w-4 h-4 bg-accent rounded-full border-4 border-navy z-10"></div>
              
              <!-- Content -->
              <div class="ml-16 bg-lightNavy p-6 rounded-lg border border-lightestNavy hover:border-accent transition-all duration-300 group">
                <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
                  <div class="flex-1">
                    <h3 class="text-xl font-semibold text-white mb-2 group-hover:text-accent transition-colors duration-200">
                      {{ award.title }}
                    </h3>
                    <div v-if="award.year" class="text-accent font-medium mb-3">
                      {{ award.year }}
                    </div>
                    <p v-if="award.content" class="text-lightSlate group-hover:text-lightestSlate transition-colors duration-200">
                      {{ award.content }}
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div v-else class="text-center py-12">
          <div class="text-lightSlate text-lg">
            No awards available at the moment.
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { ref, onMounted } from 'vue'
import { getAllContent } from '../utils/markdown'

export default {
  name: 'Awards',
  setup() {
    const sectionRef = ref(null)
    const awards = ref([])

    onMounted(() => {
      awards.value = getAllContent('awards')
    })

    return {
      sectionRef,
      awards
    }
  }
}
</script>
