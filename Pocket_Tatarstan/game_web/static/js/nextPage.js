const playPage = document.querySelector('.play_page');
const levelsPage = document.querySelector('.levels');
const infoPage = document.querySelector('.info');

document.getElementById('toLevels').addEventListener('click', (event) => {
  event.preventDefault();
  playPage.style.display = 'none';
  levelsPage.style.display = 'flex';
  infoPage.style.display = 'none';
});

document.getElementById('toPlay').addEventListener('click', (event) => {
  event.preventDefault();
  levelsPage.style.display = 'none';
  playPage.style.display = 'flex';
  infoPage.style.display = 'none';
});

document.getElementById('toInfo').addEventListener('click', (event) => {
  event.preventDefault();
  levelsPage.style.display = 'none';
  playPage.style.display = 'none';
  infoPage.style.display = 'flex';
});


const track = document.querySelector('.slider_track');
const slides = document.querySelectorAll('.level_list');
const prevBtn = document.querySelector('.prev');
const nextBtn = document.querySelector('.next');

let index = 0;

function updateSlider() {
  track.style.transform = `translateX(${-index * 100}%)`;
  prevBtn.classList.toggle('disabled', index === 0);
  nextBtn.classList.toggle('disabled', index === slides.length - 1);
}

prevBtn.addEventListener('click', (e) => {
  e.preventDefault();
  if (index > 0) {
    index--;
    updateSlider();
  }
});

nextBtn.addEventListener('click', (e) => {
  e.preventDefault();
  if (index < slides.length - 1) {
    index++;
    updateSlider();
  }
});

updateSlider();