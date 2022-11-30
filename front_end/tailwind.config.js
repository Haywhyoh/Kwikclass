module.exports = {
  content: ['./*/*.html', ],
  theme: {
    colors: {
      orange: 'rgba(255, 82, 2, 1)',
      white: 'rgba(255, 255, 255, 1)',
      gray: 'rgba(26, 25, 25, 0.6)',
      'border_color':'rgba(217, 217, 217, 1)',
      'text_black': 'rgba(26, 25, 25, 1)',
      'blur': 'rgba(26, 25, 25, 0.2)',
      'trusted_blue': 'rgba(38, 37, 67, 1)',
    },
    fontFamily: {
      body: ['Solway']
    },
    screens: {
      'xs': '410px',
      'sm': '640px',
      // => @media (min-width: 640px) { ... }

      'md': '768px',
      // => @media (min-width: 768px) { ... }

      'lg': '1024px',
      // => @media (min-width: 1024px) { ... }

      'xl': '1280px',
      // => @media (min-width: 1280px) { ... }

      '2xl': '1536px',
      // => @media (min-width: 1536px) { ... }
    },
    container: {
      center: true,
      padding: '2rem'
    },
    extend: {}
  },
  plugins: []
};
