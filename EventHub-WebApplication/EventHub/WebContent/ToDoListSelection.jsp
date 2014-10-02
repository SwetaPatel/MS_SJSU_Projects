<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
    <%@page import="utils.LocalizationHelper"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html lang="en" class="no-js demo-1">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Select To do list items</title>
<script src="http://code.jquery.com/jquery-1.9.1.js"></script>
<script src="http://code.jquery.com/ui/1.10.3/jquery-ui.js"></script>	
	<link rel="stylesheet" href="http://code.jquery.com/ui/1.10.3/themes/smoothness/jquery-ui.css" />
	
	
	<link rel="shortcut icon" href="../favicon.ico">
	<link rel="stylesheet" type="text/css" href="css/default.css" />
	<link rel="stylesheet" type="text/css" href="css/bookblock.css" />

	<link rel="stylesheet" type="text/css" href="css/demo1.css" />
	<link rel="stylesheet" type="text/css" href="css/style.css" />
	<script src="js/modernizr.custom.js"></script> 
	<script src="js/modernizr.js"></script>

	<script src="js/jquerypp.custom.js"></script>
	<script src="js/jquery.bookblock.js"></script>
	<script src="js/slidercode.js"></script>

	<script src="js/registration.js"></script>
	<script src="js/login.js"></script>
	<script src="//connect.facebook.net/en_US/all.js"></script>
	<script src="js/fb.js"></script>
	<script src="js/forgotPassword.js"></script>


<% 
System.out.println("session is redirect in selectionnnn "  +session.getAttribute("lang"));
LocalizationHelper helper = LocalizationHelper.getInstance(session.getAttribute("lang").toString(), getServletContext());
%>


<script defer src="js/slideShow.js"></script>
<link rel="stylesheet" type="text/css" href="http://skfox.com/jqExamples/jq14_jqui172_find_bug/jq132/css/ui-lightness/jquery-ui-1.7.2.custom.css">

<script>
var value;
function fetchData(){
	//alert(document.URL);
	var param = (document.URL.split("?"))[1];	
	var pa = (document.URL.split("&"));
    //languageString = pa[1].split("=")[1];
	//console.log("In selection lang is " + languageString);
	value = param.split("=")[1];
	//alert(value);
	var title;
	
	var audioString;
	
	if(value === "birthday"){
			Stitle = "<h1 align=\"center\"> BirthDay</h1>";
			Simages = "<img src=\"images/Birthday/finalbday1.png\" alt=\"Slide 1\" />"+
		    "<img src=\"images/Birthday/finalbday2.png\" alt=\"Slide 2\" />"+
		    "<img src=\"images/Birthday/finalbday3.png\" alt=\"Slide 3\" />"+
		    "<img src=\"images/Birthday/finalbday4.png\" alt=\"Slide 4\" />"+
		    "<img src=\"images/Birthday/finalbday5.png\" alt=\"Slide 5\" />"+
		    "<img src=\"images/Birthday/finalbday6.png\" alt=\"Slide 6\" />";  
		    
		    
		    audioString = "<audio controls autoplay loop ><source src=\"audio/HBDTune.mp3\" type=\"audio/mpeg\"></audio>";
		   
	}
	else if(value === "wedding"){
			Stitle = "<h1 align=\"center\"> Wedding</h1>";
			Simages = "<img src=\"images/Wedding/finalwed1.png\" alt=\"Slide 1\" />"+
		    "<img src=\"images/Wedding/finalwed2.png\" alt=\"Slide 2\" />"+
		    "<img src=\"images/Wedding/finalwed3.png\" alt=\"Slide 3\" />"+
		    "<img src=\"images/Wedding/finalwed4.png\" alt=\"Slide 4\" />"+
		    "<img src=\"images/Wedding/finalwed5.png\" alt=\"Slide 5\" />"+
		    "<img src=\"images/Wedding/finalwed6.png\" alt=\"Slide 6\" />"; 
		    
		    audioString = "<audio controls autoplay loop ><source src=\"audio/wed.mp3\" type=\"audio/mpeg\"></audio>";

		}
	else if(value === "common"){
		Stitle = "<h1 align=\"center\"> Wedding</h1>";
		Simages = "<img src=\"images/Wedding/finalwed1.png\" alt=\"Slide 1\" />"+
	    "<img src=\"images/Newyear/finalny3.png\" alt=\"Slide 3\" />"+
	    "<img src=\"images/Wedding/finalwed2.png\" alt=\"Slide 2\" />"+
	    "<img src=\"images/Birthday/finalbday5.png\" alt=\"Slide 5\" />"+
	    "<img src=\"images/Newyear/finalny4.png\" alt=\"Slide 4\" />"+

	    "<img src=\"images/Birthday/finalbday6.png\" alt=\"Slide 6\" />";  
	    
	    audioString = "<audio controls autoplay loop ><source src=\"audio/common.mp3\" type=\"audio/mpeg\"></audio>";

	}
	else{
			Stitle = "<h1 align=\"center\"> Christmas and New Year</h1>";
			Simages = "<img src=\"images/Newyear/finalny1.png\" alt=\"Slide 1\" />"+
		    "<img src=\"images/Newyear/finalny2.png\" alt=\"Slide 2\" />"+
		    "<img src=\"images/Newyear/finalny3.png\" alt=\"Slide 3\" />"+
		    "<img src=\"images/Newyear/finalny4.png\" alt=\"Slide 4\" />"+
		    "<img src=\"images/Newyear/finalny5.png\" alt=\"Slide 5\" />"+
		    "<img src=\"images/Newyear/finalny6.png\" alt=\"Slide 6\" />"; 
		    
		    audioString = "<audio controls autoplay loop ><source src=\"audio/Christms.mp3\" type=\"audio/mpeg\"></audio>";

		}
	$("#title").html(Stitle);
	
	$("#slideShowImages").html(Simages);
	$("#audioPlayer").html(audioString);

	
	getToDoList(value);	
	}
	
	
	function getToDoList(para){
		//alert("my para is" + para);
		if(Modernizr.sessionstorage){
			var result="";
			
			var events = sessionStorage.getItem(value+"Events");
			//alert("events var value: "+ events);
			if(events === null || events === ""){
				//alert("in if condition");
				$.ajax({
					type: 'get',		    
					url: '/EventHub/GetToDoListItems',
					data: 'item='+para,
					success: function(data) {			    

						result = data.responseText;

					   // alert("in if condition result is"+result);

						sessionStorage.setItem(value+"Events", result);
						//alert("my result is: " + result);
						var rows = result.split("|");
					   // alert("rows"+rows);
						var column = [];
						var list = "";
						for(var i = 0; i < rows.length;i++){
							column = rows[i].split("$");
							//alert("column"+column);
							list += "<li id=\"" + column[0]+"$"+column[1]+"$"+column[2] + "\" style=\"opacity: 1; z-index: 0;\">"+column[1]+"</li>";					
						 }				 
						 //alert(list);
						$("#sortable1").html(list);
					}
				});
			}
			else{
				//alert("in else condition");
				result = events;
				//alert("in else condition result is"+result);
				var rows = result.split("|");
				//alert("rows"+rows);
				var column = [];
				var list = "";
				for(var i = 0; i < rows.length;i++){
					column = rows[i].split("$");
					//alert("column"+column);
					list += "<li id=\"" + column[0]+"$"+column[1]+"$"+column[2] + "\" style=\"opacity: 1; z-index: 0;\">"+column[1]+"</li>";					
				 }				 
				 //alert(list);
				$("#sortable1").html(list);
			}	
		}else{
			alert("Session storage is not supported. WebSite will always fetch data from Database only.");
			$.ajax({
			    type: 'get',		    
		    	url: '/EventHub/GetToDoListItems',
			    data: 'item='+para,
			    success: function(data) {			    

				    result = data.responseText;

				   // alert("in if condition result is"+result);

				    //sessionStorage.setItem(value+"Events", result);
				    //alert("my result is: " + result);
				    var rows = result.split("|");
				   // alert("rows"+rows);
				    var column = [];
				    var list = "";
				    for(var i = 0; i < rows.length;i++){
						column = rows[i].split("$");
						//alert("column"+column);
						list += "<li id=\"" + column[0]+"$"+column[1]+"$"+column[2] + "\" style=\"opacity: 1; z-index: 0;\">"+column[1]+"</li>";					
					 }				 
					 //alert(list);
				    $("#sortable1").html(list);
			    }
			});
		}
	}
</script>
<script defer language="JavaScript" type="text/javascript">	
	
	$(function() {
		$("ul.droptrue").sortable({
			connectWith: 'ul',
			opacity: 0.6,
			update : updatePostOrder
		});

		$("#sortable1, #sortable2").disableSelection();
		$("#sortable1, #sortable2").css('minHeight',$("#sortable1").height()+"px");
		updatePostOrder();
	});
	
	function updatePostOrder() { 
		var arr = [];
	  $("#sortable2 li").each(function(){		 
	    arr.push($(this).attr('id'));
	  });
	  res = arr.join('|');
	  //alert(res);
	  $('#postOrder').val(arr.join('|'));
  }  
	function submitData(){
		var eventName = $("#event_name").val();
		//alert("Result: " + res + " " + "eventname: "+ eventName);
		//alert("new check:" + value);
		if(res === "" || eventName === ""){
			alert("Please Enter Event name and select atleast one Task list item.")
			}
		else{
			window.location.href = "ToDoListDetails.jsp?action="+res+"&eventName="+eventName+"&event="+value;
			}
		
		
	}
</script>


</head>
<body onload="fetchData()">


<div id="wsb-canvas-template-page" class="wsb-canvas-page page"style=" margin: auto; width: 1019px; background-color: #ffffff; position: relative; margin-top: 0px">
	<div id="d_header">
			<div id="heading">
			
			<div class="left">
				<span class="s_heading"><%=helper.getText("heading")%></span><br>
				<span class="s_heading" style="font-size: 14px; float:left">
				<%=helper.getText("heading2part1")%>&#9679;<%=helper.getText("heading2part2")%>&#9679;<%=helper.getText("heading2part1")%>
				</span>
			</div>
			
		<div class="right">
				<div style="display:inline-block; vertical-align:top; margin-left:200pxx;">
				<a href="index.jsp" id="home" class="ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only" style="font-size: 14px; color: #561243;" data-inline="true">
				<span class="ui-button-text"><%=helper.getText("home")%></span>
				</a>
				<% Integer userId = (Integer)session.getAttribute("userId"); %>
				
				<a id="viewSummary" href="SummaryPage.jsp?categoryName=common" class="ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only" 
				style="font-size:14px;color: #561243;<%if(userId == null){ %>display:none; <% } %>" data-inline="true"; ><span class="ui-button-text"><%=helper.getText("myevents")%></span></a>
				
				<a id="login-user" style="font-size: 14px; color: #561243; <%if( userId != null){ %>display:none; <% } %>" data-inline="true";><%=helper.getText("login")%></a>
				<a id="logout-user" href="logOut.jsp" class="ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only" 
				style="font-size:14px;color: #561243;<%if(userId == null){ %>display:none; <% } %>" data-inline="true"; ><span class="ui-button-text"><%=helper.getText("logout")%></span></a>
				<a id="create-user" style="font-size: 14px; color: #561243; <%if(userId != null){ %>display:none; <% } %>" data-inline="true"><%=helper.getText("register")%></a>
				<span id = "fblogin" style="data-inline:true; <%if(userId != null){ %>display:none; <% } %>">
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
		
	
	<div class= "container">
		<br>	
		
		<div class = "slideShowImages" id="slideShowImages">
		    <!--  
		    <img src="images/demo1/1.jpg" alt="Slide 1" />
		    <img src="images/demo1/2.jpg" alt="Slide 2" />
		    <img src="images/demo1/3.jpg" alt="Slide 3" />    
		    <img src="images/demo1/4.jpg" alt="Slide 4" />-->
  		</div> 		
			
		<div id = "title" align= "center"></div>
		
		<h3 align="center"><%=helper.getText("ins")%></h3>
		
		<div style="height:100px;width:100%;float:left;">
			<h3 style="margin-left:100px;"><%=helper.getText("eventName")%></h3>
			<input type = "text" id = "event_name" style = "width:400px;margin-left:100px;" placeholder = "<%=helper.getText("eventName")%>"/>
		</div>
		</br>
			
		<div style="height:500px;width:50%;float:left;padding-right:10px;">	
			<h3 style="margin-left:100px;"><%=helper.getText("suggestions")%>:</h3>		
			<ul id="sortable1" class="droptrue ui-sortable" unselectable="on" style="min-height: 400px;">		
			</ul>
		</div>
		
		<!--  <div class="listBlock">-->
		<div style="height:500px;width:50%;float:left;padding-left:10px;">					
			<h3><%=helper.getText("tasklist")%>:</h3>
			<ul id="sortable2" class="droptrue ui-sortable" unselectable="on" style="min-height: 400px;">
			</ul>
		</div>		
		
		
		<div align="center">
			<button type="button" class="ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only" id = "continue" value = "Continue" role="button" aria-disabled="false"><span class="ui-button-text" onclick = "submitData()"><%=helper.getText("continue")%></span></button>
			<!--  <button class= "button" id = "continue" value = "Continue" onclick = "submitData()"> Continue...</button>-->
		</div>
				
	</div> <!-- container div end -->
	
	<br><br>
		<div id="audioPlayer" align="center"></div>
		<br>
	
	<div class="d_footer">
			<span class="copyright">© 2013 EventHub Inc. All Rights Reserved. | </span>
			<a href="AboutUS.jsp?cateogry=common" >About Us </a> 
		</div>
		<br><br>
	
	</div>

</body>
</html>