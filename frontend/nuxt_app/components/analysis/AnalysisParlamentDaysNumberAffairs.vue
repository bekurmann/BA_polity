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
                        label: 'sp',
                        //data: this.getScatterData,
                        data: this.getScatterData(1),
                        pointBackgroundColor: 'red',
                    },
                    {
                        label: 'csp',
                        //data: this.getScatterData,
                        data: this.getScatterData(2),
                        pointBackgroundColor: 'yellow',
                    },
                    {
                        label: 'svp',
                        //data: this.getScatterData,
                        data: this.getScatterData(3),
                        pointBackgroundColor: 'green',
                    },
                    {
                        label: 'fdp',
                        //data: this.getScatterData,
                        data: this.getScatterData(4),
                        pointBackgroundColor: 'blue',
                    },
                    {
                        label: 'cvp',
                        //data: this.getScatterData,
                        data: this.getScatterData(5),
                        pointBackgroundColor: 'orange',
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
                        scaleLabel: {
                            display: true,
                            labelString: 'number of submitted affairs'
                        }
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
        getScatterData(fractionID) {
            let scatterData = [];

            let membershipData = this.MembershipsOW.filter(el => el.politican.fractions[0].id == fractionID);

            for (let i=0; i<membershipData.length; i++) {

                if(membershipData[i].politican.fractions[0].id = fractionID) {
                    let singleObj = {
                        x: membershipData[i].politican.days_in_parlament, 
                        y: membershipData[i].politican.number_of_submitted_affairs
                    };
                    scatterData.push(singleObj);
                }
            }
            return scatterData
        },
    }
}
</script>