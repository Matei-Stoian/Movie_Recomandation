
var getPoster = function (title) {

    var film = title;
    $('#cover').html('<div class="alert"><strong>Loading...</strong></div>');
    $.getJSON("https://api.themoviedb.org/3/search/movie?api_key=15d2ea6d0dc1d476efbca3eba2b9bbfb&query=" + film + "&callback=?", function (json) {
        console.log(json);
        var source = 'http://image.tmdb.org/t/p/w500/' + json.results[0].poster_path + '"';
        $("#cover").html('<p><strong>Your Title is: </strong>' + json.results[0].title + '</p>' + '<a href="http://image.tmdb.org/t/p/w500/'+json.results[0].poster_path+'">'+'<img src="http://image.tmdb.org/t/p/w500/' + json.results[0].poster_path + '"></a>');
    });
    
}
$('document').ready(function () {

    $('#search').click(function () {
        getPoster($('#title').val());
    });
});