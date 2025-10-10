import matter from 'gray-matter';
import { marked } from 'marked';

// For now, we'll define the content directly since raw imports may not work in older Vite versions
const beliefGuidedZeroShot = `---
title: "Belief-Guided Zero-Shot Coordination for Multi-Agent Systems"
authors: "Karan Mirakhor, Katia Sycara"
venue: "ICLR"
year: 2026
link: "https://openreview.net/forum?id=jJvXNpvOdM"
---

We propose a novel approach to zero-shot coordination in multi-agent systems by leveraging belief modeling and opponent adaptation. Our method enables agents to coordinate effectively with unseen partners by maintaining beliefs about their strategies and adapting accordingly. The approach demonstrates significant improvements in cooperative environments with partial observability.`;

const multiAgentDeception = `---
title: "Strategic Deception in Multi-Agent Reinforcement Learning"
authors: "Karan Mirakhor, Katia Sycara, Prashant Doshi"
venue: "AAMAS"
year: 2025
link: "https://example.com/paper2"
---

This work explores the role of strategic deception in multi-agent reinforcement learning environments. We develop a framework for agents to learn when and how to deceive opponents while maintaining cooperation when beneficial. The approach shows improved performance in competitive scenarios with partial information.`;

const roboticTaskPlanning = `---
title: "Hierarchical Task Planning for Robotic Object Rearrangement under Partial Observability"
authors: "Karan Mirakhor, TCS Research Team"
venue: "ICRA"
year: 2024
link: "https://example.com/paper3"
---

We present a hierarchical approach to task planning for robotic object rearrangement in partially observable environments. The method combines high-level symbolic planning with low-level motion planning, enabling robots to handle uncertainty and adapt to changing environments. Experimental results show improved success rates in cluttered indoor scenarios.`;

const justImagineVla = `---
title: "Just Imagine: Closed-Loop VLA for Long-Horizon Tasks"
link: "https://drive.google.com/presentation/d/1zFm-VuV9FV5P4Vt70gTIIagh_6zWmC2OEriu3IMXxfQ"
---

Visual-language-action pipeline leveraging world models for imagination-driven reasoning. Learning dense proxy rewards from sparse human videos to guide actor–critic control on Libero benchmark. This project explores how visual language models can be integrated with robotic control for complex manipulation tasks.`;

const multiAgentSimulation = `---
title: "Multi-Agent Simulation Framework for Cooperative Robotics"
link: "https://github.com/karan-13-hub/multi-agent-sim"
---

A comprehensive simulation framework for testing multi-agent reinforcement learning algorithms in cooperative robotic environments. Features include configurable agent behaviors, dynamic environment generation, and real-time visualization. Used for validating MARL algorithms before real-world deployment.`;

const uncertaintyQuantification = `---
title: "Uncertainty Quantification in Deep Reinforcement Learning"
link: "https://github.com/karan-13-hub/uncertainty-rl"
---

Development of uncertainty quantification methods for deep reinforcement learning agents operating in safety-critical environments. Implements ensemble-based uncertainty estimation and Bayesian neural networks for improved decision-making under uncertainty. Applied to autonomous vehicle control and robotic manipulation tasks.`;

const jnTataScholarship = `---
title: "JN Tata Endowment Scholarship"
year: 2024
---

Received for excellence in academic research and potential for doctoral study. This prestigious scholarship recognizes outstanding academic achievement and research potential in engineering and technology fields.`;

const programGoldMedal = `---
title: "Program Gold Medal - IIIT Hyderabad"
year: 2023
---

Awarded for achieving the highest GPA in the Electronics and Communication Engineering program. This recognition highlights academic excellence and outstanding performance throughout the undergraduate program.`;

const bestResearchPaper = `---
title: "Best Research Paper Award - TCS Research"
year: 2024
---

Recognized for outstanding contribution to robotic task planning research. The paper presented novel approaches to hierarchical planning under partial observability, with significant practical applications in service robotics.`;

const contentFiles = {
  publications: [
    beliefGuidedZeroShot,
    multiAgentDeception,
    roboticTaskPlanning
  ],
  projects: [
    justImagineVla,
    multiAgentSimulation,
    uncertaintyQuantification
  ],
  awards: [
    jnTataScholarship,
    programGoldMedal,
    bestResearchPaper
  ]
};

export function getAllContent(type) {
  if (!contentFiles[type]) {
    return [];
  }

  return contentFiles[type]
    .map((content, index) => {
      const { data, content: markdownContent } = matter(content);
      return {
        slug: `item-${index}`,
        ...data,
        content: markdownContent,
      };
    })
    .sort((a, b) => {
      // Sort by year if available, otherwise by title
      if (a.year && b.year) {
        return b.year - a.year;
      }
      return a.title?.localeCompare(b.title) || 0;
    });
}

export function getContentBySlug(type, slug) {
  const allContent = getAllContent(type);
  return allContent.find(item => item.slug === slug) || null;
}

export function markdownToHtml(markdown) {
  return marked(markdown);
}
