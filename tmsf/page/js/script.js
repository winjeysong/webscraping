/**
 * 脚本用于正确将JSON数据展示到页面中
 * winjeysong
 * 2017.5
 */

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

        //call the method
        place.getLocation("",function(status, result){
            if(status == "complete" && result.info ==="OK"){
                geocoder_CallBack(result);
            }
        });
    });
}

//function to generate marker
function generateMarker(index, data){  
    var marker = new
}
