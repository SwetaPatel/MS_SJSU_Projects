$(function() {
    var name = $( "#name" );
    var  email = $( "#email" );
    var password = $( "#password" );
    
   var  allFields = $( [] ).add( name ).add( email ).add( password ),
      tips = $( ".validateTips" );
 /*
    function updateTips( t ) {
      tips
        .text( t )
        .addClass( "ui-state-highlight" );
      setTimeout(function() {
        tips.removeClass( "ui-state-highlight", 1500 );
      }, 500 );
    }
 
    function checkLength( o, n, min, max ) {
      if ( o.val().length > max || o.val().length < min ) {
        o.addClass( "ui-state-error" );
        updateTips( "Length of " + n + " must be between " +
          min + " and " + max + "." );
        return false;
      } else {
        return true;
      }
    }
 
    function checkRegexp( o, regexp, n ) {
      if ( !( regexp.test( o.val() ) ) ) {
        o.addClass( "ui-state-error" );
        updateTips( n );
        return false;
      } else {
        return true;
      }
    } */
 
    $( "#dialog-form" ).dialog({
      autoOpen: false,
      height: 350,
      width: 350,
      modal: true,
      buttons: {
    	 
        "Register": function() {
        	
        /*	
          var bValid = true;
          allFields.removeClass( "ui-state-error" );
 
          bValid = bValid && checkLength( name, "username", 3, 16 );
          bValid = bValid && checkLength( email, "email", 6, 80 );
          bValid = bValid && checkLength( password, "password", 5, 16 );
 
          bValid = bValid && checkRegexp( name, /^[a-z]([0-9a-z_])+$/i, "Username may consist of a-z, 0-9, underscores, begin with a letter." );
          // From jquery.validate.js (by joern), contributed by Scott Gonzalez: http://projects.scottsplayground.com/email_address_validation/
          bValid = bValid && checkRegexp( email, /^((([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+(\.([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+)*)|((\x22)((((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(([\x01-\x08\x0b\x0c\x0e-\x1f\x7f]|\x21|[\x23-\x5b]|[\x5d-\x7e]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(\\([\x01-\x09\x0b\x0c\x0d-\x7f]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))))*(((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(\x22)))@((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?$/i, "eg. ui@jquery.com" );
          bValid = bValid && checkRegexp( password, /^([0-9a-zA-Z])+$/, "Password field only allow : a-z 0-9" );
 
          if ( bValid ) {
            $( "#users tbody" ).append( "<tr>" +
              "<td>" + name.val() + "</td>" +
              "<td>" + email.val() + "</td>" +
              "<td>" + password.val() + "</td>" +
            "</tr>" );
        	
            $( this ).dialog( "close" );
          } */
        	
        	if((fname.value == null || fname.value=="")||(lname.value == null || lname.value=="")||(email_reg.value == null || email_reg.value=="")||(password_reg.value == null || password_reg.value=="")||(question.value == null || question.value=="")||(answer.value == null || answer.value=="")){
        		document.getElementById("error1").innerHTML = "Invalid Input.Please fill all the details";
        		return;
        	}
        	var user = {};
        	user.firstName = fname.value;
        	user.lastName = lname.value;
        	user.email = email_reg.value;
        	user.password = password_reg.value;
        	user.question = question.value;
        	user.answer = answer.value;
        	
        	var requestJson = JSON.stringify(user);
        	console.log("Json String: "+requestJson);

        	$.ajax({
        		url: "GetRegistrationDetails",
        		type: "POST",
        		context: document.body,
        		data: requestJson,
        		success: function(data){
        			if(data.errorCode == 200 && data.responseText == "Success"){
        				console.log("Registration sucess..!!");
        				$("#dialog-form").dialog( "close" );
        			}
        			else if (data.errorCode == 500)
        				{
        				document.getElementById("error1").innerHTML = "Email address already exists.";

        				}
        			else{
        				document.getElementById("error1").innerHTML = "Registration Failed.Try Again";
        			}
        		}
        	});
        	
        },
        Cancel: function() {
          $( this ).dialog( "close" );
          parent.reloadContent(); // added by Rohini
        }
      },
      close: function() {
        allFields.val( "" ).removeClass( "ui-state-error" ); 
        parent.reloadContent(); // added by Rohini
      } 
    });
 
    $( "#create-user" )
      .button()
      .click(function() {
        $( "#dialog-form" ).dialog( "open" );
      });
  });


//added by Rohini
function reloadContent() {
  location.reload();
}