function getRecommendations() {
  const movie = document.getElementById("movieInput").value;
  fetch(/recommend?movie=${encodeURIComponent(movie)})
    .then(res => res.json())
    .then(data => {
      const list = document.getElementById("recommendationsList");
      list.innerHTML = "";
      if (data.recommendations.length === 0) {
        list.innerHTML = "<li>No recommendations found.</li>";
      } else {
        data.recommendations.forEach(rec => {
          const li = document.createElement("li");
          li.textContent = rec;
          list.appendChild(li);
        });
      }
    });
}