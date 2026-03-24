import { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { PixelCharacter } from './PixelCharacter';

interface LoadingActorsProps {
  count: number;
}

const LOADING_MESSAGES = [
  'Gathering stakeholders into a town hall',
  'Briefing everyone on the agenda',
  'Assigning seats at the table',
  'Sharpening their arguments',
  'Warming up the debate stage',
  'Distributing name tags',
  'Reviewing each stakeholder\'s talking points',
  'Making sure everyone has coffee',
];

export function LoadingActors({ count }: LoadingActorsProps) {
  const indices = Array.from({ length: Math.min(count, 10) }, (_, i) => i);
  const [msgIdx, setMsgIdx] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      setMsgIdx((prev) => (prev + 1) % LOADING_MESSAGES.length);
    }, 4000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="flex flex-col items-center justify-center py-16 gap-8">
      {/* Bouncing pixel characters */}
      <div className="flex items-end gap-5">
        {indices.map((i) => (
          <motion.div
            key={i}
            initial={{ opacity: 0, scale: 0, y: 40 }}
            animate={{
              opacity: 1,
              scale: 1,
              y: [0, -18, 0],
            }}
            transition={{
              opacity: { delay: i * 0.35, duration: 0.3 },
              scale: { delay: i * 0.35, duration: 0.4, type: 'spring', stiffness: 300 },
              y: {
                delay: i * 0.35 + 0.4,
                duration: 0.7,
                repeat: Infinity,
                repeatType: 'loop',
                ease: 'easeInOut',
                repeatDelay: indices.length * 0.15,
              },
            }}
            className="flex flex-col items-center gap-2"
          >
            <PixelCharacter variant={i} size={56} />
            <motion.div
              initial={{ scale: 0 }}
              animate={{ scale: [0.7, 1.1, 0.7] }}
              transition={{
                delay: i * 0.35 + 0.5,
                duration: 1.2,
                repeat: Infinity,
              }}
              className="w-7 h-1.5 rounded-full bg-gray-200"
            />
          </motion.div>
        ))}
      </div>

      {/* Progress text */}
      <div className="text-center space-y-3">
        <motion.p
          key={msgIdx}
          className="text-lg text-gray-700 font-semibold"
          initial={{ opacity: 0, y: 8 }}
          animate={{ opacity: 1, y: 0 }}
          exit={{ opacity: 0, y: -8 }}
          transition={{ duration: 0.3 }}
        >
          {LOADING_MESSAGES[msgIdx]}...
        </motion.p>
        <motion.div className="flex items-center justify-center gap-1.5">
          {[0, 1, 2].map((i) => (
            <motion.span
              key={i}
              className="w-2 h-2 rounded-full bg-blue-500"
              animate={{ opacity: [0.3, 1, 0.3] }}
              transition={{
                duration: 1,
                repeat: Infinity,
                delay: i * 0.3,
              }}
            />
          ))}
        </motion.div>
        <motion.p
          className="text-sm text-gray-400"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 3 }}
        >
          Might take up to 4 min
        </motion.p>
      </div>
    </div>
  );
}
