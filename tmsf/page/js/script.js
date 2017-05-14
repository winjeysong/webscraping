/**
 * 脚本用于正确将JSON数据展示到页面中
 * winjeysong
 * 2017.5
 */

//generate AMap
var map = new AMap.Map('container',{
    resizeEnable: true,
    zoom: 10,
    center: [116.480983, 40.0958]
});

//set the map style
map.setMapStyle("fresh")

//set the map content
map.setFeatures(["road", "point", "bg"])
