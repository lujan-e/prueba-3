const apiKey = '9962d150d9062fb9250cf0da86616324';
const apiUrl = 'https://api.themoviedb.org/3';
const movieList = document.getElementById('movies');
const movieDetailsContainer = document.getElementById('movie-details');
const searchButton = document.getElementById('search-button');
const searchInput = document.getElementById('search-input');
const favoritesList = document.getElementById('favorites-list');
const addToFavoritesButton = document.getElementById('add-to-favorites');
let selectedMovieId = null;
let favoriteMovies = JSON.parse(localStorage.getItem('favorites')) || [];

// Fetch and display popular movies
async function fetchPopularMovies() {
    try {
        const response = await fetch(`${apiUrl}/movie/popular?api_key=${apiKey}&language=en-US&page=1`);
        if (!response.ok) {
            throw new Error('Error al obtener las películas populares');
        }
        const data = await response.json();
        displayMovies(data.results);
    } catch (error) {
        console.error('Error fetching popular movies:', error);
    }
}

// Display movies
function displayMovies(movies) {
    movieList.innerHTML = ''; // Limpia la lista de películas
    movies.forEach(movie => {
        const li = document.createElement('li');
        li.innerHTML = `
            <img src="https://image.tmdb.org/t/p/w500${movie.poster_path}" alt="${movie.title}">
            <span>${movie.title}</span>
        `;
        li.onclick = () => {
            selectedMovieId = movie.id; // Actualiza el id de la película seleccionada
            showMovieDetails(movie.id); // Muestra detalles al hacer clic en la película
        };
        movieList.appendChild(li);
    });
}

// Show movie details
async function showMovieDetails(movieId) {
    try {
        const response = await fetch(`${apiUrl}/movie/${movieId}?api_key=${apiKey}&language=en-US`);
        if (!response.ok) {
            throw new Error(`Error al obtener los detalles de la película: ${response.status} - ${response.statusText}`);
        }
        const movieDetails = await response.json();
        updateMovieDetails(movieDetails);
        movieDetailsContainer.classList.remove('hidden'); // Muestra la sección de detalles
    } catch (error) {
        console.error('Error fetching movie details:', error.message);
    }
}

function updateMovieDetails(movie) {
    const details = document.getElementById('details'); // Asegúrate de tener un contenedor en tu HTML con este id
    details.innerHTML = `
        <h3>${movie.title}</h3>
        <p><strong>Fecha de lanzamiento:</strong> ${movie.release_date}</p>
        <p><strong>Sinopsis:</strong> ${movie.overview}</p>
        <p><strong>Calificación:</strong> ${movie.vote_average}/10</p>
        <img src="https://image.tmdb.org/t/p/w500${movie.poster_path}" alt="${movie.title} Poster">
    `;
}

// Search movies
searchButton.addEventListener('click', async () => {
    const query = searchInput.value.trim();
    if (query) {
        try {
            const response = await fetch(`${apiUrl}/search/movie?api_key=${apiKey}&query=${encodeURIComponent(query)}&language=en-US&page=1`);
            if (!response.ok) {
                throw new Error('Error al realizar la búsqueda de películas');
            }
            const data = await response.json();
            displayMovies(data.results);
        } catch (error) {
            console.error('Error searching movies:', error);
        }
    }
});

// Add movie to favorites
addToFavoritesButton.addEventListener('click', () => {
    if (selectedMovieId) {
        const movieTitleElement = document.querySelector('#details h3');
        const movieTitle = movieTitleElement ? movieTitleElement.textContent : null;

        if (!movieTitle) {
            console.error('No se pudo encontrar el título de la película.');
            return;
        }

        const favoriteMovie = {
            id: selectedMovieId,
            title: movieTitle
        };

        // Verifica si la película ya está en favoritos
        if (!favoriteMovies.some(movie => movie.id === selectedMovieId)) {
            favoriteMovies.push(favoriteMovie);
            localStorage.setItem('favorites', JSON.stringify(favoriteMovies)); // Guarda en localStorage
            displayFavorites(); // Muestra la lista actualizada de favoritos
        }
    }
});

// Display favorite movies
function displayFavorites() {
    favoritesList.innerHTML = ''; // Limpia la lista de favoritos

    if (favoriteMovies.length === 0) {
        favoritesList.textContent = 'No tienes películas favoritas.';
        return;
    }

    favoriteMovies.forEach(movie => {
        const li = document.createElement('li');
        li.textContent = movie.title;
        favoritesList.appendChild(li);
    });
}

// Initial fetch of popular movies and display favorites
fetchPopularMovies(); // Obtiene y muestra las películas populares
displayFavorites(); // Muestra las películas favoritas guardadas

 