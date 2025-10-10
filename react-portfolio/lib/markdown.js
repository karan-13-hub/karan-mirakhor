import matter from 'gray-matter';
import { remark } from 'remark';
import html from 'remark-html';

// Static content data
const publications = [
  {
    title: "Belief-Guided Zero-Shot Coordination for Multi-Agent Systems",
    authors: "Karan Mirakhor, Katia Sycara",
    venue: "ICLR",
    year: 2026,
    link: "https://openreview.net/forum?id=jJvXNpvOdM",
    content: "We propose a novel approach to zero-shot coordination in multi-agent systems by leveraging belief modeling and opponent adaptation. Our method enables agents to coordinate effectively with unseen partners by maintaining beliefs about their strategies and adapting accordingly. The approach demonstrates significant improvements in cooperative environments with partial observability."
  },
  {
    title: "Strategic Deception in Multi-Agent Reinforcement Learning",
    authors: "Karan Mirakhor, Katia Sycara, Prashant Doshi",
    venue: "AAMAS",
    year: 2025,
    link: "https://example.com/paper2",
    content: "This work explores the role of strategic deception in multi-agent reinforcement learning environments. We develop a framework for agents to learn when and how to deceive opponents while maintaining cooperation when beneficial. The approach shows improved performance in competitive scenarios with partial information."
  },
  {
    title: "Hierarchical Task Planning for Robotic Object Rearrangement under Partial Observability",
    authors: "Karan Mirakhor, TCS Research Team",
    venue: "ICRA",
    year: 2024,
    link: "https://example.com/paper3",
    content: "We present a hierarchical approach to task planning for robotic object rearrangement in partially observable environments. The method combines high-level symbolic planning with low-level motion planning, enabling robots to handle uncertainty and adapt to changing environments. Experimental results show improved success rates in cluttered indoor scenarios."
  }
];

const projects = [
  {
    title: "Just Imagine: Closed-Loop VLA for Long-Horizon Tasks",
    link: "https://drive.google.com/presentation/d/1zFm-VuV9FV5P4Vt70gTIIagh_6zWmC2OEriu3IMXxfQ",
    content: "Visual-language-action pipeline leveraging world models for imagination-driven reasoning. Learning dense proxy rewards from sparse human videos to guide actor–critic control on Libero benchmark. This project explores how visual language models can be integrated with robotic control for complex manipulation tasks."
  },
  {
    title: "Multi-Agent Simulation Framework for Cooperative Robotics",
    link: "https://github.com/karan-13-hub/multi-agent-sim",
    content: "A comprehensive simulation framework for testing multi-agent reinforcement learning algorithms in cooperative robotic environments. Features include configurable agent behaviors, dynamic environment generation, and real-time visualization. Used for validating MARL algorithms before real-world deployment."
  },
  {
    title: "Uncertainty Quantification in Deep Reinforcement Learning",
    link: "https://github.com/karan-13-hub/uncertainty-rl",
    content: "Development of uncertainty quantification methods for deep reinforcement learning agents operating in safety-critical environments. Implements ensemble-based uncertainty estimation and Bayesian neural networks for improved decision-making under uncertainty. Applied to autonomous vehicle control and robotic manipulation tasks."
  }
];

const awards = [
  {
    title: "JN Tata Endowment Scholarship",
    year: 2024,
    content: "Received for excellence in academic research and potential for doctoral study. This prestigious scholarship recognizes outstanding academic achievement and research potential in engineering and technology fields."
  },
  {
    title: "Program Gold Medal - IIIT Hyderabad",
    year: 2023,
    content: "Awarded for achieving the highest GPA in the Electronics and Communication Engineering program. This recognition highlights academic excellence and outstanding performance throughout the undergraduate program."
  },
  {
    title: "Best Research Paper Award - TCS Research",
    year: 2024,
    content: "Recognized for outstanding contribution to robotic task planning research. The paper presented novel approaches to hierarchical planning under partial observability, with significant practical applications in service robotics."
  }
];

const contentData = {
  publications,
  projects,
  awards
};

export function getAllContent(type) {
  return contentData[type] || [];
}

export function getContentBySlug(type, slug) {
  const allContent = getAllContent(type);
  return allContent.find(item => item.slug === slug) || null;
}

export async function markdownToHtml(markdown) {
  const result = await remark().use(html).process(markdown);
  return result.toString();
}
