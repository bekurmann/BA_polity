<template>
    <v-card>
        <v-card-title>Submitted Affairs per Politican</v-card-title>
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
                labels: this.getBarLabels(),
                datasets: [
                    {
                        label: "submitted affairs",
                        data: this.MembershipsOW.map(affair => affair.politican.number_of_submitted_affairs)
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
                    text: 'Usage of Affair Types over Time',
                    position: 'top',
                    fontSize: 18,
                },
                scales: {
                    xAxes: [{
                        scaleLabel: {
                            display: true,
                            labelString: 'number of submitted affairs'
                        }
                    }],
                    yAxes: [{
                        scaleLabel: {
                            display: true,
                            labelString: 'number of politicans'
                        }
                    }],
                }
            }
        }
    },
    props: {
        MembershipsOW: {
            type: Array
        },
    },
    components: {
        BarChart,
    },
    methods: {
        getBarData() {
            let barData = [];

            let membershipData = this.MembershipsOW;

            for (let i=0; i<membershipData.length; i++) {

                let singleObj = {

                }
            }

        },
        getBarLabels() {
            let barLabels = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14];

            //barLabels = this.MembershipsOW.map(affair => affair.politican.number_of_submitted_affairs)

            return barLabels
        },
    }
}
</script>