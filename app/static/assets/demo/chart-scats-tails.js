// path_to_your_external_js_file.js
Chart.defaults.global.defaultFontFamily =
  '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = "#292b2c";

// Initialize Chart.js with fetched data
var ctx = document.getElementById("ScatsTailsAreaChart");
var myLineChart = new Chart(ctx, {
  type: "line",
  data: {
    labels: chartData.dates,
    datasets: [
      {
        label: "CIL",
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
        data: chartData.cil,
      },
      {
        label: "SCATS",       
        data: chartData.scats,
        borderColor: "rgba(255,0,0,1)",
        pointRadius: 5,
        pointBackgroundColor: "rgba(255,0,0,1)",
        pointBorderColor: "rgba(255,255,255,0.8)",
        pointHoverRadius: 5,
        pointHoverBackgroundColor: "rgba(255,0,0,1)",
      },
      {
        label: "GRG",
      
        // backgroundColor: "rgba(61,238,74,0.3)",
        borderColor: "rgba(61,238,74,1)",
        pointRadius: 5,
        pointBackgroundColor: "rgba(61,238,74,1)",
        pointBorderColor: "rgba(255,255,255,0.8)",
        pointHoverRadius: 5,
        pointHoverBackgroundColor: "rgba(61,238,23746,1)",        
        data: chartData.grg,
      },
      
    ],
  },
  options: {
    // Add your chart options here
  },
});
