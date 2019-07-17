$(document).ready(function() {

  data = {
    datasets: [{
      data: [10, 20, 30]
    }],

    // These labels appear in the legend and in the tooltips when hovering different arcs
    labels: [
      'Red',
      'Yellow',
      'Blue'
    ]
  };

  new Chart(ctx, {
    data: data,
    type: 'polarArea',
    options: options
  });
});
