// Fetch the items from the JSON file
function loadItems() {
  return fetch('data/data.json')
    .then((response) => response.json()) // JSON 으로 변환
    .then((json) => json.items); // JSON 안에 있는 items return
}

// Update the list with the given items
function displayItems(items) {
  const container = document.querySelector('.items');
  const html = items.map((item) => createHTMLString(item));
  // console.log(html);
  container.innerHTML = items.map((item) => createHTMLString(item)).join('');
}

// Create HTML list item from the given data item
function createHTMLString(item) {
  return `
    <li class="item">
        <img src="${item.image}" alt="${item.type}" class="item__thumbnail" />
        <span class="item__description">${item.gender}, ${item.size}</span>
    </li>
    `;
}

// Button이 클릭되었을 때 발생하는 함수구나! -> 접두사 on 붙여주기
function onButtonClick(event, items) {
  const datset = event.target.dataset;
  const key = datset.key;
  const value = datset.value;

  if (key == null || value == null) {
    return;
  }

  displayItems(items.filter((item) => item[key] === value));

  // 조금 어려울 때는 변수로 선언한 다음에 확인하면서 진행
}

function setEventListeners(items) {
  const logo = document.querySelector('.logo');
  const buttons = document.querySelector('#buttons');
  logo.addEventListener('click', () => displayItems(items));
  buttons.addEventListener('click', (event) => onButtonClick(event, items));
}

// main
// promise가 성공적으로 아이템을 return하면..
// 그렇지 않으면 catch로 문제 파악
loadItems()
  .then((items) => {
    displayItems(items);
    setEventListeners(items);
  })
  .catch(console.log);
