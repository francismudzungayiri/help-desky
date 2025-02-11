
/*** DASHBOARD VERTICAL TABS  ***/

//var tab_btns = document.getElementsByClassName('tab-btn');

// Object.keys(tab_btns).forEach(key => {
//     let btn = tab_btns[key]
//     console.log(btn.innerHTML)
// })



/******  TABLE - ROW CLICKING   *******/

document.addEventListener('DOMContentLoaded', () => {
    const rows = document.querySelectorAll('tbody tr');
    rows.forEach(row => {
        row.addEventListener('click', () => {
            const id = row.getAttribute('data-id');
            window.location.href = `/details/${id}`;
        });
    });
});



let tab_btns = document.querySelectorAll('.tab-btn');
let tab_pane = document.querySelectorAll('.tab-pane');


tab_btns.forEach(btn =>{
    btn.addEventListener('click', ()=>{

        tab_btns.forEach(x =>  x.classList.remove('vertical-tab-active'));
        tab_pane.forEach(pane => pane.classList.remove('pane-active'))
        btn.classList.add('vertical-tab-active');

        let targetTab = btn.getAttribute('data-tab');
        console.log(targetTab)
        document.getElementById(targetTab).classList.add('pane-active')
    });
});



