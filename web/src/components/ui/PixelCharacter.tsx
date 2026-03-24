/**
 * 16x16 pixel-art style characters rendered as inline SVG.
 * Each character is a unique silhouette with a dominant color.
 */

interface PixelCharacterProps {
  variant: number;
  size?: number;
  className?: string;
}

// Each character is a 16x16 grid encoded as rows of [x, y, w, h] rects.
// This creates distinct pixel-art silhouettes for different stakeholder types.
const CHARACTERS: { body: string; color: string; accent: string }[] = [
  {
    // Business person (suit + tie)
    color: '#3b82f6',
    accent: '#93c5fd',
    body: `
      M6,1h4v1h-4z M5,2h6v1h-6z M6,3h1v1h2v-1h1v1h-1v1h-2v-1h-1z
      M7,5h2v1h-2z M5,6h6v1h-6z M4,7h8v1h-8z M4,8h3v1h2v-1h3v1h-3v1h-2v-1h-3z
      M4,9h8v1h-8z M4,10h8v1h-8z M4,11h8v2h-8z M3,13h4v2h-4z M9,13h4v2h-4z
    `,
  },
  {
    // Judge / regulator
    color: '#8b5cf6',
    accent: '#c4b5fd',
    body: `
      M5,0h6v1h-6z M4,1h8v1h-8z M6,2h4v1h-4z M6,3h1v1h2v-1h1v1h-1v1h-2v-1h-1z
      M7,5h2v1h-2z M3,6h10v1h-10z M4,7h8v1h-8z M4,8h8v1h-8z
      M4,9h8v1h-8z M3,10h10v1h-10z M3,11h10v1h-10z M4,12h3v3h-3z M9,12h3v3h-3z
    `,
  },
  {
    // Scientist / researcher
    color: '#10b981',
    accent: '#6ee7b7',
    body: `
      M6,0h4v1h-4z M6,1h4v1h-4z M6,2h1v1h2v-1h1v1h-1v1h-2v-1h-1z
      M7,4h2v1h-2z M5,5h6v1h-6z M5,6h6v1h-6z M4,7h2v1h4v-1h2v1h-2v5h-4v-5h-2z
      M6,13h1v2h-1z M9,13h1v2h-1z
      M2,7h2v1h-2z M12,7h2v1h-2z
    `,
  },
  {
    // Engineer / builder
    color: '#f59e0b',
    accent: '#fcd34d',
    body: `
      M5,0h6v2h-6z M6,2h4v1h-4z M6,3h1v1h2v-1h1v1h-1v1h-2v-1h-1z
      M7,5h2v1h-2z M5,6h6v1h-6z M4,7h8v1h-8z M4,8h8v4h-8z
      M4,12h3v3h-3z M9,12h3v3h-3z
      M3,8h1v2h-1z M12,8h1v2h-1z
    `,
  },
  {
    // Teacher / academic
    color: '#ec4899',
    accent: '#f9a8d4',
    body: `
      M6,1h4v1h-4z M6,2h4v1h-4z M6,3h1v1h2v-1h1v1h-1v1h-2v-1h-1z
      M7,5h2v1h-2z M4,6h8v1h-8z M4,7h8v1h-8z M5,8h6v4h-6z
      M4,12h3v3h-3z M9,12h3v3h-3z
      M13,1h2v4h-2z
    `,
  },
  {
    // Doctor / medic
    color: '#ef4444',
    accent: '#fca5a5',
    body: `
      M7,0h2v1h-2z M6,1h4v1h-4z M6,2h1v1h2v-1h1v1h-1v1h-2v-1h-1z
      M7,4h2v1h-2z M5,5h6v1h-6z M4,6h8v1h-8z
      M4,7h3v1h2v-1h3v6h-3v-5h-2v5h-3z
      M4,13h3v2h-3z M9,13h3v2h-3z
    `,
  },
  {
    // Detective / investigator
    color: '#06b6d4',
    accent: '#67e8f9',
    body: `
      M5,0h7v1h-7z M5,1h6v1h-6z M6,2h4v1h-4z M6,3h1v1h2v-1h1v1h-1v1h-2v-1h-1z
      M7,5h2v1h-2z M5,6h6v1h-6z M5,7h6v1h-6z M5,8h6v4h-6z
      M4,12h3v3h-3z M9,12h3v3h-3z
    `,
  },
  {
    // Activist / advocate
    color: '#84cc16',
    accent: '#bef264',
    body: `
      M6,1h4v1h-4z M6,2h4v1h-4z M6,3h1v1h2v-1h1v1h-1v1h-2v-1h-1z
      M7,5h2v1h-2z M5,6h6v1h-6z M4,7h8v1h-8z
      M5,8h6v4h-6z M4,12h3v3h-3z M9,12h3v3h-3z
      M2,7h2v3h-2z M12,7h2v3h-2z
    `,
  },
  {
    // Executive / CEO
    color: '#f97316',
    accent: '#fdba74',
    body: `
      M6,1h4v1h-4z M5,2h6v1h-6z M6,3h1v1h2v-1h1v1h-1v1h-2v-1h-1z
      M7,5h2v1h-2z M4,6h8v1h-8z M3,7h10v1h-10z
      M4,8h8v4h-8z M4,12h3v3h-3z M9,12h3v3h-3z
    `,
  },
  {
    // Union / worker representative
    color: '#14b8a6',
    accent: '#5eead4',
    body: `
      M6,1h4v1h-4z M6,2h4v1h-4z M6,3h1v1h2v-1h1v1h-1v1h-2v-1h-1z
      M7,5h2v1h-2z M5,6h6v1h-6z M4,7h8v1h-8z M4,8h8v1h-8z
      M5,9h6v3h-6z M4,12h3v3h-3z M9,12h3v3h-3z
      M1,8h3v1h-3z M12,8h3v1h-3z
    `,
  },
];

export function PixelCharacter({ variant, size = 48, className = '' }: PixelCharacterProps) {
  const char = CHARACTERS[variant % CHARACTERS.length];

  return (
    <svg
      width={size}
      height={size}
      viewBox="0 0 16 16"
      className={className}
      style={{ imageRendering: 'pixelated' }}
    >
      {/* Shadow */}
      <ellipse cx="8" cy="15.5" rx="4" ry="0.5" fill="rgba(0,0,0,0.3)" />
      {/* Body */}
      <path d={char.body} fill={char.color} />
      {/* Eyes */}
      <rect x="6" y="3" width="1" height="1" fill="white" />
      <rect x="9" y="3" width="1" height="1" fill="white" />
    </svg>
  );
}
