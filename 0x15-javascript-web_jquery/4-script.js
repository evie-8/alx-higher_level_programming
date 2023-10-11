function addClass () {
  $('header').toggleClass('red');
   $('header').toggleClass('green');
}

$('#toggle_header').click(addClass);
