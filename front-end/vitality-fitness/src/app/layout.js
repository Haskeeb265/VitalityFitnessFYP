import "./globals.css";
export const metadata = {
  title: "Vitality Fitness",
  description: "Vitality Fitness is a fitness app. We offer personalized workouts for each unique individual.",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <body>
        {children}
      </body>
    </html>
  );
}
