function renderModal(id, collection) {
  var div = document.getElementById('modal-div');
  var button = document.getElementById("modal-submit");
  var modal = document.getElementById("modal");
  var input1 = document.createElement("input");
  input1.type = "hidden";
  input1.name = "id";
  input1.value = id;
  modal.insertBefore(input1, button);
  var input2 = document.createElement("input");
  input2.type = "hidden";
  input2.name = "collection";
  input2.value = collection;
  modal.insertBefore(input2, button);
  console.log('ok');
  div.style.display = 'block';
  return false;
}
