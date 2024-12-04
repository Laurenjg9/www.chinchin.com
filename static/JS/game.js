let score = 0;
const gameArea = document.getElementById("gameArea");
const player = document.getElementById("player");
const startButton = document.getElementById("startButton");
const scoreDisplay = document.getElementById("score");
let gameInterval;

startButton.addEventListener("click", startGame);

function startGame() {
    score = 0;
    scoreDisplay.textContent = score;
    startButton.disabled = true;
    player.style.left = "180px";
    gameInterval = setInterval(spawnItem, 1000);
    document.addEventListener("keydown", movePlayer);
    setTimeout(endGame, 30000); // Juego dura 30 segundos
}

function movePlayer(event) {
    const playerPos = player.offsetLeft;
    if (event.key === "ArrowLeft" && playerPos > 10) {
        player.style.left = playerPos - 20 + "px";
    } else if (event.key === "ArrowRight" && playerPos < 350) {
        player.style.left = playerPos + 20 + "px";
    }
}

function spawnItem() {
    const item = document.createElement("div");
    const isCoin = Math.random() > 0.5;
    item.classList.add("item", isCoin ? "coin" : "expense");
    item.style.left = Math.random() * 370 + "px";
    gameArea.appendChild(item);

    let fallInterval = setInterval(() => {
        const itemPos = item.offsetTop;
        if (itemPos >= 570) {
            clearInterval(fallInterval);
            gameArea.removeChild(item);
        } else if (isColliding(item, player)) {
            clearInterval(fallInterval);
            gameArea.removeChild(item);
            if (isCoin) {
                score++;
            } else {
                score = Math.max(0, score - 1);
            }
            scoreDisplay.textContent = score;
        } else {
            item.style.top = itemPos + 5 + "px";
        }
    }, 20);
}

function isColliding(a, b) {
    const aRect = a.getBoundingClientRect();
    const bRect = b.getBoundingClientRect();
    return !(
        aRect.top > bRect.bottom ||
        aRect.bottom < bRect.top ||
        aRect.left > bRect.right ||
        aRect.right < bRect.left
    );
}

function endGame() {
    clearInterval(gameInterval);
    document.removeEventListener("keydown", movePlayer);
    startButton.disabled = false;
    alert(`¡Juego terminado! Ahorraste ${score} monedas.`);
}