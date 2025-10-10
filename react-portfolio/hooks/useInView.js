import { useState, useEffect, useRef } from 'react';

export const useInView = (options = {}) => {
  const ref = useRef(null);
  const [isInView, setIsInView] = useState(false);

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setIsInView(true);
        }
      },
      {
        threshold: options.threshold || 0.1,
        rootMargin: options.margin || "0px",
        ...options
      }
    );

    if (ref.current) {
      observer.observe(ref.current);
    }

    return () => observer.disconnect();
  }, [options.threshold, options.margin]);

  return [ref, isInView];
};
