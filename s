document.getElementsByClassName('card-search')[0].querySelector('input').addEventListener('click',(items)=>{
var SwapingNode=document.querySelectorAll('.table-body tr')[0]
document.querySelectorAll('.table-body td').forEach((item)=>{ 
if (item.innerText == items.target.value.toString() ){ console.log(items.target);
item.parentElement.before(SwapingNode);}
});
});
  
                                