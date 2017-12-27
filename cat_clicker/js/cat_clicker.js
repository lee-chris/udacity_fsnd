var click_count = 0;

function cat_click() {
    click_count++;
    $("#count").html(click_count);
}

$(function() {
    $("#cat").click(cat_click);
});