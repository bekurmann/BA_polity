<template>
    <v-card>
        <v-card-title>Chart</v-card-title>
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
                labels: this.fractions.map(fraction => fraction.name),
                datasets: [
                    {
                        label: 'Fractions',
                        backgroundColor: [
                            chartColors.red,
                            chartColors.yellow,
                            chartColors.green,
                            chartColors.blue,
                            chartColors.orange
                        ],
                        data: this.fractions.map(fraction => fraction.number_of_active_members)                
                    }
                ]
            },
            pieChartOptions: {
                responsive: true,
                legend: {
                    position: "top",
                },
                title: {
                    display: true,
                    text: 'Fractions OW 2018-2022',
                    position: 'top',
                    fontSize: 18,
                },
            }
        }
    },
    props: {
        fractions: {
            type: Object
        },
    },
    components: {
        PieChart,
    }
}
</script>