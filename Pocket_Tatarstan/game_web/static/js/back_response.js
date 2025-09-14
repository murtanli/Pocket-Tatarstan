export async function getLevelData(levelId) {
    try {
        const response = await fetch(`/level_part_info/${levelId}/`);
        if (!response.ok) {
            throw new Error("Ошибка загрузки уровня");
        }
        return await response.json();
    } catch (err) {
        console.error("Ошибка API:", err);
        return null;
    }
}
