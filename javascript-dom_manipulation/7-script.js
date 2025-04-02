fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(reponse => reponse.json())
  .then(data => {
    const movies = data.results;
    const ul = document.querySelector('#list_movies');

    movies.forEach(movie => {
      const li = document.createElement('li');
      li.textContent = movie.title;
      ul.appendChild(li);
    });
})
.catch(error => console.error('Error:', error));


