var pw = $("#id_password");
pw.attr("placeholder","PassWord");
var id = $("#id_username");
id.attr("placeholder","ID");
var cs = $("#id_classification");
cs.css('display','inline');
var cs = $("#id_classification_0");
cs.css('display','inline');
var cs = $("#id_classification_1");
cs.css('display','inline');

var a = document.getElementsByClassName('errorlist')
var v = a.length;
for(var i = 0; i<v; i++){
    console.log(a)
    var pa = a[0].parentElement
    a[0].parentElement.innerHTML=a[0].textContent
    if(pa.textContent){
        pa.style.marginTop = '-30px';
    }else{
        pa.style.marginTop = '0px';
    }
}