window.onload = function () {

    var bar = document.getElementById('bar');
    var pie = document.getElementById('pie');

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
    

    if (bar && pie){load_charts(bar.getContext('2d'),pie.getContext('2d'));}

    var MCQS = document.getElementsByClassName("MCQS")[0];
    var Subjective = document.getElementsByClassName("Subjective")[0];
    var Exam = document.getElementsByClassName("Exam")[0];

    if(MCQS && Subjective && Exam){typeof_paper(MCQS,Subjective,Exam);}    

}

function closeall(MCQS,Subjective,Exam){
    MCQS.style.display = 'none';Subjective.style.display = 'none';Exam.style.display = 'none';
}



function typeof_paper(MCQS,Subjective,Exam) {
    closeall(MCQS,Subjective,Exam);
    document.getElementsByClassName("papertype")[0].addEventListener("click", (event) => {
        
        var data = event.target.form; var type_paper = [];
        for (var i = 0; i < data.length - 1; i++) { type_paper.push(data[i].value);}
        var Totaltime=document.getElementById('Totaltime');
        var Starttime=document.getElementById('Starttime');
        

        if (Totaltime.value!="" && Starttime.value!=""){

        if (type_paper[0] == 'MCQS') {
            closeall(MCQS,Subjective,Exam);
            MCQS.style.display = 'flex';
        }
        else if (type_paper[0] == 'Subjective') {
            closeall(MCQS,Subjective,Exam);
            Subjective.style.display = 'flex';
        }
        else if (type_paper[0] == 'Exam') {
            closeall(MCQS,Subjective,Exam);
            Exam.style.display = 'flex';
        }
    }
    

    });
}




function load_charts(bar,pie) {
    let _data = JSON.parse(document.getElementById('dataJson').textContent);
    _labels=[];_marks=[];


    _data['data'].forEach(item => {_labels.push(item['regno_id']);_marks.push(item['marks']);});

    new Chart(bar, {
        type: 'bar',
        data: {labels: _labels,datasets: [{label :["Exam Result"],backgroundColor:'#ff6347',data:_marks}]},
        options:{scales:{ yAxes:[{ticks:{beginAtZero:true}}]}}
    });

    new Chart(pie, {
        type: 'doughnut',
        data: {
            labels: ["Pass", "Fail"],
            datasets: [{ 
            label:_labels,data: [ _data['pass'],  _data['fail'] ],backgroundColor: ['#ff6347', '#422232'], borderAlign: "center" }]
        }
    });
}