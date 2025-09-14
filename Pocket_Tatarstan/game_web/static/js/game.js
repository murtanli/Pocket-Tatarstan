export function startGame(levelData) {
    if (!levelData) return;

    const playSpace = document.getElementById("play_space");
    const levelRect = playSpace.getBoundingClientRect();
    const levelWidth = levelRect.width;
    const levelHeight = levelRect.height;

    const levelImage = document.querySelector(".image_game");

    // позиция и размер картинки на экране
    const imgRect = levelImage.getBoundingClientRect();
    const imgLeft = imgRect.left;
    const imgTop = imgRect.top;
    const imgWidth = imgRect.width;
    const imgHeight = imgRect.height;

    const scaleX = imgWidth / levelImage.naturalWidth;
    const scaleY = imgHeight / levelImage.naturalHeight;

    levelData.objects.forEach(obj => {
        obj.parts.forEach(part => {
            const partDiv = document.createElement("div");
            partDiv.classList.add("part");
            partDiv.style.backgroundImage = `url(${part.image})`;

            const partX = part.center_x; // координата X из БД
            const partY = part.center_y; // координата Y из БД

            // загружаем реальные размеры изображения
            const img = new Image();
            img.src = part.image;
            img.onload = () => {
                partDiv.style.width = img.width / 1.58  + "vh";
                partDiv.style.height = img.height / 1.58 + "vh";

                // случайное стартовое положение (в меню)
                partDiv.style.left = Math.random() * (levelWidth - img.width) + "px";
                partDiv.style.top = Math.random() * (levelHeight - img.height) + "px";
            };

            // сохраняем координаты цели относительно картинки
            partDiv.dataset.targetX = imgLeft + partX * scaleX - partDiv.offsetWidth / 2;
            partDiv.dataset.targetY = imgTop + partY * scaleY - partDiv.offsetHeight / 2;

            // drag & drop
            partDiv.onmousedown = function(e) {
                const shiftX = e.clientX - partDiv.getBoundingClientRect().left;
                const shiftY = e.clientY - partDiv.getBoundingClientRect().top;

                function moveAt(pageX, pageY) {
                    partDiv.style.left = pageX - shiftX + "px";
                    partDiv.style.top = pageY - shiftY + "px";
                }

                function onMouseMove(e) {
                    moveAt(e.pageX, e.pageY);
                }

                document.addEventListener('mousemove', onMouseMove);

                partDiv.onmouseup = function() {
                    document.removeEventListener('mousemove', onMouseMove);
                    partDiv.onmouseup = null;

                    // проверяем близость к цели
                    const x = parseFloat(partDiv.style.left);
                    const y = parseFloat(partDiv.style.top);

                    const targetX = imgLeft + partX * scaleX - partDiv.offsetWidth / 2;
                    const targetY = imgTop + partY * scaleY - partDiv.offsetHeight / 2;

                    const distance = Math.hypot(x - targetX, y - targetY);
                    console.log(`x=${x} y=${y} targetX=${targetX} targetY=${targetY} distance=${distance}`);

                    if (distance < 30) {
                        partDiv.style.left = targetX + "px";
                        partDiv.style.top = targetY + "px";
                        xpartDiv.style.border = "2px solid green";

                        // можно пометить прогресс через AJAX
                        // savePartProgress(partDiv.dataset.partId)
                    }
                };
            };

            document.body.appendChild(partDiv);
        });
    });
}
