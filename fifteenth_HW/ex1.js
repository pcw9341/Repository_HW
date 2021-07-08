var $ulElement = document.querySelector('ul');

$ulElement.addEventListener("click",(event) => {
    const $target = event.target;
    if($target.classList.contains('close')){
        var $parentTarget = $target.parentElement;
        $parentTarget.style.display = "none";
    }
    $target.classList.toggle('checked');
})

function newElement() {
    const inputValue = document.getElementById("myInput").value;
    const $liElement = `
        <li>
            ${inputValue}
            <span class="close">&#215;</span>
        </li>    
    `
    //ul 하위에 li tag 추가하기
    if (inputValue === '') {
        alert("You must write something!");
    } else {
        $ulElement.insertAdjacentHTML("Beforeend",$liElement);
    }
    document.getElementById("myInput").value = "";
}

function myFunction() {
    var element = document.body;
    element.classList.toggle("dark-mode");
    var header = document.getElementById("myDIV");
    header.classList.toggle("dark-header");
}

// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[1];

// When the user clicks on the button, open the modal
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

// 두번째 실습
function init() {
    let todoList = getTodoList('todoList');
    for(let i=0; i<todoList.length; i++){
        $liElement = `
            <li>
                <span>${todoList[i]}</span>
                <span class="close">&#215;</span>
            </li>
        `
        $ulElement.insertAdjacentHTML('beforeend', $liElement);
    }
}

function getTodoList(key) {
    return localStorage.getItem(key) ? localStorage.getItem(key).split(',') : [];
}

function addTodoList(key, value) {
    const todoList = getTodoList(key)
    return localStorage.setItem(key,[...todoList, value])
}

function deleteTodoList(key,value) {
    const todoList = getTodoList(key)
    return localStorage.setItem(key,todoList.filter(todo => todo !== value))
}

init()
