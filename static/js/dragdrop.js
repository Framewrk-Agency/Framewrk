$( document ).ready(function() {


  function handleDragStop( event, ui ) {
    var offsetXPos = parseInt( ui.offset.left );
    var offsetYPos = parseInt( ui.offset.top );
    alert( "Drag stopped!\n\nOffset: (" + offsetXPos + ", " + offsetYPos + ")\n");
  }

  function handleDropEvent( event, ui ) {
    alert(this + " got dropped");
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
