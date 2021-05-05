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

    var path =new URL(document.URL).pathname
    var pages=path.split('/')
    var page=pages[pages.length-2]


    if (page=="Admin") {
        load_charts();
    }
    else {
        var close_node = document.getElementsByClassName("close")[0];
        var open_node = document.getElementsByClassName("open")[0];
        close(close_node);
        open(open_node, close_node);
    }
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
    _labels=[];_marks=[];_papers=[];resultdata=[];var dataitem;
    totalstudent=[]

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
            datasets: [
                { data: [ _data['pass'],  _data['fail'] ],

            backgroundColor: ['#ff6347', '#422232'], borderAlign: "center" }]
        }
    });

}