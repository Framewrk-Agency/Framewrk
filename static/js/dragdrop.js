$( document ).ready(function() {

  var selection = '';
  $('[data-toggle="tooltip"]').tooltip({placement: "bottom"});

  function handleDragStop( event, ui ) {
    var offsetXPos = parseInt( ui.offset.left );
    var offsetYPos = parseInt( ui.offset.top );
    console.log( "Drag stopped!\n\nOffset: (" + offsetXPos + ", " + offsetYPos + ")\n");
  }




  $('.shape').draggable({
    cursor: 'grabbing',
    snap: '.dropzone',
    revert: "invalid",
    //snapTolerance: 20,
    snapMode: "inner"
  });

  $('.dropzone').droppable( {
    tolerance: "intersect",
    addClasses: true,
    hoverClass: "drop-hover",
    drop: function( event, ui ) {
      selection = $(this).attr('data-type');
      $( ".shape" ).position({
        my: "center",
        at: "center",
        of: this
      });
    },
    over: function( event, ui ) {
      $(this).closest( "li" ).addClass('label-highlight');
      $(this).next().addClass('hr-highlight');
    },
    out: function( event, ui ) {
      $(this).closest( "li" ).removeClass('label-highlight');
      $(this).next().removeClass('hr-highlight');
      $(this).next().removeClass('hr-selected');
      $(this).closest( "li" ).removeClass('label-selected');
      $('.nextquestion').removeClass('nextquestion-active');
    },
    drop: function( event, ui ) {
      $(this).next().removeClass('hr-highlight');
      $(this).next().addClass('hr-selected');
      $(this).closest( "li" ).removeClass('label-highlight');
      $(this).closest( "li" ).addClass('label-selected');
      $('.nextquestion').addClass('nextquestion-active');
    }
  });
});
