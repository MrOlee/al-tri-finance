const ctx = document.getElementById('financeChart')

if(ctx){

new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr'],
        datasets: [{
            label: 'Pengeluaran',
            data: [1200000, 900000, 1500000, 800000],
            borderWidth: 1
        }]
    }
})

}
