import { Metadata } from "next";
import Navigation from "../components/navigation";
export const metadata: Metadata = {
    title: "None found",
}

export default function NotFound() {
    return <div>
        <h1>Not found!</h1>
    </div>
}