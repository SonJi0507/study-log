import { Metadata } from "next"


export const metadata: Metadata = {
    title: "Home",
};
const URL = "https://nomad-movies.nomadcoders.workers.dev/movies"
async function getMovies() {
    return fetch(URL).then(response => response.json());
}
export default async function HomePage() {
    const movies = await getMovies();
    return <div>
        {JSON.stringify(movies)}
    </div>

    // const [isLoading, setIsLoding] = useState(true);
    // const [movies, setMovies] = useState();
    // const getMovies = async () => {
    //     const response = await fetch(URL)
    //     const json = await response.json();
    //     setMovies(json);
    //     setIsLoding(false);
    // }
    // useEffect(() => {
    //     getMovies();
    // }, []);
    // return <div>
    //     {isLoading ? "Loading... " : JSON.stringify(movies)}
    // </div>
}