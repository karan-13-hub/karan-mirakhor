import Head from 'next/head'
import Navbar from '../components/Navbar'
import HeroSection from '../components/HeroSection'
import AboutSection from '../components/AboutSection'
import Interests from '../components/Interests'
import Publications from '../components/Publications'
import Projects from '../components/Projects'
import Awards from '../components/Awards'
import Contact from '../components/Contact'
import Footer from '../components/Footer'

export default function Home() {
  return (
    <div className="min-h-screen bg-navy">
      <Head>
        <title>Karan Mirakhor - Research Portfolio</title>
        <meta name="description" content="Graduate Researcher in Reinforcement Learning and Robotics at Carnegie Mellon University" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

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
  )
}
