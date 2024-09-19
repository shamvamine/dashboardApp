
Chart.defaults.global.defaultFontFamily =
  '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = "#292b2c";

// Initialize Chart.js with fetched data
var ctx = document.getElementById("goldChart");
var myLineChart = new Chart(ctx, {
  type: "line",
  data: {
    labels: priceInfo.dates,
    datasets: [
      {
        label: "C1",
        lineTension: 0.3,
        backgroundColor: "rgba(0, 0, 0, 0)",  // No background
        borderColor: "rgba(2,117,216,1)",
        pointRadius: 5,
        pointBackgroundColor: "rgba(2,117,216,1)",
        pointBorderColor: "rgba(255,255,255,0.8)",
        pointHoverRadius: 5,
        pointHoverBackgroundColor: "rgba(2,117,216,1)",
        pointHitRadius: 50,
        pointBorderWidth: 2,
        data: priceInfo.c1_total,
      },
      {
        label: "C2",
        lineTension: 0.3,
        backgroundColor: "rgba(0, 0, 0, 0)",  // No background
        borderColor: "rgba(238,196,64,1)",
        pointRadius: 5,
        pointBackgroundColor: "rgba(238,196,64,1)",
        pointBorderColor: "rgba(255,255,255,0.8)",
        pointHoverRadius: 5,
        pointHoverBackgroundColor: "rgba(238,196,64,1)",
        pointHitRadius: 50,
        pointBorderWidth: 2,
        data: priceInfo.c2_total,
      },
      {
        label: "C3",
        lineTension: 0.3,
        backgroundColor: "rgba(0, 0, 0, 0)",  // No background
        borderColor: "rgba(61,238,74,1)",
        pointRadius: 5,
        pointBackgroundColor: "rgba(61,238,74,1)",
        pointBorderColor: "rgba(255,255,255,0.8)",
        pointHoverRadius: 5,
        pointHoverBackgroundColor: "rgba(61,238,74,1)",
        pointHitRadius: 50,
        pointBorderWidth: 2,
        data: priceInfo.c3_total,
      },
      {
        label: "C1 Budget",
        lineTension: 0.3,
        backgroundColor: "rgba(0, 0, 0, 0)",  // No background
        borderColor: "rgba(2,117,216,1)",
        pointRadius: 5,
        pointBackgroundColor: "rgba(2,117,216,1)",
        pointBorderColor: "rgba(255,255,255,0.8)",
        pointHoverRadius: 5,
        pointHoverBackgroundColor: "rgba(2,117,216,1)",
        pointHitRadius: 50,
        pointBorderWidth: 2,
        borderDash: [5, 5],  // Dotted line
        data: priceInfo.c1_budget,
      },
      {
        label: "C2 Budget",
        lineTension: 0.3,
        backgroundColor: "rgba(0, 0, 0, 0)",  // No background
        borderColor: "rgba(238,196,64,1)",
        pointRadius: 5,
        pointBackgroundColor: "rgba(238,196,64,1)",
        pointBorderColor: "rgba(255,255,255,0.8)",
        pointHoverRadius: 5,
        pointHoverBackgroundColor: "rgba(238,196,64,1)",
        pointHitRadius: 50,
        pointBorderWidth: 2,
        borderDash: [5, 5],  // Dotted line
        data: priceInfo.c2_budget,
      },
      {
        label: "C3 Budget",
        lineTension: 0.3,
        backgroundColor: "rgba(0, 0, 0, 0)",  // No background
        borderColor: "rgba(61,238,74,1)",
        pointRadius: 5,
        pointBackgroundColor: "rgba(61,238,74,1)",
        pointBorderColor: "rgba(255,255,255,0.8)",
        pointHoverRadius: 5,
        pointHoverBackgroundColor: "rgba(61,238,74,1)",
        pointHitRadius: 50,
        pointBorderWidth: 2,
        borderDash: [5, 5],  // Dotted line
        data: priceInfo.c3_budget,
      },
    ],
  },
  options: {
    // Add your chart options here
  },
});
