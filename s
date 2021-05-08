document.getElementsByClassName('card-search')[0].querySelector('input').addEventListener('input',(items)=>{
var SwapingNode=document.querySelectorAll('tbody tr')[0];var Node=false;
document.querySelectorAll('tbody td').forEach((item)=>{ 
if (item.innerText == items.target.value.toString() ){Node=item.parentElement;}
});
if (Node != false){SwapingNode.before(Node);}
});
                                                             