window.onload = function () {


    let card_item = document.getElementsByClassName("sidebar-btn");
    for (var i = 0; i < card_item.length - 1; i++) {
        if (card_item[i].nextElementSibling != null) {
            card_item[i].nextElementSibling.style.display = 'none';
            card_item[i].addEventListener("click", (event) => {
                var dis = event.target.parentElement.nextElementSibling;
                if (dis.style.display == "none") { dis.style.display = "block"; } else { dis.style.display = "none"; }
            });
        }
    }
    var path = document.URL.split('/');
    var page = path[path.length - 2].split('.')[0];

    var pages = ["Exams", "Papers", "Courses", "Results", "Students", "Signin", "Signup"];
    var present = false;

    for (var i = 0; i < 6; i++) { if (page == pages[i]) { present = true; } }


    if (!present) {
        load_charts();
    }
    else {
        // var close_node=document.getElementsByClassName("close")[0];
        // var open_node=document.getElementsByClassName("open")[0];
        // close(close_node);
        // open(open_node,close_node);
        typeof_paper();

    }
}

function closeall(MCQS,Subjective,Exam){
    MCQS.style.display = 'none';
    Subjective.style.display = 'none';
    Exam.style.display = 'none';
}

function typeof_paper() {
    var MCQS = document.getElementsByClassName("MCQS")[0];
    var Subjective = document.getElementsByClassName("Subjective")[0];
    var Exam = document.getElementsByClassName("Exam")[0];

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