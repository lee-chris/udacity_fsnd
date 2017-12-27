
function loadData() {

    var $body = $('body');
    var $wikiElem = $('#wikipedia-links');
    var $nytHeaderElem = $('#nytimes-header');
    var $nytElem = $('#nytimes-articles');
    var $greeting = $('#greeting');

    // clear out old data before new request
    $wikiElem.text("");
    $nytElem.text("");

    // load streetview
    $body.append('<img class="bgimg" src="http://maps.googleapis.com/maps/api/streetview?size=600x300&location=' + $('#street').val() + ' ' + $('#city').val() + '">');

    var url = "https://api.nytimes.com/svc/search/v2/articlesearch.json";
    url += '?' + $.param({
        'api-key': NYT_API_KEY,
        'q': $('#city').val()
    });
    $.getJSON(url, function(result) {
        
        // console.log(result);
        
        var docs = result.response.docs;
        
        for (var i = 0; i < docs.length; i++) {
            $('#nytimes-articles').append('<li class="article"><a href="' + docs[i].web_url + '">' + docs[i].headline.main + '</a><p>' + docs[i].snippet + '</p></li>');
        }
    
    })
    .error(function() {
        $('#nytimes-header').html("Failed to load NY Times articles.");
    });
    
    $.ajax({
        url: "https://en.wikipedia.org/w/api.php",
        data: {
            action: "query",
            format: "json",
            callback: "wikipedia",
            list: "search",
            srsearch: $("#city").val(),
            srprop: "",
            srlimit: 10
        },
        dataType: "jsonp",
        success: function(data) {
            $("body").append("<script>" + data + "</script>");
        }
    });

    return false;
};

function wikipedia(data) {
    var results = data.query.search;
    for (var i = 0; i < results.length; i++) {
        $("#wikipedia-links").append("<li><a href='http://en.wikipedia.org/w/index.php?curid=" + results[i].pageid + "'>" + results[i].title + "</a></li>");
    }
}

$('#form-container').submit(loadData);
