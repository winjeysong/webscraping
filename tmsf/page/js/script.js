/**
 * 脚本用于正确将JSON数据展示到页面中
 * winjeysong
 * 2017.5
 */

/* datas */
var datas = [

];

/* create a map instance */
var map = new AMap.Map('container',{
    resizeEnable: true,
    zoom: 11
});
map.setMapStyle("fresh")  //set the map style
map.setFeatures(["road", "point", "bg"])  //set the map content

/* mark datas on map */
//function to get location 
function geocoder(){  
    //load AMap plugin
    AMap.service(["AMap.Geocoder"],function(){
        //create an instance
        var place = new AMap.Geocoder({
            city: "hangzhou",
            redius: 1000,
        });

        //get data in Array datas, call the method to get every location result
        for(i in datas){
            place.getLocation(datas[i].name,function(status, result){
                if(status == "complete" && result.info ==="OK"){
                    geocoder_CallBack(result);
                }
            });
        }
       
    });
}

//function to generate marker
function generateMarker(i, d){  
    //create an instance of marker
    var marker = new AMap.Marker({
        map: map,
        position: [d.location.getLng(), d.location.getLat()]
    });
    //create an instance of data display
    var dataDisplay = new AMap.InfoWindow({
        //content: d.formattedAddress, 静态内容
        offset: {x:0 ,y:-30}
    });
    //set content 
    dataDisplay.setContent(
        //String或htmlDOM,htmlDOM也需要写在引号内
        ""
    )
    //add event
    marker.on("mouseover",function(e){
        dataDisplay.open(map, marker.getPosition());
    })
}

//callback from getLocation, and call generateMarker
function geocoder_CallBack(result){
    //get geocode
    var geocode = result.geocodes;
    for(var i =0; i<geocode.length; i++){
        //call generateMarker
        generateMarker(i,geocode[i]);
    }
    //make marker in a fit range of page
    map.setFitView();
}
