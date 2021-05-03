<template>
    <v-card>
        <v-card-title>Usage of Affair Types over Time</v-card-title>
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
                labels: this.numberOfAffairsTypesPerYear.labels_years,
                datasets: [
                    {
                        label: "inquiry",
                        data: this.numberOfAffairsTypesPerYear.data_inqui,
                        pointBackgroundColor: chartColors.orange,
                        backgroundColor: chartColors.orange, 
                        yAxisID: "y-axis-1",
                    },
                    {
                        label: "interpellation",
                        data: this.numberOfAffairsTypesPerYear.data_inter,
                        pointBackgroundColor: chartColors.blue,
                        backgroundColor: chartColors.blue, 
                        yAxisID: "y-axis-1",
                    },
                    {
                        label: "interpellation",
                        data: this.numberOfAffairsTypesPerYear.data_postu,
                        pointBackgroundColor: chartColors.green,
                        backgroundColor: chartColors.green, 
                        yAxisID: "y-axis-1",
                    },
                    {
                        label: "interpellation",
                        data: this.numberOfAffairsTypesPerYear.data_motio,
                        pointBackgroundColor: chartColors.red,
                        backgroundColor: chartColors.red, 
                        yAxisID: "y-axis-1",
                    },
                    {
                        label: "people's motion",
                        data: this.numberOfAffairsTypesPerYear.data_pmoti,
                        pointBackgroundColor: chartColors.yellow,
                        backgroundColor: chartColors.yellow, 
                        yAxisID: "y-axis-1",
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
                    text: 'title',
                    position: 'top',
                    fontSize: 18,
                },
                scales: {
                    xAxes: [{
                        stacked:true
                    }],
                    yAxes: [{
                        stacked:true,
                        type: "linear",
                        id: "y-axis-1"
                    }],
                }
            }
        }
    },
    props: {
        numberOfAffairsTypesPerYear: {
            type: Array
        },
    },
    components: {
        BarChart,
    },
}
</script>