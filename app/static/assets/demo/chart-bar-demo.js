// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily =
  '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = "#292b2c";

// Bar Chart Example
var ctx = document.getElementById("myBarChart");
var myLineChart = new Chart(ctx, {
  type: "bar",
  data: {
    labels: chartData.labels,
    datasets: [
      {
        label: "Actual Spend",
        backgroundColor: "rgba(2,117,216,1)",
        borderColor: "rgba(2,117,216,1)",
        data:chartData.spend,
      },
      {
        label: "Planned Spend",
        backgroundColor: "rgba(185, 153, 50, 0.8)",
        borderColor: "rgba(10, 10, 10, 1)",
        data: chartData.plan,
      },
    ],
  },
  options: {
    scales: {
      xAxes: [
        {
          time: {
            unit: "month",
          },
          gridLines: {
            display: false,
          },
          ticks: {
            // maxTicksLimit: 6,
          },
        },
      ],
      yAxes: [
        {
          ticks: {
            min: 0,
            // max: ,
            // maxTicksLimit: ,
          },
          gridLines: {
            display: true,
          },
        },
      ],
    },
    legend: {
      display: true,
    },
  },
});
