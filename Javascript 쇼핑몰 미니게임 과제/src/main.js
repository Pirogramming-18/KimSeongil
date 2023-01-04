// Fetch the items from the JSON file
function loadItems() {
  return fetch("data/data.json")
    .then((response) => response.json()) // JSON 으로 변환
    .then((json) => json.items); // JSON 안에 있는 items return
}

function displayItems(items) {
  const container = document.querySelector(".items");
  const html = items.map((item) => createHTMLString(item));
  console.log(html);
  container.innerHTML = items.map((item) => createHTMLString(item)).join("");
}

function createHTMLString(item) {
  return `
    <li class="item">
        <img src="${item.image}" alt="${item.type}" class="item__thumbnail" />
        <span class="item__description">${item.gender}, ${item.size}</span>
    </li>
    `;
}

// main
// promise가 성공적으로 아이템을 return하면..
// 그렇지 않으면 catch로 문제 파악
loadItems()
  .then((items) => {
    console.log(items);
    displayItems(items);
    // setEventListeners(items);
  })
  .catch(console.log);
