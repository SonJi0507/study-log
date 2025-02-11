import React from "react"

interface Params {
    id: string;
}

export default function MovieDetail({ params }: { params: Params }) {
    const { id } = React.use(params);
    return <h1>Movie {id}</h1>
}