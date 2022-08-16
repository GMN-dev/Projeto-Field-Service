(() => {
    'use strict'

    const marca = document.querySelector('#marca')
    const periferico = document.querySelector('#periferico')

    marca.innerHTML = "<option value='none'></option>"

    let headset = [
        { value: "Felitron", text: "Felitron" },
        { value: "TopUse", text: "TopUse" }
    ]

    let others = [
        { value: "Dell", text: "Dell" },
        { value: "Lenovo", text: "Lenovo" },
        { value: "Genérico", text: "Genérico" }
    ]

    periferico.onchange = event => {
        if (periferico.options[periferico.selectedIndex].value === 'Headset') {
            addOption(marca)
            headset.forEach(m => marca.add(new Option(m.text, m.value)))
        } else {
            addOption(marca)
            others.forEach(o => marca.add(new Option(o.text, o.value)))
        }
    }

    function addOption(element) {
        element.innerHTML = "<option value='none'></option>"
    }
})()