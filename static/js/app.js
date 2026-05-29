function saveTransaction(){

    const note = document.getElementById('note').value

    if(note === ''){
        alert('Isi transaksi')
        return
    }

    alert('Transaksi berhasil disimpan')
}
