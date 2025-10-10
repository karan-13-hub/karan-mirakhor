<template>
  <div id="app" class="min-h-screen bg-navy">
    <Navbar />
    <main>
      <HeroSection />
      <AboutSection />
      <Interests />
      <Publications />
      <Projects />
      <Awards />
      <Contact />
    </main>
    <Footer />
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue'
import HeroSection from './components/HeroSection.vue'
import AboutSection from './components/AboutSection.vue'
import Interests from './components/Interests.vue'
import Publications from './components/Publications.vue'
import Projects from './components/Projects.vue'
import Awards from './components/Awards.vue'
import Contact from './components/Contact.vue'
import Footer from './components/Footer.vue'

export default {
  name: 'App',
  components: {
    Navbar,
    HeroSection,
    AboutSection,
    Interests,
    Publications,
    Projects,
    Awards,
    Contact,
    Footer
  }
}
</script>
