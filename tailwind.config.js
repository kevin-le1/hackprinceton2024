/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: ["class"],
  content: ["./index.html", "./src/**/*.{ts,tsx,js,jsx}"],
  theme: {
    extend: {
      borderRadius: {
        lg: "var(--radius)",
        md: "calc(var(--radius) - 2px)",
        sm: "calc(var(--radius) - 4px)",
      },
      colors: {
        primary: "#E85A4F",
        background: "#EAE7DC",
        secondary: "#D8C3A5",
        red2: "#E98074",
        grey: "#8E8D8A",
      },
    },
  },
  plugins: [require("tailwindcss-animate")],
};
