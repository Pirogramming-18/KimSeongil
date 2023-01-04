// ++++++++++ stopwatch feature
// ---------- Variables ----------
const startButton = document.querySelector('#start');
const stopButton = document.querySelector('#stop');
const resetButton = document.querySelector('#reset');
const timer = document.querySelector('#timer__span');

let interval;
let isRunning = false;
let time = 0;
let allSelected = false;

// ---------- Functions ----------
function startTimer() {
  if (isRunning) return;
  isRunning = true;
  // 함수가 1초에 100번 실행?
  interval = setInterval(updateTimer, 10);
}

function stopTimer() {
  if (!isRunning) return;
  isRunning = false;
  clearInterval(interval);

  const timeRecord = document.createElement('li');
  const checkbox = document.createElement('input');
  const recordedTime = document.createElement('span');
  checkbox.type = 'checkbox';
  recordedTime.textContent = timer.textContent;
  timeRecord.appendChild(checkbox);
  timeRecord.appendChild(recordedTime);

  recordsList.appendChild(timeRecord);
}

function resetTimer() {
  stopTimer();
  overallSelection();
  deleteSelected();

  allSelected = false;
  timer.textContent = '00:00';
  time = 0;
}

function updateTimer() {
  time++;
  const seconds = Math.floor(time / 100)
    .toString()
    .padStart(2, '0');
  const milliseconds = (time % 100).toString().padStart(2, '0');
  timer.textContent = `${seconds}:${milliseconds}`;
}

startButton.addEventListener('click', startTimer);
stopButton.addEventListener('click', stopTimer);
resetButton.addEventListener('click', resetTimer);

// ++++++++++ Records feature
const recordsList = document.querySelector('#records__container');
const deleteButton = document.querySelector('.delete__records');
const overallSelectionButton = document.querySelector('.check__all');

// ---------- Functions ----------

function deleteSelected() {
  const checkboxes = recordsList.querySelectorAll('input[type="checkbox"]');
  const toDelete = [];
  for (let i = 0; i < checkboxes.length; i++) {
    if (checkboxes[i].checked) {
      toDelete.push(checkboxes[i]);
    }
  }
  toDelete.forEach((checkbox) => recordsList.removeChild(checkbox.parentElement));
}

function overallSelection() {
  allSelected = !allSelected;
  const checkboxes = recordsList.querySelectorAll('input[type="checkbox"]');
  checkboxes.forEach((checkbox) => (checkbox.checked = allSelected));
}

deleteButton.addEventListener('click', deleteSelected);
overallSelectionButton.addEventListener('click', overallSelection);
