import { motion } from 'framer-motion';
import { useInView } from '../hooks/useInView';
import { getSectionContent } from '../lib/markdown';

const Interests = () => {
  const [ref, isInView] = useInView({ once: true, margin: "-100px" });
  const interestsData = getSectionContent('interests');

  const interests = [
    {
      title: "Reinforcement Learning",
      description: "Develop algorithms that enable agents to learn close-to-optimal planning and control strategies in robotics, leveraging human demonstrations, fixed datasets, or interactions with dynamic environments.",
      icon: "🤖"
    },
    {
      title: "Sequence Modelling",
      description: "Design models that predict and understand sequential data, including temporal patterns, trajectories, and planning sequences.",
      icon: "📈"
    },
    {
      title: "Decision Making under Uncertainty",
      description: "Develop methods for robust and adaptive decision-making in partially observable or stochastic environments.",
      icon: "🎯"
    },
    {
      title: "Multi-Agent Reinforcement Learning (MARL)",
      description: "Study interactions of multiple agents learning together, including cooperation, competition, and strategic reasoning.",
      icon: "👥"
    },
    {
      title: "Safe and Robust Control",
      description: "Design control strategies for autonomous systems that ensure safety, reliability, and robustness under uncertainty.",
      icon: "🛡️"
    },
    {
      title: "Planning",
      description: "Develop algorithms for efficient and adaptive planning in robotics and AI systems, including long-horizon decision-making.",
      icon: "🗺️"
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
          className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-6xl mx-auto"
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
