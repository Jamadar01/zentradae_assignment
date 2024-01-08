// First Vertical Bar Chart
var ctx1 = document.getElementById('chart1').getContext('2d');
var chart1 = new Chart(ctx1, {
    type: 'bar',
    data: {
        labels: ['Everett', 'Seattle', 'Lynnwood', 'Bothell', 'Mukilteo', 'Edmonds'],
        datasets: [{
            label: 'Revenue for November 2019',
            data: [25000, 35000, 40000, 45000, 50000, 5000],
            backgroundColor: 'rgba(65,191,153,255)',
            
            borderWidth: 1
        }]
    },
    options: {
        indexAxis: 'y', // Display as vertical bar chart
        scales: {
            x: {
                beginAtZero: true
            }
        }
    }
});

// Second Vertical Bar Chart
var ctx2 = document.getElementById('chart2').getContext('2d');
var chart2 = new Chart(ctx2, {
    type: 'bar',
    data: {
        labels: ['Service Plumbing', 'Bid Work HVAC', 'Service HVAC', 'Bid Work Plumbing', 'HWT Replacement', 'Maintenance', 'Material Sale'],
        datasets: [{
            label: 'Revenue for November 2019',
            data: [0, 20000, 40000, 80000, 60000, 100000, 120000, 140000],
            backgroundColor: 'rgba(65,191,153,255)',
            
            borderWidth: 1
        }]
    },
    options: {
        indexAxis: 'y', // Display as vertical bar chart
        scales: {
            x: {
                beginAtZero: true
            }
        }
    }
});
