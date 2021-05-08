document.addEventListener('DOMContentLoaded', (event) => {

    let card_item = document.getElementsByClassName("sidebar-btn");
    for (var i = 0; i < 2; i++) {
        if (card_item[i].nextElementSibling != null) {
            card_item[i].nextElementSibling.style.display = 'none';
            card_item[i].addEventListener("click", (event) => {
                var dis = event.target.parentElement.nextElementSibling;
                if (dis.style.display == "none") { 
                dis.style.display = "block"; } 
                else { dis.style.display = "none"; }
            });
        }
    }

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


    var bar = document.getElementById('bar');
    var pie = document.getElementById('pie');

    if (bar && pie){load_charts(bar.getContext('2d'),pie.getContext('2d'));}
    var close_node = document.getElementsByClassName("close")[0];
    var open_node = document.getElementsByClassName("open")[0];
    
    if (close_node){close(close_node);}
    if (close_node && open_node){open(open_node,close_node);}
    

function close(close_node) {
    close_node.addEventListener("click", (event) => {
        event.target.parentElement.parentElement.parentElement.style.display = 'none';
    });
}

function open(open_node, close_node) {
    open_node.addEventListener("click", (event) => {
        close_node.parentElement.parentElement.parentElement.style.display = 'flex';
    });
}



function load_charts(bar ,pie) {
    let _data = JSON.parse(document.getElementById('dataJson').textContent);
    _labels=[];_marks=[];_papers=[];resultdata=[];var dataitem;
    totalstudent=[]

    

        _data['data'].forEach(item => {
            _labels.push(item['regno_id']);
            _marks.push(item['marks']);
        });


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
            datasets: [
                { data: [ _data['pass'],  _data['fail'] ],

            backgroundColor: ['#ff6347', '#422232'], borderAlign: "center" }]
        }
    });

}

});