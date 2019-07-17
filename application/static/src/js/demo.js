$(document).ready(function() {
  var answered = 0;

  function next_question() {
    var pathname = window.location.pathname;
    var question = pathname.split('/');
    question = question[question.length -2];
    var nextQuestion = parseInt(question, 10) + 1;
    setTimeout(function() {
      window.location.replace('/question/' + nextQuestion + '/')
    }, 2000);
  }


  $('.answer-button').on('click', function() {
    $('.answer').addClass('active');
    $('.answer-button').css('opacity', 0);
    $('.skip-button').css('opacity', 0);
    $('.answer-button').css('height', 0);
    $('.skip-button').css('height', 0);
    $('.answer-button').css('padding', 0);
    $('.skip-button').css('padding', 0);
  });

  $('.answer-option').on('click', function(event){
    answered = parseInt(event.target.id, 10);
    console.log(answered);
  });

  function showTooltip(event) {
    console.log(this);
    $(this).find('.answer-tooltip').toggleClass('tooltipActive');
  }

  $( '.answer-container' ).mouseenter( showTooltip ).mouseleave( showTooltip );

  $('#answer-submit').on('click', function(event){
    if (answered) {
      $('.explanation p').css('display', 'none');
      $('.answer-response.' + answered).css('display', 'inline');
      next_question();
    } else if ($('body').hasClass('question-freeform')) {
      $('.explanation p').css('display', 'none');
      $('.answer-response.' + answered).css('display', 'inline');
      next_question();
    }
  });

  $('.skip-button').on('click', function(){
    next_question()
  });
});
