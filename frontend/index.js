const state = document.getElementById("state");
if (state.className == 'fancy-text-bad'){
    state.innerText = 'DOWN';
}
else{
    state.innerText = 'UP';
}



const ping = document.getElementById('ping');
const fixping = parseInt(ping);
if (fixping <= 20){
   ping.style.color = 'green';
}
else if(20 < fixping < 60){
    ping.style.color = 'orange';
}

else if(60 < fixping){
    ping.style.color = 'red';
}