function StatkartMapType(name, layer) {
  this.layer = layer
  this.name = name
  this.alt = name

  this.tileSize = new google.maps.Size(256,256);
  this.maxZoom = 20;
  this.minZoom = 5;
  this.getTile = function(coord, zoom, ownerDocument) {
    var div = ownerDocument.createElement('DIV');
    div.style.width = this.tileSize.width + 'px';
    div.style.height = this.tileSize.height + 'px';
    div.style.backgroundImage = "url(http://opencache.statkart.no/gatekeeper/gk/gk.open_gmaps?layers=" + this.layer + "&zoom=" + zoom + "&x=" + coord.x + "&y=" + coord.y + ")";
    return div;
  };
}
var map;
var markers = new Array()
var bounds = new google.maps.LatLngBounds();
function initialize() {
  var mapOptions = {
    zoom: 8,
    center: new google.maps.LatLng(60.5,9.5),
    mapTypeControlOptions: {
      mapTypeIds: ['topo2'],
      style: google.maps.MapTypeControlStyle.DROPDOWN_MENU
    }
  };
  map = new google.maps.Map(document.getElementById("map_canvas"), mapOptions);
  map.mapTypes.set('topo2',new StatkartMapType("Topografisk", "topo2"));
  map.setMapTypeId('topo2');
}
function jumpthis(id) {
  for (var i=0; i<3; i++) {
    var marker = markers[i]
    if(marker.id==id) {
      stopAnimation(marker);
      if (getAnimation(marker) != null) {
        stopAnimation(marker);
      } else {
        marker.setAnimation(google.maps.Animation.BOUNCE);
        stopAnimation(marker)
      }
    }
  }
}
function getAnimation(marker) {
  return marker.getAnimation()
}
function stopAnimation(marker) {
  setTimeout(function () {
    marker.setAnimation(null);
  }, 1450);
}