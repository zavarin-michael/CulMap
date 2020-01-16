var google;

function initMap() {

    var pos = {lat: 56.832040, lng: 60.598218};

    var opt = {
        center: pos,
        zoom: 10,
    };

    var map = new google.maps.Map(document.getElementById("map"), opt);

    var marker = [];
    var pos1 = 0;
    var info = [];
    var mas = ['1','2','3','4','5','6','7','8','9','10'];
    for (let i = 0; i < 10; i++) {
        pos1 = {lat: i * 10, lng: i * 10};
        marker[i] = new google.maps.Marker({
            position: pos1,
            map: map,
            label: mas[i],
        });

        info[i] = new google.maps.InfoWindow({
            content: '<h3>' + i + '</h3>',
        });

        marker[i].addListener("click", function () {
            info[i].open(map, marker[i]);
        })
     }


}
