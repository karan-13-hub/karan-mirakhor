import { motion } from 'framer-motion';
import { useInView } from '../hooks/useInView';
import { getSectionContent } from '../lib/markdown';

const AboutSection = () => {
  const [ref, isInView] = useInView({ once: true, margin: "-100px" });
  const aboutData = getSectionContent('about');

  return (
    <section id="about" ref={ref} className="py-20 bg-lightNavy/30">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: isInView ? 1 : 0, y: isInView ? 0 : 30 }}
          transition={{ duration: 0.8 }}
          className="max-w-4xl mx-auto text-center"
        >
          <h2 className="section-title">{aboutData?.title || 'About Me'}</h2>
          <div className="w-24 h-1 bg-accent mx-auto mb-8"></div>
          
          <div className="space-y-6 text-lg text-lightSlate leading-relaxed">
            {aboutData?.content ? (
              <div dangerouslySetInnerHTML={{ __html: aboutData.content.replace(/\n\n/g, '</p><p>').replace(/^/, '<p>').replace(/$/, '</p>') }} />
            ) : (
              <>
                <p>
                  I am a Graduate Research Assistant at the Robotics Institute, Carnegie Mellon University, 
                  advised by Prof. Katia Sycara.
                </p>
                <p>
                  My research explores multi-agent reinforcement learning (MARL) in cooperative and competitive 
                  environments, emphasizing belief modeling, opponent adaptation, and decision-making under uncertainty.
                </p>
                <p>
                  Previously, I was a Pre-doctoral Research Fellow at TCS Research, India, working on task planning 
                  for indoor object rearrangement under partial observability.
                </p>
                <p>
                  I hold a B.Tech (Honors) in Electronics and Communication Engineering from IIIT Hyderabad, 
                  where I received the Program Gold Medal for highest GPA.
                </p>
              </>
            )}
          </div>

          {/* Research Stats */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: isInView ? 1 : 0, y: isInView ? 0 : 20 }}
            transition={{ duration: 0.8, delay: 0.3 }}
            className="grid grid-cols-1 md:grid-cols-3 gap-8 mt-16"
          >
            <div className="text-center">
              <div className="text-3xl font-bold text-accent mb-2">3+</div>
              <div className="text-lightSlate">Years Research Experience</div>
            </div>
            <div className="text-center">
              <div className="text-3xl font-bold text-accent mb-2">5+</div>
              <div className="text-lightSlate">Publications</div>
            </div>
            <div className="text-center">
              <div className="text-3xl font-bold text-accent mb-2">10+</div>
              <div className="text-lightSlate">Projects</div>
            </div>
          </motion.div>
        </motion.div>
      </div>
    </section>
  );
};

export default AboutSection;
