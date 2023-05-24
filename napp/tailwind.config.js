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
        'sans': ['Proxima-Regular', 'Noto Sans', 'Open Sans', ],
        'serif': [ 'Proxima-Regular', 'Noto Sans', 'Open Sans', ],
        'mono': ['Proxima-Regular', 'Noto Sans', 'Open Sans', ],
        'display': ['Proxima-Regular', 'Noto Sans', 'Open Sans', ],
        'body': ['Proxima-Regular', 'Noto Sans', 'Open Sans', ],
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

