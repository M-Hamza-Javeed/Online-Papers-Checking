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




function load_charts() {
    let _data = JSON.parse(document.getElementById('dataJson').textContent);
    _labels=[];_marks=[];_papers=[];resultdata=[];var dataitem;totalstudent=[]

    var bar = document.getElementById('bar').getContext('2d');
    var pie = document.getElementById('pie').getContext('2d');

        _data['data'].forEach(item => {
            _labels.push(item['regno_id']);
            _marks.push(item['marks']);
        });

    console.log(_marks,_labels)

    new Chart(bar, {
        type: 'bar',
        data: {        
            labels: _labels,
            datasets: [{label :["Exam Result"],backgroundColor:'#ff6347',data:_marks}]},
        options:{scales:{ yAxes:[{ticks:{beginAtZero:true}}]}}
    });


    new Chart(pie, {
        type: 'doughnut',
        data: {
            labels: ["Pass", "Fail"],
            datasets: [{ 
            label:_labels,
            data: [ _data['pass'],  _data['fail'] ],
            backgroundColor: ['#ff6347', '#422232'], borderAlign: "center" }]
        }
    });

}

