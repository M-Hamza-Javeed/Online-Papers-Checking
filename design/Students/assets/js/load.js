window.onload=function(){


    var bar = document.getElementById('bar');
    var pie = document.getElementById('pie');

    if (bar && pie){load_charts(bar.getContext('2d'),pie.getContext('2d'));}


    let cardsearch=document.getElementsByClassName('card-search')[0];
    var SwapingNode=document.querySelectorAll('tbody tr')[0];
    if (cardsearch){
    cardsearch.querySelector('input').addEventListener('input',(items)=>{
    var Node=false;
    document.querySelectorAll('tbody td').forEach((item)=>{ 
    if (item.innerText == items.target.value.toString() ){Node=item.parentElement;}});
    if (Node != false){SwapingNode.after(Node);}
    });
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

}
