import React, { Suspense } from "react"
import MovieVideos from "../../../../components/movie-videos";
import MovieInfo, { getMovie } from "../../../../components/movie-info";


interface IParams {
    id: string;
}

export async function generateMetadata({ params }: { params: IParams }) {
    const { id } = await params;
    const movie = await getMovie(id);
    return {
        title: movie.title,
    }
}



export default async function MovieDetail({ params }: { params: IParams }) {
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