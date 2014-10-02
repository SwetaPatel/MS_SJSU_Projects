<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
	pageEncoding="ISO-8859-1"%>
<%@page import="utils.LocalizationHelper"%>

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
<link rel="stylesheet" type="text/css" href="css/style.css" />


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





<!-- <script>
var param = (document.URL.split("?"))[1];
var pa = (document.URL.split("&"));
var languageString = pa[4].split("=")[1];
console.log("In detail lang is " + languageString);
</script>
 -->
<script>

function checkNo(evt) {
    evt = (evt) ? evt : window.event;
    var charCode = (evt.which) ? evt.which : evt.keyCode;
    if (charCode > 31 && (charCode < 48 || charCode > 57)) {
        return false;
    }
    return true;
}

</script>




<script type="text/javascript" src="js/DetailView.js"></script>

<script type="text/javascript" src="https://www.google.com/jsapi"></script>
<script type="text/javascript">
	google.load("visualization", "1", {
		packages : [ "corechart" ]
	});
	google.setOnLoadCallback(drawChart);
</script>

<script>
	function drawChart() {
		document.getElementById("piechart").style.visibility = "visible";

		var param = (document.URL.split("?"))[1];
		var pa = (document.URL.split("&"));
		var itemDetails = pa[0].split("=")[1];
		var eventName = pa[1].split("=")[1];

		var strWithoutPipe = itemDetails.split("|");

		var data = new google.visualization.DataTable();

		data.addColumn('string', 'Item Name');

		data.addColumn('number', 'Cost ($)');

		var inputs = document.getElementsByTagName('input');

		for (var i = 0; i < strWithoutPipe.length; i++) {

			var s = strWithoutPipe[i].split("$");
			var itemString = s[1].replace(/%20/g,' ');	
			data.addRow([itemString, parseInt(inputs[i].value) ]);
		}

		var options = {
			title : 'Estimated Cost Distribution',
			is3D : true,

		};

		var chart = new google.visualization.PieChart(document
				.getElementById('piechart'));
		chart.draw(data, options);
	}
</script>


<script>
	function drawChart1() {

		document.getElementById("piechart").style.visibility = "visible";

		var param = (document.URL.split("?"))[1];
		var pa = (document.URL.split("&"));
		var itemDetails = pa[0].split("=")[1];
		var eventName = pa[1].split("=")[1];

		var strWithoutPipe = itemDetails.split("|");

		var data = new google.visualization.DataTable();

		data.addColumn('string', 'Item Name');

		data.addColumn('number', 'Cost ($)');

		var inputs = document.getElementsByTagName('input');

		for (var i = 0; i < strWithoutPipe.length; i++) {

			var s = strWithoutPipe[i].split("$");
			
			
			var itemString = s[1].replace(/%20/g,' ');	
			data.addRow([itemString, parseInt(inputs[i].value) ]);

		}

		var options = {
			title : 'Estimated Cost Distribution',
			pieHole : 0.4,
		// colors: ['#D156D1', '#e6693e', '#ec8f6e', '#f3b49f', '#f6c7b6'],

		};

		var chart = new google.visualization.PieChart(document
				.getElementById('piechart'));
		chart.draw(data, options);
	}
</script>
<script>
	function updateChart() {

		if (document.getElementById('piechrt').checked
				|| document.getElementById('donutchrt').checked) {
			if (document.getElementById('piechrt').checked) {
				drawChart();
			} else {
				drawChart1();
			}
		} else {
			alert("Select a chart style first.");

		}
	}

	function saveDetails() {
		var inputs = document.getElementsByTagName('input');
		var flag = 0;
		for (var k = 0 ; k < inputs.length ; k++)
			{
			
			if (inputs[k].value == "")
		
				flag = 1;
			} 
		
		if (flag == 0) {

		var param = (document.URL.split("?"))[1];
		var pa = (document.URL.split("&"));
		var itemDetails = pa[0].split("=")[1];
		var eventName = pa[1].split("=")[1];
		var categoryName = pa[2].split("=")[1];
		var strWithoutPipe = itemDetails.split("|");
		
		var eventName1 = eventName.replace(/%20/g,' ');
		
		var user = {};		
		user.orderName = eventName1;
	
		var strItem = "";
		for (var i = 0; i < strWithoutPipe.length; i++) {
            var s = strWithoutPipe[i].split("$");            
            var s1 = s[1].replace(/%20/g,' ');    
            var itemDetail= s1 + "&" + parseInt(inputs[i].value) ;
        strItem += itemDetail + "|" ;     
        }
		
		user.itemsString = strItem ;


			var requestJson = JSON.stringify(user);
			console.log("Json String: " + requestJson);
			$.ajax({
						url : "SaveItemDetails",
						type : "POST",
						context : document.body,
						data : requestJson,
						success : function(data) {
							if (data.errorCode == 200
									&& data.responseText == "Success") {
							//alert("Success");
								 console.log("success !!!!");
									openSummary(categoryName);


							} else {
								alert("Uh-oh - Something went wrong, try again!");
							}
						}
					});
		
		}
		else{
				alert("Please enter Cost for every task or Keep it 0.");		
			}
		}
	
	

	function openSummary(categoryName) {

		window.location.href = "SummaryPage.jsp?categoryName=" +categoryName;
	}
</script>
<style>
.button {
	width: 150px;
	height: 50px
}
</style>

</head>

<% 


System.out.println("session is redirect in selectionnnn "  +session.getAttribute("lang"));
LocalizationHelper helper = LocalizationHelper.getInstance(session.getAttribute("lang").toString(), getServletContext());
%>

<body onload="onLoadDetail()">

	<div id="wsb-canvas-template-page" class="wsb-canvas-page page"
		style="height: 1450px; margin: auto; width: 1019px; background-color: #ffffff; position: relative; margin-top: 0px">

		<div id="d_header">
			<div id="heading">

				<div class="left">
					<span class="s_heading"><%=helper.getText("heading")%></span><br> <span class="s_heading" style="font-size: 14px; float: left">
				<%=helper.getText("heading2part1")%>&#9679;<%=helper.getText("heading2part2")%>&#9679;<%=helper.getText("heading2part1")%>
						</span>
				</div>


				<div class="right">
					<div
						style="display: inline-block; vertical-align: top; margin-left: 200pxx;">
						<a href="index.jsp" id="home"
							class="ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only"
							style="font-size: 14px; color: #561243;" data-inline="true">
							<span class="ui-button-text"><%=helper.getText("home")%></span>
						</a>
						<%
							Integer userId = (Integer) session.getAttribute("userId");
						%>

						<a id="viewSummary" href="SummaryPage.jsp?categoryName=common"
							class="ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only"
							style="font-size:14px;color: #561243;<%if (userId == null) {%>display:none; <%}%>"
							data-inline="true"; ><span class="ui-button-text"><%=helper.getText("myevents")%></span></a>

						<a id="login-user"
							style="font-size: 14px; color: #561243; <%if (userId != null) {%>display:none; <%}%>"
							data-inline="true";><%=helper.getText("login")%></a> <a id="logout-user"
							href="logOut.jsp"
							class="ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only"
							style="font-size:14px;color: #561243;<%if (userId == null) {%>display:none; <%}%>"
							data-inline="true"; ><span class="ui-button-text"><%=helper.getText("logout")%></span></a>
						<a id="create-user"
							style="font-size: 14px; color: #561243; <%if (userId != null) {%>display:none; <%}%>"
							data-inline="true"><%=helper.getText("register")%></a> <span id="fblogin"
							style="data-inline:true; <%if (userId != null) {%>display:none; <%}%>">
							<a href="javascript:login();"> <img src="img/fb-login.png"></a>
						</span>
					</div>


					<div id="fblogout"
						style="display: inline-block; visibility: hidden;">
						<img style="data-inline: true;" id="profile_pic" />
						<div style="display: inline-block;">
							<span id="profile_name"
								style="data-inline: true; font-size: 12px; visibility: hidden;"></span><br />
							<a href="javascript:logout();"><img
								src="img/facebook_logout_button.png"></a>
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

			<div id="eventNameSpace" align="center"></div>
			<br>
			<div id="detailSpace"></div>
			<div id="addChartSpace"></div>


			<br>
			<form>

				<table border="0" align="center">
					<tr>
						<td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<b>
						<%=helper.getText("chart")%></b></td>
					</tr>
					<tr>
						<td></td>
					</tr>

					<tr>
						<td><input type="radio" name="chart" id="piechrt" value="pie"
							onClick='drawChart()' align="center"><%=helper.getText("pie")%></td>
						<td><input type="radio" name="chart" id="donutchrt"
							value="donut" onClick='drawChart1()'><%=helper.getText("donut")%></td>
						<br>
						<br>
						<br>
					</tr>
					</tr>
				</table>
			</form>

			<br>
			<form>
				<table align="center">

					<tr>
						<!--  <td><input type='button' class="button" id="btnUpdate"
							value='Update Chart' onClick='updateChart()'></td>-->
						<td><button type="button"
								class="ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only"
								id="btnUpdate" value="Update Chart" role="button"
								aria-disabled="false">
								<span class="ui-button-text" onclick="updateChart()"><%=helper.getText("update")%></span>
							</button></td>
						<!-- <td><input type='button' id="btnSave" class="button"
							value='Save it' onclick='saveDetails()'></td> -->
						<td><button type="button"
								class="ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only"
								id="btnSave" value="Save it" role="button" aria-disabled="false">
								<span class="ui-button-text" onclick="saveDetails()"><%=helper.getText("save")%></span>
							</button></td>
					</tr>
				</table>
			</form>
			<div id="piechart" align="center"
				style="width: 1000px; height: 500px; margin-right: 550px;"></div>



		</div>
		
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