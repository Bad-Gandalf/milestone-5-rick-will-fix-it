
$(document).ready(function() {
            $('.reply-btn').click(function() {
                $(this).parent().parent().parent().parent().next('.replied-comments').fadeToggle();

            });
            $( function() {
			    $("#id_date_of_birth").datepicker({
			      changeMonth: true,
			      changeYear: true,
			      yearRange: "1900:2018",
			      dateFormat: 'yy-mm-dd',
     

    });
  } );
});
