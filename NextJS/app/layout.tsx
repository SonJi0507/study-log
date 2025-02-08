import { Metadata } from "next"
import Navigation from "../components/navigation"

export const metadata: Metadata = {
  title: {
    template: "%s | Next movies",
    default: "Next movies",
  },
  description: 'The best movies on the best framework',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>
        <Navigation />
        {children}
      </body>
    </html>
  )
}
