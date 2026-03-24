import { motion, type HTMLMotionProps } from 'framer-motion';

interface GlassCardProps extends HTMLMotionProps<'div'> {
  children: React.ReactNode;
  className?: string;
  hover?: boolean;
}

export function GlassCard({ children, className = '', hover = false, ...props }: GlassCardProps) {
  return (
    <motion.div
      className={`glass-card p-4 ${hover ? 'transition-all hover:shadow-md hover:border-black/10' : ''} ${className}`}
      {...props}
    >
      {children}
    </motion.div>
  );
}
