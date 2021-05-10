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

import regression from 'regression'

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
                //labels: this.MembershipsOW.map(memberships => memberships.politican.first_name + ' ' + memberships.politican.last_name),
                type: 'scatter',
                datasets: [
                    {
                        label: 'sp',
                        labels: this.getScatterLabels(1),
                        data: this.getScatterData(1),
                        pointBackgroundColor: chartColors.red,
                        backgroundColor: chartColors.red, 
                    },
                    {
                        label: 'csp',
                        data: this.getScatterData(2),
                        labels: this.getScatterLabels(2),
                        pointBackgroundColor: chartColors.yellow,
                        backgroundColor: chartColors.yellow, 
                    },
                    {
                        label: 'svp',
                        data: this.getScatterData(3),
                        labels: this.getScatterLabels(3),
                        pointBackgroundColor: chartColors.green,
                        backgroundColor: chartColors.green, 
                    },
                    {
                        label: 'fdp',
                        data: this.getScatterData(4),
                        labels: this.getScatterLabels(4),
                        pointBackgroundColor: chartColors.blue,
                        backgroundColor: chartColors.blue, 
                    },
                    {
                        label: 'cvp',
                        data: this.getScatterData(5),
                        labels: this.getScatterLabels(5),
                        pointBackgroundColor: chartColors.orange,
                        backgroundColor: chartColors.orange, 
                    },
                    {
                        label: 'regression',
                        data: this.getRegressionData(),
                        type: 'line',
                    }

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
                tooltips: {
                    callbacks: {
                        label: function(tooltipItem, data) {
                        var dataset = data.datasets[tooltipItem.datasetIndex];
                        var index = tooltipItem.index;
                        return dataset.labels[index] + ': (' + tooltipItem.xLabel + ', ' + tooltipItem.yLabel + ')';
                        }
                    }
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
        ScatterChart,
    },
    methods: {
        getScatterData(fractionID) {
            let scatterData = [];

            let membershipData = this.MembershipsOW.filter(el => el.politican.fractions[0].id == fractionID);

            for (let i=0; i<membershipData.length; i++) {

                let singleObj = {
                    x: membershipData[i].politican.days_in_parlament, 
                    y: membershipData[i].politican.number_of_submitted_affairs
                };
                scatterData.push(singleObj);
            }
            return scatterData
        },
        getScatterLabels(fractionID) {
            let scatterLabels = [];
            let membershipData = this.MembershipsOW.filter(el => el.politican.fractions[0].id == fractionID);
            
            for (let i=0; i<membershipData.length; i++) {
                let label = membershipData[i].politican.first_name + ' ' + membershipData[i].politican.last_name;
                scatterLabels.push(label);
            }
            return scatterLabels
        },
        getRegressionData() {
            let regressionData = this.MembershipsOW.map(
                membership => {
                return [membership.politican.days_in_parlament, membership.politican.number_of_submitted_affairs];
            });

            console.log(regressionData);

            const regressionResult = regression.linear(regressionData);



            console.log(regressionResult);

            const regressionPoints = regressionResult.points.map(([x, y]) => {
                return {x,y}
            });

            console.log(regressionPoints);

            return regressionPoints
        }
    }
}
</script>