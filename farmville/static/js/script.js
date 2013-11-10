function searcher() {
var $rows = $('#subTable tr');
$('#search').keyup(function() {
    var val = $.trim($(this).val()).replace(/ +/g, ' ').toLowerCase();
    $rows.show().filter(function() {
        var text = $(this).text().replace(/\s+/g, ' ').toLowerCase();
        return !~text.indexOf(val);
        }).hide();
        setRowColours();
    });
}
function details(sheepId) {
    $('#search').val(sheepId);
    $('#search').keyup();
}
function setRowColours(){
    $('tbody tr:visible:odd,tbody tr:visible:odd input').css({"background": "#bbeebb"});
    $('tbody tr:visible:even,tbody tr:visible:even input').css({"background": "#e5f9e5"});
}

$(document).ready(function(){
    setRowColours();
});

$('tr').click(function(){
     $(this).hide();
    setRowColours();
});