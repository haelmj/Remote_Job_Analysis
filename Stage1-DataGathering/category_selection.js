// Mock html:
// <div id='categories_chosen_chosen'>
//  <ul class='chosen-choices'>
//      <li class='search-choice'>
//          <span>arguments[0]</span>
//          <a class='search-choice-close' data-option-array-index='arguments[1]'></a>
//      </li>
//  ...existingchildNodes
//  </ul>
//  <div class="chosen-drop">
//      <ul class="chosen-results"> 
//          <li class="result-selected" data-option-array-index='arguments[1]'>arguments[0]</li>
//      </ul>
//  </div>
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

var category_to_select = document.createElement('li')
category_to_select.className = 'result-selected'
category_to_select.setAttribute('data-option-array-index', arguments[1])
category_to_select.innerText = arguments[0]
var chosen_results = document.querySelector('#categories_chosen_chosen > div > ul')
chosen_results.insertBefore(category_to_select, chosen_results.childNodes[0])

// select category via category drop-down
const values = { 'Design': '1', 
                'Programming': '2', 
                'Customer Support': '7', 
                'Copywriting': '5', 
                'DevOps and Sysadmin': '6', 
                'Sales and Marketing': '9', 
                'Management and Finance': '3', 
                'Product': '11' }
const category_drop_down = document.querySelector("#categories_chosen")
category_drop_down.value = values[arguments[0]]
