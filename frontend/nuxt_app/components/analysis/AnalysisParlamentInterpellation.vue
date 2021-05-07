<template>
    <v-card>
        <v-card-title>Interpellation Discussions</v-card-title>
        <v-card-text>
            <PieChart :data="pieChartData" :options="pieChartOptions" :height="250"></PieChart>
        </v-card-text>
    </v-card>
</template>
<script>
import PieChart from '~/components/PieChart.js'

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
            pieChartData: {
                labels: this.analysisInterpellation.labels,
                datasets: [
                    {
                        backgroundColor: [
                            chartColors.yellow,
                            chartColors.green,
                            chartColors.red,
                        ],
                        data: [
                            this.analysisInterpellation.data_notDesired,
                            this.analysisInterpellation.data_desiredSuccess,
                            this.analysisInterpellation.data_desiredDeclined,
                        ]
                    },
                ]
            },
            pieChartOptions: {
                responsive: true,
                legend: {
                    position: "top",
                },
                title: {
                    display: true,
                    text: 'Interpellation Discussions Total',
                    position: 'top',
                    fontSize: 18,
                },
            }
        }
    },
    props: {
        analysisInterpellation: {
            type: Array
        },
    },
    components: {
        PieChart,
    },
}
</script>