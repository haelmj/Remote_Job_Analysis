// Mock html:
// <div id='categories_chosen_chosen'>
//  <ul class='chosen-choices'>
//      <li class='search-choice'>
//          <span>arguments[0]</span>
//          <a class='search-choice-close' data-option-array-index='arguments[1]'></a>
//      </li>
//  ...existingchildNodes
//  </ul>
// </div>

var item = document.createElement('li');
item.className = 'search-choice';
var span = document.createElement('span');
span.innerText = arguments[0];
var closeButton = document.createElement('a');
closeButton.className = 'search-choice-close';
closeButton.setAttribute('data-option-array-index', arguments[1])
item.appendChild(span);
item.appendChild(closeButton);
var selected_choices = document.querySelector("#categories_chosen_chosen > ul");
selected_choices.insertBefore(item, selected_choices.childNodes[0])