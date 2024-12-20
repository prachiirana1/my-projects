// Quiz Timer
let timer = 60;
let timerInterval;

function startTimer() {
    timerInterval = setInterval(function() {
        if (timer > 0) {
            document.getElementById('timer').innerHTML = "Time Left: " + timer;
            timer--;
        } else {
            clearInterval(timerInterval);
            submitQuiz();  // Automatically submit quiz when timer reaches zero
        }
    }, 1000);
}

function submitQuiz() {
    // Get selected answers
    const form = document.getElementById('quizForm');
    const answers = {
        q1: form.q1.value,
        q2: form.q2.value,
        q3: form.q3.value
    };

    // Define correct answers
    const correctAnswers = {
        q1: '4',
        q2: '8',
        q3: 'Paris'
    };

    // Calculate score
    let score = 0;
    for (let key in answers) {
        if (answers[key] === correctAnswers[key]) {
            score++;
        }
    }

    // Show result
    document.getElementById('score').innerText = score + "/3";
    document.getElementById('quizForm').style.display = 'none';  // Hide the quiz form
    document.getElementById('result').style.display = 'block';  // Show the result
}

// Start the timer when the page loads
window.onload = function() {
    startTimer();
};
