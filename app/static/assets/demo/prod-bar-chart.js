// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily =
  '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = "#292b2c";

// Bar Chart Example
var ctx = document.getElementById("newBarChart");
var myLineChart = new Chart(ctx, {
  type: "line",
  data: {
    labels: barChartData.dates,
    datasets: [
      {
        label: "Trucked Grade",
        lineTension: 0.3,
        // backgroundColor: "rgba(2255,255,255,0.8)",
        borderColor: "rgba(2,117,216,1)",
        pointRadius: 5,
        pointBackgroundColor: "rgba(2,117,216,1)",
        pointBorderColor: "rgba(255,255,255,0.8)",
        pointHoverRadius: 5,
        pointHoverBackgroundColor: "rgba(2,117,216,1)",
        pointHitRadius: 50,
        pointBorderWidth: 2,
        data: barChartData.actual,
      },
      {
        label: "Planned Grade",

        borderColor: "rgba(255, 0, 0, 1)",
        data: barChartData.grade,
        borderColor: "rgba(255,0,0,1)",
        pointRadius: 5,
        pointBackgroundColor: "rgba(255,0,0,1)",
        pointBorderColor: "rgba(255,255,255,0.8)",
        pointHoverRadius: 5,
        pointHoverBackgroundColor: "rgba(255,0,0,1)",
      },
      {
        label: "CIL Feed Grade",
        lineTension: 0.3,
        // backgroundColor: "rgba(61,238,74,0.3)",
        borderColor: "rgba(61,238,74,1)",
        pointRadius: 5,
        pointBackgroundColor: "rgba(61,238,74,1)",
        pointBorderColor: "rgba(255,255,255,0.8)",
        pointHoverRadius: 5,
        pointHoverBackgroundColor: "rgba(61,238,23746,1)",
        pointHitRadius: 50,
        pointBorderWidth: 2,
        data: barChartData.cil,
      },
      {
        label: "Reconciled Grade",
        lineTension: 0.3,
        // backgroundColor: "rgba(238,196,64,0.63)",
        borderColor: "rgba(238,196,64,1)",
        pointRadius: 5,
        pointBackgroundColor: "rgba(238,196,64,1)",
        pointBorderColor: "rgba(255,255,255,0.8)",
        pointHoverRadius: 5,
        pointHoverBackgroundColor: "rgba(238,196,64,1)",
        pointHitRadius: 50,
        pointBorderWidth: 2,
        data: barChartData.reconciled,
      },
    ],
  },
  options: {},
});
