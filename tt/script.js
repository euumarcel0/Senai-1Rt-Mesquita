document.addEventListener("DOMContentLoaded", function() {
    const gameContainer = document.getElementById("game");
    const gridSize = 19; // Tamanho do tabuleiro
    const numMines = 30; // Número de minas

    // Função para criar o tabuleiro
    function createGrid() {
        const grid = [];

        for (let row = 0; row < gridSize; row++) {
            grid[row] = [];
            for (let col = 0; col < gridSize; col++) {
                grid[row][col] = {
                    isMine: false,
                    isRevealed: false,
                    neighborCount: 0
                };
            }
        }

        // Posiciona as minas aleatoriamente no tabuleiro
        let minesPlaced = 0;
        while (minesPlaced < numMines) {
            const randomRow = Math.floor(Math.random() * gridSize);
            const randomCol = Math.floor(Math.random() * gridSize);

            if (!grid[randomRow][randomCol].isMine) {
                grid[randomRow][randomCol].isMine = true;
                minesPlaced++;
            }
        }

        // Calcula o número de minas vizinhas para cada célula
        for (let row = 0; row < gridSize; row++) {
            for (let col = 0; col < gridSize; col++) {
                if (!grid[row][col].isMine) {
                    grid[row][col].neighborCount = countNeighborMines(grid, row, col);
                }
            }
        }

        return grid;
    }

    // Função para contar o número de minas vizinhas
    function countNeighborMines(grid, row, col) {
        const neighborOffsets = [
            [-1, -1], [-1, 0], [-1, 1],
            [0, -1],           [0, 1],
            [1, -1],  [1, 0],  [1, 1]
        ];

        let count = 0;

        for (let i = 0; i < neighborOffsets.length; i++) {
            const offsetX = neighborOffsets[i][0];
            const offsetY = neighborOffsets[i][1];

            const neighborRow = row + offsetX;
            const neighborCol = col + offsetY;

            if (neighborRow >= 0 && neighborRow < gridSize && neighborCol >= 0 && neighborCol < gridSize) {
                if (grid[neighborRow][neighborCol].isMine) {
                    count++;
                }
            }
        }

        return count;
    }

    // Função para criar a representação visual do tabuleiro
    function renderGrid() {
        gameContainer.innerHTML = ""; // Limpa o conteúdo anterior

        for (let row = 0; row < gridSize; row++) {
            for (let col = 0; col < gridSize; col++) {
                const cell = document.createElement("div");
                cell.className = "cell";
                cell.dataset.row = row;
                cell.dataset.col = col;

                if (grid[row][col].isRevealed) {
                    cell.classList.add("revealed");

                    if (grid[row][col].isMine) {
                        cell.classList.add("mine");
                    } else {
                        cell.textContent = grid[row][col].neighborCount;
                    }
                }

                cell.addEventListener("click", handleCellClick);
                gameContainer.appendChild(cell);
            }
        }
    }

    // Função para lidar com o clique em uma célula
    function handleCellClick(event) {
        const row = parseInt(event.target.dataset.row);
        const col = parseInt(event.target.dataset.col);

        if (!grid[row][col].isRevealed) {
            grid[row][col].isRevealed = true;

            if (grid[row][col].isMine) {
                revealAllMines();
                alert("Você perdeu!");
            } else if (grid[row][col].neighborCount === 0) {
                revealNeighborCells(row, col);
            }

            if (checkWinCondition()) {
                alert("Parabéns! Você venceu!");
            }

            renderGrid();
        }
    }

    // Função para revelar células vizinhas quando a célula atual não tiver minas vizinhas
    function revealNeighborCells(row, col) {
        const neighborOffsets = [
            [-1, -1], [-1, 0], [-1, 1],
            [0, -1],           [0, 1],
            [1, -1],  [1, 0],  [1, 1]
        ];

        for (let i = 0; i < neighborOffsets.length; i++) {
            const offsetX = neighborOffsets[i][0];
            const offsetY = neighborOffsets[i][1];

            const neighborRow = row + offsetX;
            const neighborCol = col + offsetY;

            if (neighborRow >= 0 && neighborRow < gridSize && neighborCol >= 0 && neighborCol < gridSize) {
                if (!grid[neighborRow][neighborCol].isMine && !grid[neighborRow][neighborCol].isRevealed) {
                    grid[neighborRow][neighborCol].isRevealed = true;

                    if (grid[neighborRow][neighborCol].neighborCount === 0) {
                        revealNeighborCells(neighborRow, neighborCol);
                    }
                }
            }
        }
    }

    // Função para verificar se todas as células não-mine foram reveladas
    function checkWinCondition() {
        for (let row = 0; row < gridSize; row++) {
            for (let col = 0; col < gridSize; col++) {
                if (!grid[row][col].isMine && !grid[row][col].isRevealed) {
                    return false;
                }
            }
        }

        return true;
    }

    // Função para revelar todas as minas
    function revealAllMines() {
        for (let row = 0; row < gridSize; row++) {
            for (let col = 0; col < gridSize; col++) {
                if (grid[row][col].isMine) {
                    grid[row][col].isRevealed = true;
                }
            }
        }
    }

    // Inicializa o jogo
    const grid = createGrid();
    renderGrid();
});
