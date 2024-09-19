// path_to_your_external_js_file.js
Chart.defaults.global.defaultFontFamily =
  '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = "#292b2c";

// Initialize Chart.js with fetched data
var ctx = document.getElementById("goldChart");
var myBarChart = new Chart(ctx, {
  type: "bar",
  data: {
    labels: priceInfo.dates,
    datasets: [
      {
        label: "C1",
        backgroundColor: "rgba(2,117,216,0.5)",  // Semi-transparent blue
        borderColor: "rgba(2,117,216,1)",
        borderWidth: 1,
        data: priceInfo.c1_total,
      },
      {
        label: "C1 Budget",
        backgroundColor: "rgba(2,117,216,0.2)",  // Lighter semi-transparent blue
        borderColor: "rgba(2,117,216,1)",
        borderWidth: 1,
        borderDash: [5, 5],  // Dotted line effect for border
        data: priceInfo.c1_budget,
      },
      {
        label: "C2",
        backgroundColor: "rgba(238,196,64,0.5)",  // Semi-transparent yellow
        borderColor: "rgba(238,196,64,1)",
        borderWidth: 1,
        data: priceInfo.c2_total,
      },
      {
        label: "C2 Budget",
        backgroundColor: "rgba(238,196,64,0.2)",  // Lighter semi-transparent yellow
        borderColor: "rgba(238,196,64,1)",
        borderWidth: 1,
        borderDash: [5, 5],  // Dotted line effect for border
        data: priceInfo.c2_budget,
      },
      {
        label: "C3",
        backgroundColor: "rgba(61,238,74,0.5)",  // Semi-transparent green
        borderColor: "rgba(61,238,74,1)",
        borderWidth: 1,
        data: priceInfo.c3_total,
      },
      {
        label: "C3 Budget",
        backgroundColor: "rgba(61,238,74,0.2)",  // Lighter semi-transparent green
        borderColor: "rgba(61,238,74,1)",
        borderWidth: 1,
        borderDash: [5, 5],  // Dotted line effect for border
        data: priceInfo.c3_budget,
      },
    ],
  },
  options: {
    scales: {
      xAxes: [{
        barPercentage: 0.4,  // Adjust bar width
        categoryPercentage: 0.5,
        scaleLabel: {
          display: true,
          labelString: 'Date',
        },
        gridLines: {
          display: false,
        },
      }],
      yAxes: [{
        ticks: {
          beginAtZero: true,
        },
        scaleLabel: {
          display: true,
          labelString: 'Cost',
        },
      }],
    },
    tooltips: {
      callbacks: {
        label: function(tooltipItem, data) {
          var label = data.datasets[tooltipItem.datasetIndex].label || '';
          return label + ': ' + tooltipItem.yLabel;
        }
      }
    },
  },
});
// path_to_your_external_js_file.js