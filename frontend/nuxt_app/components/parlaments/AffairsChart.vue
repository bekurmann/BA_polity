<template>
    <v-card>
        <v-card-title>Chart</v-card-title>
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
                //labels: this.affairs.map(affairs => affairs.date_received),
                // wohl besser im backend
                datasets: [
                    {
                        label: 'All Affairs',
                        data: this.affairs.map(affairs => affairs.date_received)             
                    }
                ]
            },
            lineChartOptions: {
                responsive: true,
                legend: {
                    position: "top",
                },
                title: {
                    display: true,
                    text: 'Affairs OW 2018-2022',
                    position: 'top',
                    fontSize: 18,
                },
                scales: {
                    xAxes: [{
                        type : 'time',
                        time: {
                            unit: 'year'
                        }
                    }]
                },
            }
        }
    },
    props: {
        affairs: {
            type: Object
        },
    },
    components: {
        LineChart,
    }
}
</script>