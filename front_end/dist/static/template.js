const menu_btn = document.querySelector('#menu_btn');
const menu_box = document.querySelector('#menu_box');

menu_btn.addEventListener('click', () => {
  if (menu_box.classList.contains('d-none')) {
    menu_box.classList.add('d-block');
    menu_box.classList.remove('d-none')
  } else {
    menu_box.classList.add('d-none');
  }
});