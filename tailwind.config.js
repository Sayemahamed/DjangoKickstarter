/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/**/*.html"],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        primary: 'rgb(var(--color-primary) / <alpha-value>)',
        secondary: 'rgb(var(--color-secondary) / <alpha-value>)',
        accent: 'rgb(var(--color-accent) / <alpha-value>)',
        text: 'rgb(var(--color-text) / <alpha-value>)',
      }
    },
  },
  plugins: [],
}
