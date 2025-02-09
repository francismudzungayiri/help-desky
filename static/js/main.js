alert('JS LOADED');


/*** DASHBOARD VERTICAL TABS  ***/
var vertical_tabs;
var content;


vertical_tabs = document.getElementsByClassName('vertical-tab')
content = document.getElementsByClassName('tabs');
tab_active = document.querySelector('.vertical-active')

for(i = 0; i < vertical_tabs.length; i++){
    vertical_tabs[i].addEventListener('click',()=>{
        tab_active.classList.remove('vertical-active')
        this.classList.add('vertical-active')
    })
}
/*** CHANGING CONTENT ON VERTICAL TABS  CLICK  ***/


