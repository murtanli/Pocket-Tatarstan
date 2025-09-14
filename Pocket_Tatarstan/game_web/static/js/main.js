import { getLevelData } from "./back_response.js";
import { startGame } from "./game.js";

// достаем ID уровня из URL
const pathParts = window.location.pathname.split("/");
const levelId = pathParts[pathParts.length - 2];

getLevelData(levelId).then(data => startGame(data));
