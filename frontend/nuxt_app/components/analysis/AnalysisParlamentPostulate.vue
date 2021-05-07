<template>
    <v-card>
        <v-card-title>Postulate Recommendation + Success</v-card-title>
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
                labels: this.analysisPostulate.labels,
                datasets: [
                    {
                        backgroundColor: [
                            "pink",
                            chartColors.orange,
                            chartColors.yellow,
                            chartColors.red,
                        ],
                        data: [
                            this.analysisPostulate.data_notRecommendedSuccess,
                            this.analysisPostulate.data_notRecommendedDeclined,
                            this.analysisPostulate.data_recommendedSuccess,
                            this.analysisPostulate.data_recommendedDeclined,
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
                    text: 'Postulate Recommendation + Success',
                    position: 'top',
                    fontSize: 18,
                },
            }
        }
    },
    props: {
        analysisPostulate: {
            type: Array
        },
    },
    components: {
        PieChart,
    },
}
</script>