let currentDate = new Date();
console.log(currentDate);

let timer;
let seconds = 0;

function updateTimer() {
    document.getElementById('timer').innerText = seconds + ' წამი';
    seconds++;
}

function startTimer() {
    if (!timer) {
        timer = setInterval(updateTimer, 1000);
    }
}

function stopTimer() {
    clearInterval(timer);
    timer = null;
}

function resetTimer() {
    stopTimer();
    seconds = 0;
    document.getElementById('timer').innerText = '0 წამი';
}