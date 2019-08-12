$(document).ready(function() {
  var answered = 0;

  function next_question() {
    var pathname = window.location.pathname;
    var question = pathname.split('/');
    question = question[question.length - 2];
    var nextQuestion = parseInt(question, 10) + 1;
    window.location.replace('/question/' + nextQuestion + '/');
  }

  // User agrees to answer current question
  $('.answer-button').on('click', function() {
    $('.answer').addClass('active');
    $('.answer-button').css('opacity', 0);
    $('.skip-button').css('opacity', 0);
    $('.answer-button').css('height', 0);
    $('.skip-button').css('height', 0);
    $('.answer-button').css('padding', 0);
    $('.skip-button').css('padding', 0);
  });

  // User selects multiple choice answer
  $('.answer-option').on('click', function(event) {
    answered = parseInt(event.target.id, 10);
  });


  function showTooltip(event) {
    $(this).find('.answer-tooltip').toggleClass('tooltipActive');
  }

  $('.answer-container').mouseenter(showTooltip).mouseleave(showTooltip);

  $('#answer-submit').on('click', function(event) {
    if ($('body').hasClass('question-multiplechoice')) {
      if (answered) {
        $('.explanation .explanation-description').css('display', 'none');
        $('.answer-response.' + answered).css('display', 'inline');
      }
    } else if ($('body').hasClass('question-freeform')) {
      $('.explanation .explanation-description').css('display', 'none');
      $('.answer-response.' + answered).css('display', 'inline');
    }
    $('.answer-alert').css('display', 'inline');
    $(this).css('opacity', '0');
    $('#next-question').css('display', 'block');
  });

  $('#next-question').on('click', function(event) {
    next_question();
  });

  $('.skip-button').on('click', function() {
    next_question()
  });
});
