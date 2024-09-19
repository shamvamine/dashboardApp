// path_to_your_external_js_file.js
Chart.defaults.global.defaultFontFamily =
  '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = "#292b2c";

// Initialize Chart.js with fetched data
var ctx = document.getElementById("newAreaChart");
var myLineChart = new Chart(ctx, {
  type: "line",
  data: {
    labels: chartData.dates,
    datasets: [
      {
        label: "R.O.M Tonnes",
        lineTension: 0.3,
        backgroundColor: "rgba(2,117,216,0.2)",
        borderColor: "rgba(2,117,216,1)",
        pointRadius: 5,
        pointBackgroundColor: "rgba(2,117,216,1)",
        pointBorderColor: "rgba(255,255,255,0.8)",
        pointHoverRadius: 5,
        pointHoverBackgroundColor: "rgba(2,117,216,1)",
        pointHitRadius: 50,
        pointBorderWidth: 2,
        data: chartData.rom,
      },
      {
        label: "Milled Tonnes",
        lineTension: 0.3,
        backgroundColor: "rgba(255,193,7,0.2)",
        borderColor: "rgba(255,193,7,1)",
        pointRadius: 5,
        pointBackgroundColor: "rgba(255,193,7,1)",
        pointBorderColor: "rgba(255,255,255,0.8)",
        pointHoverRadius: 5,
        pointHoverBackgroundColor: "rgba(255,193,7,1)",
        pointHitRadius: 50,
        pointBorderWidth: 2,
        data: chartData.milled_tonnage,
      },
      // {
      //   label: "Stock Pile",
      //   lineTension: 0.3,
      //   // backgroundColor: "rgba(61,238,74,0.3)",
      //   borderColor: "rgba(61,238,74,1)",
      //   pointRadius: 5,
      //   pointBackgroundColor: "rgba(61,238,74,1)",
      //   pointBorderColor: "rgba(255,255,255,0.8)",
      //   pointHoverRadius: 5,
      //   pointHoverBackgroundColor: "rgba(61,238,23746,1)",
      //   pointHitRadius: 50,
      //   pointBorderWidth: 2,
      //   data: chartData.stock_pile,
      // },
    ],
  },
  options: {
    // Add your chart options here
  },
});
