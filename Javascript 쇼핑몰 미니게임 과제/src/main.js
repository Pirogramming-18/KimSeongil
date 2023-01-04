// Fetch the items from the JSON file
function loadItems() {
  return fetch("data/data.json")
    .then((response) => response.json()) // JSON 으로 변환
    .then((json) => json.items); // JSON 안에 있는 items return
}

// main
// promise가 성공적으로 아이템을 return하면..
// 그렇지 않으면 catch로 문제 파악
loadItems()
  .then((items) => {
    console.log(items);
    // displayItems(items);
    // setEventListeners(items);
  })
  .catch(console.log);
