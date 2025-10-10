<template>
  <section id="publications" ref="sectionRef" class="py-20 bg-lightNavy/30">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div 
        class="text-center mb-16"
        v-motion
        :initial="{ opacity: 0, y: 30 }"
        :visible="{ opacity: 1, y: 0 }"
        :transition="{ duration: 800 }"
      >
        <h2 class="section-title">Publications</h2>
        <div class="w-24 h-1 bg-accent mx-auto mb-8"></div>
        <p class="text-lg text-lightSlate max-w-3xl mx-auto">
          My research contributions in multi-agent reinforcement learning, robotics, and AI systems.
        </p>
      </div>

      <div 
        class="space-y-8"
        v-motion
        :initial="{ opacity: 0, y: 30 }"
        :visible="{ opacity: 1, y: 0 }"
        :transition="{ duration: 800, delay: 200 }"
      >
        <div 
          v-if="publications.length > 0"
        >
          <div
            v-for="(pub, index) in publications"
            :key="index"
            class="card group hover:border-accent transition-all duration-300"
            v-motion
            :initial="{ opacity: 0, x: -20 }"
            :visible="{ opacity: 1, x: 0 }"
            :transition="{ duration: 600, delay: index * 100 }"
          >
            <div class="flex flex-col lg:flex-row lg:items-start lg:justify-between gap-4">
              <div class="flex-1">
                <h3 class="text-xl font-semibold text-white mb-2 group-hover:text-accent transition-colors duration-200">
                  {{ pub.title }}
                </h3>
                <p class="text-lightSlate mb-3">
                  {{ pub.authors }}
                </p>
                <div class="flex flex-wrap items-center gap-4 text-sm">
                  <span class="bg-accent/20 text-accent px-3 py-1 rounded-full">
                    {{ pub.venue }} {{ pub.year }}
                  </span>
                </div>
                <p v-if="pub.content" class="text-lightSlate mt-4 leading-relaxed">
                  {{ pub.content }}
                </p>
              </div>
              <a
                v-if="pub.link"
                :href="pub.link"
                target="_blank"
                rel="noopener noreferrer"
                class="btn-primary whitespace-nowrap self-start lg:self-center"
                v-motion
                :hover="{ scale: 1.05 }"
                :tap="{ scale: 0.95 }"
              >
                Read Paper
              </a>
            </div>
          </div>
        </div>
        <div v-else class="text-center py-12">
          <div class="text-lightSlate text-lg">
            No publications available at the moment.
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
  name: 'Publications',
  setup() {
    const sectionRef = ref(null)
    const publications = ref([])

    onMounted(() => {
      publications.value = getAllContent('publications')
    })

    return {
      sectionRef,
      publications
    }
  }
}
</script>
