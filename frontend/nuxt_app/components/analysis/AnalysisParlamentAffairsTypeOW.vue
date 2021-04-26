<template>
    <v-card>
        <v-card-title>Number of Affairs per year and fraction</v-card-title>
        <v-card-text>
            <BarChart :data="barChartData" :options="barChartOptions" :height="250"></BarChart>
        </v-card-text>
    </v-card>
</template>
<script>
import BarChart from '~/components/BarChart.js'

const chartColors = {
  red: 'rgb(255, 99, 132)',
  orange: 'rgb(255, 159, 64)',
  yellow: 'rgb(255, 205, 86)',
  green: 'rgb(0, 153, 76)',
  blue: 'rgb(54, 162, 235)',
};

export default {
    data() {
        return {
            barChartData: {
                labels: this.numberOfAffairsTypes.labels,
                datasets: [
                    {
                        label: 'OW: Number of Affairs per Type',
                        data: this.numberOfAffairsTypes.data_all,
                        backgroundColor: [
                            chartColors.red,
                            chartColors.yellow,
                            chartColors.green,
                            chartColors.blue,
                            chartColors.orange
                        ],
                    },
                ]
            },
            barChartOptions: {
                responsive: true,
                legend: {
                    position: "top",
                },
                title: {
                    display: true,
                    text: 'OW: Number of Affairs per Type',
                    position: 'top',
                    fontSize: 18,
                },
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true,
                        },
                        // stacked: true,
                    }],
                    xAxes: [{
                        gridLines: {
                            //display: false,
                        }
                    }],
                },
            }
        }
    },
    props: {
        numberOfAffairsTypes: {
            type: Object
        },
    },
    components: {
        BarChart,
    }
}
</script>