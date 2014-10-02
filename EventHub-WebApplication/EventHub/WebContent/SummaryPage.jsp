<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@page import="utils.LocalizationHelper"%>
<!-- SummaryPage -->

<!DOCTYPE html>
<html lang="en" class="no-js demo-1">
<head>
<meta charset="UTF-8" />
<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EventHub</title>
<meta name="description" content="EventHub - Event Planning Made Simple" />
<meta name="keywords"
	content="event planning, birthday party, wedding planning, new year party" />
<meta name="author" content="Codrops" />

<script src="http://code.jquery.com/jquery-1.9.1.js"></script>
<link rel="stylesheet"
	href="http://code.jquery.com/ui/1.10.3/themes/smoothness/jquery-ui.css" />
<script src="http://code.jquery.com/ui/1.10.3/jquery-ui.js"></script>


<link rel="shortcut icon" href="../favicon.ico">
<link rel="stylesheet" type="text/css" href="css/default.css" />
<link rel="stylesheet" type="text/css" href="css/bookblock.css" />

<link rel="stylesheet" type="text/css" href="css/demo1.css" />
<link rel="stylesheet" type="text/css" href="css/style.css" />
<script src="js/modernizr.custom.js"></script>

<script src="js/jquerypp.custom.js"></script>
<script src="js/jquery.bookblock.js"></script>
<script src="js/slidercode.js"></script>
<script defer src="js/slideShow.js"></script>

<script src="js/registration.js"></script>
<script src="js/login.js"></script>
<script src="//connect.facebook.net/en_US/all.js"></script>
<script src="js/fb.js"></script>


<script type="text/javascript" src="js/DetailView.js"></script>


<!-- <script>
var param = (document.URL.split("?"))[1];
var pa = (document.URL.split("&"));
var languageString = pa[1].split("=")[1];
console.log("In summary lang is " + languageString);


</script>
 -->

<script>
	function viewSummary() {
		var param = (document.URL.split("?"))[1];

		var category = param.split("=");

		var categoryName = category[1];

		var audioString;

		if(categoryName === "birthday"){
			Stitle = "<h1 align=\"center\"> BirthDay Planning</h1>";
			Simages = "<img src=\"images/Birthday/finalbday1.png\" alt=\"Slide 1\" />"+
		    "<img src=\"images/Birthday/finalbday2.png\" alt=\"Slide 2\" />"+
		    "<img src=\"images/Birthday/finalbday3.png\" alt=\"Slide 3\" />"+
		    "<img src=\"images/Birthday/finalbday4.png\" alt=\"Slide 4\" />"+
		    "<img src=\"images/Birthday/finalbday5.png\" alt=\"Slide 5\" />"+
		    "<img src=\"images/Birthday/finalbday6.png\" alt=\"Slide 6\" />";  
		    audioString = "<audio controls autoplay loop ><source src=\"audio/HBDTune.mp3\" type=\"audio/mpeg\"></audio>";

		   
		}
	else if(categoryName === "wedding"){
			Stitle = "<h1 align=\"center\"> Wedding Planning</h1>";
			Simages = "<img src=\"images/Wedding/finalwed1.png\" alt=\"Slide 1\" />"+
		    "<img src=\"images/Wedding/finalwed2.png\" alt=\"Slide 2\" />"+
		    "<img src=\"images/Wedding/finalwed3.png\" alt=\"Slide 3\" />"+
		    "<img src=\"images/Wedding/finalwed4.png\" alt=\"Slide 4\" />"+
		    "<img src=\"images/Wedding/finalwed5.png\" alt=\"Slide 5\" />"+
		    "<img src=\"images/Wedding/finalwed6.png\" alt=\"Slide 6\" />"; 
		    audioString = "<audio controls autoplay loop ><source src=\"audio/wed.mp3\" type=\"audio/mpeg\"></audio>";

		}
	else if(categoryName === "common"){
		Stitle = "<h1 align=\"center\"> Wedding</h1>";
		Simages = "<img src=\"images/Wedding/finalwed1.png\" alt=\"Slide 1\" />"+
	    "<img src=\"images/Newyear/finalny3.png\" alt=\"Slide 3\" />"+
	    "<img src=\"images/Wedding/finalwed2.png\" alt=\"Slide 2\" />"+
	    "<img src=\"images/Birthday/finalbday5.png\" alt=\"Slide 5\" />"+
	    "<img src=\"images/Newyear/finalny4.png\" alt=\"Slide 4\" />"+

	    "<img src=\"images/Birthday/finalbday6.png\" alt=\"Slide 6\" />"; 
		
	    audioString = "<audio controls autoplay loop ><source src=\"audio/Wed.mp3\" type=\"audio/mpeg\"></audio>";

	}
	else{
			Stitle = "<h1 align=\"center\"> Christmas And NewYear Party Planning</h1>";
			Simages = "<img src=\"images/Newyear/finalny1.png\" alt=\"Slide 1\" />"+
		    "<img src=\"images/Newyear/finalny2.png\" alt=\"Slide 2\" />"+
		    "<img src=\"images/Newyear/finalny3.png\" alt=\"Slide 3\" />"+
		    "<img src=\"images/Newyear/finalny4.png\" alt=\"Slide 4\" />"+
		    "<img src=\"images/Newyear/finalny5.png\" alt=\"Slide 5\" />"+
		    "<img src=\"images/Newyear/finalny6.png\" alt=\"Slide 6\" />"; 
		    audioString = "<audio controls autoplay loop ><source src=\"audio/Christms.mp3\" type=\"audio/mpeg\"></audio>";

		}
		$("#slideShowImages").html(Simages);
		//$("#audioPlayer").html(audioString);
		
		
		getSummary();
	}

	function getSummary() {
		$
				.ajax({

					url : 'GetSummaryDetails',
					type : 'GET',
					
					success : function(data) {
						var result = data.responseText;

						var row1 = result.split("*");
						
						
	        			 if (data.status == 300)
							{
							document.getElementById('summarySpace').innerHTML = "<h2 align='center'> No, you don't have any event created yet. ";
							
							}
	        			 
	        			 else{

						var innrhtmlString = "";
						for (var i = 0; i < row1.length; i++) {

							var row2 = row1[i].split("|");
							var actual = "";

							var sum = 0;
							for (var j = 0; j < (row2.length - 1); j++) {

								var row3 = row2[j].split("$");
								
									
						
									 var eventNameAfterReplace = row3[0].replace(/%20/g,' '); 
								
										var sumString = "<details><summary id = \""+eventNameAfterReplace+"\"><b><font color='purple'>"
										+ eventNameAfterReplace + "</font></b></summary><ul>";

								actual += "<li> " + row3[1] + "                      .  .  .     $ "
										+ row3[2] + "</li>";

								sum += parseInt(row3[2]);
							}

							
							
							innrhtmlString += sumString + actual
									+ "<li><b><font color='#660066'> Total Cost          .  .  .  $ " + sum
									+ "</font></b></li></details></ul>"

						}

						document.getElementById('summarySpace').innerHTML = innrhtmlString;

					}
					}
				});

	}
</script>

</head>

<% 
System.out.println("session is redirect in selectionnnn "  +session.getAttribute("lang"));
LocalizationHelper helper = LocalizationHelper.getInstance(session.getAttribute("lang").toString(), getServletContext());
%>

<body onload="viewSummary()">

	<div id="wsb-canvas-template-page" class="wsb-canvas-page page"
		style="height: 1550px; margin: auto; width: 1019px; background-color: #ffffff; position: relative; margin-top: 0px">

		<div id="d_header">
			<div id="heading">

				<div class="left">
				<span class="s_heading">EventHub</span><br>
				<span class="s_heading" style="font-size: 14px; float:left">Birthday &#9679; Wedding &#9679; Christmas</span>
			</div>
			
		<div class="right">
				<div style="display:inline-block; vertical-align:top; margin-left:200pxx;">
				<a href="index.jsp" id="home" class="ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only" style="font-size: 14px; color: #561243;" data-inline="true">
				<span class="ui-button-text">Home</span>
				</a>
				<% Integer userId = (Integer)session.getAttribute("userId"); %>
				
				<a id="viewSummary" href="SummaryPage.jsp?categoryName=common" class="ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only" 
				style="font-size:14px;color: #561243;<%if(userId == null){ %>display:none; <% } %>" data-inline="true"; ><span class="ui-button-text">MyEvents</span></a>
				
				<a id="login-user" style="font-size: 14px; color: #561243; <%if( userId != null){ %>display:none; <% } %>" data-inline="true";>Login</a>
				<a id="logout-user" href="logOut.jsp" class="ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only" 
				style="font-size:14px;color: #561243;<%if(userId == null){ %>display:none; <% } %>" data-inline="true"; ><span class="ui-button-text">LogOut</span></a>
				<a id="create-user" style="font-size: 14px; color: #561243; <%if(userId != null){ %>display:none; <% } %>" data-inline="true">Register</a>
				<span id = "fblogin" style="data-inline:true; <%if(userId != null){ %>display:none; <%} %>">
  				<a href="javascript:login();"> <img src="img/fb-login.png"></a>
   				</span>
				</div>
				
   				
  			    <div id = "fblogout" style="display:inline-block;visibility:hidden;">
  			    <img style="data-inline:true;" id="profile_pic"/>
  			    <div style="display:inline-block;">
  			    <span id="profile_name" style="data-inline:true;font-size:12px;visibility:hidden;"></span><br/>
  			    <a href="javascript:logout();"><img src="img/facebook_logout_button.png"></a> 
 				</div> 			    	    
  			    </div>
  			   
  			</div>


			</div>
		</div>
		<br>
		<div class="container">

			<br>

			<div class="slideShowImages" id="slideShowImages"></div>

			<br>

			<h2 align="center"> &#9829; <%=helper.getText("myEvent")%> &#9829;</h2>
			<div id="summarySpace" style="margin-left: 50px;" height="1000"></div>


		</div>

	<div id="audioPlayer" align="center">
			<audio controls autoplay loop>
				<source src="audio/common.mp3" type="audio/mpeg">
				</audio>
	<br>
		<div class="d_footer">
			<span class="copyright">© 2013 EventHub Inc. All Rights Reserved. | </span>
			<a href="AboutUS.jsp?cateogry=common" >About Us </a> 
		</div>
		<br><br>

	</div>
</body>
</html>