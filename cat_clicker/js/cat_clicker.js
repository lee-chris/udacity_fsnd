function cat(props) {
    
    var that = {};
    
    that.name = props.name;
    that.img = "img/cat.jpeg";
    that.click_count = 0;
    
    return that;
}

function get_cat_html(cat) {
    
    var container_div = $('<div class="cat-container"></div>');
    
    var count_div = $('<div class="count">0</div>');
    $(count_div)
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
    $("#main")
        .append(get_cat_html(cat({name : 'Simon'})))
        .append(get_cat_html(cat({name : 'Ben'})));
});