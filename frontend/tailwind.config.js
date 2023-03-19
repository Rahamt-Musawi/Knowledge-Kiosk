/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./index.html", "./src/**/*.{vue,js}"],
  theme: {
    extend: {
      colors: {
        'txt-bg': '#FBFDFF ',
        'form-bg': '#EEF2F5',
      },
    },
  },
  plugins: [],
}
