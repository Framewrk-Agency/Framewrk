$( document ).ready(function() {

  var selection = '';

  function handleDragStop( event, ui ) {
    var offsetXPos = parseInt( ui.offset.left );
    var offsetYPos = parseInt( ui.offset.top );
    console.log( "Drag stopped!\n\nOffset: (" + offsetXPos + ", " + offsetYPos + ")\n");
  }

  function handleDropEvent( event, ui ) {
    selection = $(this).attr('data-type');
    console.log(selection);
  }


  $('.shape').draggable({
    cursor: 'grabbing',
    snap: '.dropzone',
    revert: "invalid",
    snapTolerance: 20,
    snapMode: "inner",
    stop: handleDragStop
  });

  $('.dropzone').droppable( {
    tolerance: "intersect"
  });
});
