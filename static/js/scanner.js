async function scanReceipt(){

    const file = document.getElementById('receipt').files[0]

    if(!file){
        alert('Pilih gambar struk')
        return
    }

    const result = await Tesseract.recognize(
        file,
        'eng'
    )

    document.getElementById('result').innerText = result.data.text
}
