
let name = document.getElementById("name");
name.value = "周亚庆大神";
name.onfocus = function () {
    name.value = ""
};
name.onblur = function () {
    if (!name.value.trim())
        name.value = "周亚庆大神"
};


let province = document.getElementById("province");
let city = document.getElementById("city");
province.onchange = function () {
    let proCitys = {0:[],1:["海淀区","朝阳区","丰台区"],2:["浦东新区","虹口区","黄浦区"],3:[]};
    let citys = proCitys[province.value];
    if(province.value !== "0")
        city.innerHTML = "";
    else
        city.innerHTML = "<option value=\"\">未选择</option>";
    for(let i=0; i<citys.length; i++){
        let op = document.createElement("option");
        op.innerText = citys[i];
        city.appendChild(op);
    }
};

