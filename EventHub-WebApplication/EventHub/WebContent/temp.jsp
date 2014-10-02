<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Insert title here</title>

</head>
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
<body>
 <H1>Using Buttons</H1>
        <FORM NAME="form1" ACTION="temp.jsp" METHOD="POST">
            <INPUT TYPE="HIDDEN" NAME="buttonName">
            <INPUT TYPE="BUTTON" VALUE="Button 1" ONCLICK="button1()">
            <INPUT TYPE="BUTTON" VALUE="Button 2" ONCLICK="button2()">
            <INPUT TYPE="BUTTON" VALUE="Button 3" ONCLICK="button3()">
        </FORM>

        <SCRIPT LANGUAGE="JavaScript">
            <!--
               function button1()
               {
                   document.form1.buttonName.value = "button 1"
                   form1.submit()
               }    
               function button2()
               {
                   document.form1.buttonName.value = "button 2"
                   form1.submit()
               }    
               function button3()
               {
                   document.form1.buttonName.value = "button 3"
                   form1.submit()
               }    
            // --> 
        </SCRIPT>
        
        <%request.getSession().setAttribute("lang", "eng");
        String value = request.getParameter("buttonName");
        System.out.println("Value:"+value);
        %>
</body>
</html>