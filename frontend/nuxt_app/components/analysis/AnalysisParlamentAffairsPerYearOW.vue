<template>
    <v-card>
        <v-card-title>Number of Affairs per year and fraction</v-card-title>
        <v-card-text>
            <LineChart :data="lineChartData" :options="lineChartOptions" :height="250"></LineChart>
        </v-card-text>
    </v-card>
</template>
<script>
import LineChart from '~/components/LineChart.js'

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
            lineChartData: {
                labels: this.numberOfAffairsPerYear.labels,
                segment: {
                    borderDash: ctx => skipped(ctx, [6, 6]),
                },
                datasets: [
                    {
                        label: 'all',
                        data: this.numberOfAffairsPerYear.data_all,
                        fill: false,      
                        borderColor: 'grey', 
                    },
                    {
                        label: 'SP',
                        data: this.numberOfAffairsPerYear.data_sp,
                        fill: false,      
                        borderColor: 'red',                      
                    },
                    {
                        label: 'CVP',
                        data: this.numberOfAffairsPerYear.data_cvp,
                        fill: false,      
                        borderColor: 'orange',                      
                    },
                    {
                        label: 'FDP',
                        data: this.numberOfAffairsPerYear.data_fdp,
                        fill: false,      
                        borderColor: 'blue',                      
                    },
                    {
                        label: 'SVP',
                        data: this.numberOfAffairsPerYear.data_svp,
                        fill: false,      
                        borderColor: 'green',                      
                    },
                    {
                        label: 'CSP',
                        data: this.numberOfAffairsPerYear.data_csp,
                        fill: false,      
                        borderColor: 'yellow',                      
                    },
                ]
            },
            lineChartOptions: {
                responsive: true,
                legend: {
                    position: "top",
                },
                title: {
                    display: true,
                    text: 'OW: Number of Affairs per year and fraction',
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
                            color: [
                                '', '', 'black', 'black', '', '', '',
                                'black', 'black', ''
                            ]
                        }
                    }],
                },
            }
        }
    },
    props: {
        numberOfAffairsPerYear: {
            type: Object
        },
    },
    components: {
        LineChart,
    }
}
</script>