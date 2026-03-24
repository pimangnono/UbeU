import type { Config } from 'tailwindcss'

export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        'bg-primary': '#ffffff',
        'bg-surface': '#f8f9fa',
        'bg-elevated': '#f0f1f3',
        'bg-glass': 'rgba(0,0,0,0.02)',
        'border-glass': 'rgba(0,0,0,0.06)',
        'border-subtle': 'rgba(0,0,0,0.08)',
        'text-primary': '#111827',
        'text-secondary': '#4b5563',
        'text-muted': '#9ca3af',
        'accent-blue': '#3b82f6',
        'accent-green': '#10b981',
        'accent-red': '#ef4444',
        'accent-amber': '#f59e0b',
        'accent-purple': '#8b5cf6',
        'accent-cyan': '#06b6d4',
        'accent-pink': '#ec4899',
        'accent-lime': '#84cc16',
        'accent-orange': '#f97316',
        'accent-teal': '#14b8a6',
      },
      fontSize: {
        'xs': ['13px', '18px'],
        'sm': ['14px', '20px'],
        'base': ['15px', '24px'],
        'lg': ['18px', '28px'],
        'xl': ['22px', '30px'],
        '2xl': ['28px', '36px'],
      },
    },
  },
  plugins: [],
} satisfies Config
