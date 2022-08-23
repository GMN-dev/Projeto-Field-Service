(() => {
    'use strict'

    let t = document.querySelector('#tblsolicitacoes')
    
    Array.from(t.rows).forEach((tr, row_ind) => {
        console.log(tr.cells)
        Array.from(tr.cells).forEach((cell, col_ind) => {
            //console.log(cell.textContent)
            //console.log('Value at row/col [' + row_ind + ',' + col_ind + '] = ' + cell.textContent);
        });
    });
    
})()