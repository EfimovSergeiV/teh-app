/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: [
    'components/**/*.vue',
    'layouts/**/*.vue',
    'pages/**/*.vue',
    'plugins/**/*.js',
  ],
  theme: {
    extend: {
      fontFamily: {
        'sans': ['Proxima-Regular',],
        'serif': [ 'Proxima-Regular',],
        'mono': ['Proxima-Regular',],
        'display': ['Proxima-Regular',],
        'body': ['Proxima-Regular',],
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
    require('@tailwindcss/forms'),
    require('@tailwindcss/line-clamp'),
    require('@tailwindcss/aspect-ratio'),
  ],
}

