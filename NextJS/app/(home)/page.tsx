import { Metadata } from "next"
import Link from "next/link";
import Movie from "../../components/movie";
import styles from "../../styles/home.module.css"

export const metadata: Metadata = {
    title: "Home",
};

export const API_URL = "https://nomad-movies.nomadcoders.workers.dev/movies"

async function getMovies() {
    return fetch(API_URL).then(response => response.json());
}
export default async function HomePage() {
    const movies = await getMovies();
    return <div className={styles.container}>
        {movies.map(movie =>
            <Movie
                key={movie.id}
                id={movie.id}
                title={movie.title}
                poster_path={movie.poster_path}
            />
        )}
    </div>
}