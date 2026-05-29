const ctx = document.getElementById('financeChart');

if(ctx){

new Chart(ctx, {
    type: 'line',
    data: {
        labels: [
            '1 Mei',
            '7 Mei',
            '14 Mei',
            '21 Mei',
            '28 Mei'
        ],
        datasets: [
            {
                label: 'Pemasukan',
                data: [
                    2400000,
                    3800000,
                    4500000,
                    5200000,
                    6000000
                ],
                borderColor: '#00ff9d',
                backgroundColor: 'rgba(0,255,157,0.2)',
                tension: 0.4,
                fill: true
            },
            {
                label: 'Pengeluaran',
                data: [
                    1000000,
                    2000000,
                    2200000,
                    3000000,
                    3500000
                ],
                borderColor: '#ff3b5c',
                backgroundColor: 'rgba(255,59,92,0.2)',
                tension: 0.4,
                fill: true
            }
        ]
    },
    options: {
        responsive:true,
        plugins:{
            legend:{
                labels:{
                    color:'white'
                }
            }
        },
        scales:{
            y:{
                ticks:{
                    color:'white'
                },
                grid:{
                    color:'rgba(255,255,255,0.05)'
                }
            },
            x:{
                ticks:{
                    color:'white'
                },
                grid:{
                    color:'rgba(255,255,255,0.05)'
                }
            }
        }
    }
});

}

const pie = document.getElementById('pieChart');

if(pie){

new Chart(pie, {
    type:'doughnut',
    data:{
        labels:[
            'Makanan',
            'Transport',
            'Belanja',
            'Tagihan'
        ],
        datasets:[{
            data:[
                40,
                25,
                20,
                15
            ],
            backgroundColor:[
                '#00ff9d',
                '#0084ff',
                '#ff9900',
                '#b026ff'
            ]
        }]
    },
    options:{
        plugins:{
            legend:{
                labels:{
                    color:'white'
                }
            }
        }
    }
})

}
