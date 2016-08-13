function renderModal(id, collection) {

  var div = document.getElementById('modal-div');
  var button = document.getElementById("modal-submit");
  var modal = document.getElementById("modal");
  var input1 = document.createElement("input");
  input1.type = "hidden";
  input1.name = "id";
  input1.value = id;
  input1.id = "idInfo";
  modal.insertBefore(input1, button);
  var input2 = document.createElement("input");
  input2.type = "hidden";
  input2.name = "collection";
  input2.value = collection;
  input2.id = "collectionInfo"
  modal.insertBefore(input2, button);
  div.className = "lightbox";
  return false;
}
function cancelModal(id, collection) {
  var div = document.getElementById('modal-div');
  var input1 = document.getElementById('idInfo');
  var input2 = document.getElementById("collectionInfo");
  var modal = document.getElementById("modal");
  modal.removeChild(input1);
  modal.removeChild(input2);

  div.className = "";
  return false;
}
