// per ora non funge

class HexCell {
    constructor(x, y, z) {
        this._x = x;
        this._y = y;
        this._z = z;
    }
}

// Create a HexCell at x=1, y=2, z=3.
let hexCell = new HexCell(1, 2, 3);

let hexGrid = initGrid(5);
drawGrid(hexGrid);

function HexCell(x, y, z) {
    this._x = x;
    this._y = y;
    this._z = z;
}

function initGrid(mapSize) {
    mapSize = Math.max(1, mapSize);
    let gridArray = [];
    let cnt = 0;

    for (let i = -mapSize; i < mapSize + 1; i += 1) {
        for (let j = -mapSize; j < mapSize + 1; j += 1) {
            for (let k = -mapSize; k < mapSize + 1; k += 1) {
                if (i + j + k == 0) {
                    gridArray.push(new HexCell(i, j, k));
                    cnt += 1;
                }
            }
        }
    }

    return gridArray;
}

function drawGrid(gridArray) {
    let edgeLength = 13;
    let edgeW = edgeLength * 3 / 2;
    let edgeH = edgeLength * Math.sqrt(3) / 2;

    let previewFrame = document.getElementById('hex_1_preview');
    let preview = previewFrame.contentDocument ||  previewFrame.contentWindow.document;
    let canvas = preview.getElementById('hex_1_canvas');
    canvas.width = canvas.width;
    let ctx = canvas.getContext('2d');
    ctx.fillStyle = 'lightgray';
    let x, y, z;
    let posX, posY;
    let centerX = canvas.width / 2;
    let centerY = canvas.height / 2;

    for (let i = 0; i < gridArray.length; i++) {
        [x, y, z] = [gridArray[i]._x, gridArray[i]._y, gridArray[i]._z];
        posX = x * edgeW + centerX;
        posY = (-y + z) * edgeH + centerY;

        ctx.moveTo(posX + Math.cos(0) * edgeLength,
                   posY + Math.sin(0) * edgeLength);
        for (let j = 1; j <= 6; j++) {
            ctx.lineTo(posX + Math.cos(j / 6 * (Math.PI * 2)) * edgeLength,
                       posY + Math.sin(j / 6 * (Math.PI * 2)) * edgeLength);
        }
        ctx.fill();
        ctx.stroke();
    }
}