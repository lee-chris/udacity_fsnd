
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
        
        console.log(result);
        
        var docs = result.response.docs;
        
        for (var i = 0; i < docs.length; i++) {
            $('#nytimes-articles').append('<li class="article"><a href="' + docs[i].web_url + '">' + docs[i].headline.main + '</a><p>' + docs[i].snippet + '</p></li>');
        }
    
    });

    return false;
};

$('#form-container').submit(loadData);
