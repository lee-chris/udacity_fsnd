function cat(props) {
    
    var that = {};
    
    that.name = props.name;
    that.img = props.img;
    that.click_count = 0;
    
    return that;
}

function get_cat_html(cat) {
    
    var container_div = $('<div class="cat-container"></div>');
    
    var count_div = $('<div class="count"></div>');
    $(count_div)
        .html(cat.click_count)
        .appendTo(container_div);
    
    var name_div = $('<div class="name"></div>');
    $(name_div)
        .html(cat.name)
        .appendTo(container_div);
    
    $('<img class="cat"/>')
        .attr("src", cat.img)
        .click(function() {
            cat.click_count++;
            $(count_div).html(cat.click_count);
        })
        .appendTo(container_div);
    
    return container_div;
}

$(function() {
    
    var cats = [];
    cats.push(cat({name: 'Simon', img:'img/cat1.jpg'}));
    cats.push(cat({name: 'Ben', img: 'img/cat2.jpg'}));
    cats.push(cat({name: 'Josh', img: 'img/cat3.jpg'}));
    cats.push(cat({name: 'David', img: 'img/cat4.jpg'}));
    cats.push(cat({name: 'Adam', img: 'img/cat5.jpg'}));
    
    for (var i = 0; i < cats.length; i++) {
        var opt = $('<option>')
            .val(i)
            .html(cats[i].name);
        $("#list").append(opt);
    }
    
    $("#list").change(function() {
        $("#main").html(get_cat_html(cats[$(this).val()]));
    });
});