// path_to_your_external_js_file.js
Chart.defaults.global.defaultFontFamily =
  '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = "#292b2c";

// Initialize Chart.js with fetched data
var ctx = document.getElementById("TrammingChart");
var myLineChart = new Chart(ctx, {
  type: "line",
  data: {
    labels: chartInfo.dates,
    datasets: [
      {
        label: "Western Top",
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
        data: chartInfo.western_top,
      },
      {
        label: "Cymric Top",
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
        data: chartInfo.cymric_top,
      },
      {
        label: "Cymric Bottom",
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
        data: chartInfo.cymric_bottom,
      },
      {
        label: "13 Level",

        borderColor: "rgba(255, 0, 0, 1)",
        data: chartInfo.l_13,
        borderColor: "rgba(255,0,0,1)",
        pointRadius: 5,
        pointBackgroundColor: "rgba(255,0,0,1)",
        pointBorderColor: "rgba(255,255,255,0.8)",
        pointHoverRadius: 5,
        pointHoverBackgroundColor: "rgba(255,0,0,1)",
      },
      {
        label: "15 Level",
        lineTension: 0.3,
        // backgroundColor: "rgba(61,238,74,0.3)",
        borderColor: "rgba(38,127,134,1)",
        pointRadius: 5,
        pointBackgroundColor: "rgba(38,127,134,1)",
        pointBorderColor: "rgba(255,255,255,0.8)",
        pointHoverRadius: 5,
        pointHoverBackgroundColor: "rgba(38,127,134,1)",
        pointHitRadius: 50,
        pointBorderWidth: 2,
        data: chartInfo.l_15,
      },
      {
        label: "Far East",
        lineTension: 0.3,
        //backgroundColor: "rgba(124,20,225,0.8)",
        borderColor: "rgba(124,20,255,1)",
        pointRadius: 5,
        pointBackgroundColor: "rgba(124,20,225,1)",
        pointBorderColor: "rgba(255,255,255,0.8)",
        pointHoverRadius: 5,
        pointHoverBackgroundColor: "rgba(124,20,225,1)",
        pointHitRadius: 50,
        pointBorderWidth: 2,
        data: chartInfo.far_east,
      },

    ],
  },
  options: {
    // Add your chart options here
  },
});
