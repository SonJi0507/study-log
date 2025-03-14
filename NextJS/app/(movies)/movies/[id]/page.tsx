import React, { Suspense } from "react"
import MovieVideos from "../../../../components/movie-videos";
import MovieInfo from "../../../../components/movie-info";


interface Params {
    id: string;
}
export default async function MovieDetail({ params }: { params: Params }) {
    const { id } = await params;
    // const [movie, videos] = await Promise.all([getMovie(id), getVideos(id)]);
    return <div>
        <Suspense fallback={<h1>Loading movie info</h1>}>
            <MovieInfo id={id} />
        </Suspense>
        <Suspense fallback={<h1>Loading movie videos</h1>}>
            <MovieVideos id={id} />
        </Suspense>
    </div>
}