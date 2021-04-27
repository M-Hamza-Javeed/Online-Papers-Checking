window.onload=function(){


    let card_item=document.getElementsByClassName("sidebar-btn");
    for(var i=0;i<card_item.length-1;i++){
    if(card_item[i].nextElementSibling!=null){
    card_item[i].nextElementSibling.style.display='none';
    card_item[i].addEventListener("click",(event)=>{
    var dis=event.target.parentElement.nextElementSibling;
    if(dis.style.display=="none"){dis.style.display="block";}else{dis.style.display="none";}
    });}}

   var path=document.URL.split('/');
   var page=path[path.length-2].split('.')[0];
   var pages=["Exams","Add_Coruses","Courses","Results","Students","Teachers"];
   var present=false;
    
   for (var i=0;i<6;i++){if(page==pages[i]){present=true;}}
        load_charts();
}



function load_charts(){

    var bar = document.getElementById('bar').getContext('2d');
    var pie = document.getElementById('pie').getContext('2d');
    
    var chart = new Chart(bar, {
        type: 'bar',
        data: {
            labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
            datasets: [{label: 'Student Resuls',backgroundColor:'#ff6347',
                data: [5, 10, 5, 2, 20, 30, 45]}]}});

                
    var myChart = new Chart(pie, {
        type: 'doughnut', 
        data: {
            labels: ["Marks","From 100%"],
            datasets: [{data:[60,40],backgroundColor: ['#ff6347', '#fff0'],borderAlign:"center",borderWidth:0}]}        
        });
    
    
}

