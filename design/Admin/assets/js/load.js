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

    var bar = document.getElementById('bar').getContext('2d');
    var pie = document.getElementById('pie').getContext('2d');

    var chart = new Chart(bar, {
        type: 'bar',
        data: {
            labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
            datasets: [{
                label: 'Student Resuls', backgroundColor: '#ff6347',
                data: [5, 10, 5, 2, 20, 30, 45]
            }]
        }
    });


    var myChart = new Chart(pie, {
        type: 'doughnut',
        data: {
            labels: ["Pass", "Fail"],
            datasets: [{ data: [60, 40], backgroundColor: ['#ff6347', '#422232'], borderAlign: "center" }]
        }
    });

}