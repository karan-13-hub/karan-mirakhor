import { motion } from 'framer-motion';
import { useInView } from '../hooks/useInView';
import { getSectionContent } from '../lib/markdown';

const Interests = () => {
  const [ref, isInView] = useInView({ once: true, margin: "-100px" });
  const interestsData = getSectionContent('interests');

  const interests = [
    {
      title: "Multi-Agent Reinforcement Learning",
      description: "Cooperative and competitive learning in multi-agent systems",
      icon: "🤖"
    },
    {
      title: "Robotics",
      description: "Autonomous systems and robotic manipulation",
      icon: "🦾"
    },
    {
      title: "Imitation Learning",
      description: "Learning from human demonstrations and expert behavior",
      icon: "👥"
    },
    {
      title: "Decision Making under Uncertainty",
      description: "Robust decision-making in partially observable environments",
      icon: "🎯"
    },
    {
      title: "Deception in AI",
      description: "Strategic deception and adversarial behavior in AI systems",
      icon: "🎭"
    }
  ];

  return (
    <section id="research" ref={ref} className="py-20">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: isInView ? 1 : 0, y: isInView ? 0 : 30 }}
          transition={{ duration: 0.8 }}
          className="text-center mb-16"
        >
          <h2 className="section-title">{interestsData?.title || 'Research Interests'}</h2>
          <div className="w-24 h-1 bg-accent mx-auto mb-8"></div>
          <p className="text-lg text-lightSlate max-w-3xl mx-auto">
            {interestsData?.description || "My research focuses on advancing artificial intelligence through multi-agent systems, with particular emphasis on learning, adaptation, and strategic decision-making."}
          </p>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: isInView ? 1 : 0, y: isInView ? 0 : 30 }}
          transition={{ duration: 0.8, delay: 0.2 }}
          className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8"
        >
          {interests.map((interest, index) => (
            <motion.div
              key={index}
              whileHover={{ 
                scale: 1.05, 
                y: -5,
                transition: { duration: 0.2 }
              }}
              whileTap={{ scale: 0.95 }}
              className="card group cursor-pointer"
            >
              <div className="text-center">
                <div className="text-4xl mb-4 group-hover:scale-110 transition-transform duration-200">
                  {interest.icon}
                </div>
                <h3 className="text-xl font-semibold text-white mb-3 group-hover:text-accent transition-colors duration-200">
                  {interest.title}
                </h3>
                <p className="text-lightSlate group-hover:text-lightestSlate transition-colors duration-200">
                  {interest.description}
                </p>
              </div>
            </motion.div>
          ))}
        </motion.div>
      </div>
    </section>
  );
};

export default Interests;
