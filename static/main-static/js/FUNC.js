$('#adding-post').on('click', function(event) {
        $('#modal1').toggleClass('open');
        $('#modal2').toggleClass('open');
    });

$('#modal2').on('click', function(event) {
        $('#modal1').toggleClass('open');
        $('#modal2').toggleClass('open');
    });
