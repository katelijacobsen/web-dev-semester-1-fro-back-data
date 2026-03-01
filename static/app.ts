// source:  https://medium.com/@dearpermatasari18/designing-input-fields-with-floating-labels-html-css-javascript-9a37bc81216d
const fields = document.querySelectorAll('.field input');


// Default State for the input fields
fields.forEach(input => {
    input.addEventListener('focus', () => {
        input.parentElement?.classList.add('active')
    })
    input.addEventListener('blur', () => {
        input.parentElement?.classList.remove('active')
    })
})


