// Selecting elements
const userScoreEl = document.getElementById("user-score");
const computerScoreEl = document.getElementById("computer-score");
const resultTextEl = document.getElementById("result-text");
const choiceButtons = document.querySelectorAll(".choice");

// Initial scores
let userScore = 0;
let computerScore = 0;

// Function to generate computer's choice
function getComputerChoice() {
    const choices = ["rock", "paper", "scissors"];
    const randomIndex = Math.floor(Math.random() * choices.length);
    return choices[randomIndex];
}

// Function to determine the winner
function determineWinner(userChoice, computerChoice) {
    if (userChoice === computerChoice) return "draw";
    if (
        (userChoice === "rock" && computerChoice === "scissors") ||
        (userChoice === "paper" && computerChoice === "rock") ||
        (userChoice === "scissors" && computerChoice === "paper")
    ) {
        return "user";
    }
    return "computer";
}

// Function to update scores and display results
function playGame(userChoice) {
    const computerChoice = getComputerChoice();
    const winner = determineWinner(userChoice, computerChoice);

    if (winner === "user") {
        userScore++;
        resultTextEl.textContent = `You win! You chose ${userChoice}, and the computer chose ${computerChoice}.`;
    } else if (winner === "computer") {
        computerScore++;
        resultTextEl.textContent = `You lose! You chose ${userChoice}, and the computer chose ${computerChoice}.`;
    } else {
        resultTextEl.textContent = `It's a draw! Both you and the computer chose ${userChoice}.`;
    }

    userScoreEl.textContent = userScore;
    computerScoreEl.textContent = computerScore;
}

// Adding event listeners to buttons
choiceButtons.forEach(button => {
    button.addEventListener("click", () => {
        const userChoice = button.getAttribute("data-choice");
        playGame(userChoice);
    });
});
