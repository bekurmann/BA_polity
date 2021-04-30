<template>
    <v-card>
        <v-card-title>Days in Parlament vs. Number of submitted Affairs</v-card-title>
        <v-card-text>
            <ScatterChart :data="scatterChartData" :options="scatterChartOptions" :height="250"></ScatterChart>
        </v-card-text>
    </v-card>
</template>
<script>
import ScatterChart from '~/components/ScatterChart.js'

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
            scatterChartData: {
                labels: this.MembershipsOW.map(memberships => memberships.politican.first_name),
                datasets: [
                    {
                        label: 'all',
                        //data: this.getScatterData,
                        data: this.getScatterData(),
                    },
                ]
            },
            scatterChartOptions: {
                responsive: true,
                legend: {
                    position: "top",
                },
                title: {
                    display: true,
                    text: 'days in parlament / number of submitted affairs',
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
                        scaleLabel: {
                            display: true,
                            labelString: 'number of days in parlament'
                        }
                    }],
                },
            }
        }
    },
    props: {
        MembershipsOW: {
            type: Array
        },
    },
    components: {
        ScatterChart,
    },
    methods: {
        getScatterData() {
            let scatterData = [];
            for (let i=0; i<this.MembershipsOW.length; i++) {
                let singleObj = {
                    x: this.MembershipsOW[i].politican.days_in_parlament, 
                    y: this.MembershipsOW[i].politican.number_of_submitted_affairs
                };
                scatterData.push(singleObj);
            }
            return scatterData
        },

    }
}
</script>