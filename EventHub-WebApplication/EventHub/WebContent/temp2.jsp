<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Insert title here</title>
</head>
<body>
<form>
<select name='myfield' onchange='this.form.submit()'>
  <option selected>Milk</option>
  <option>Coffee</option>
  <option>Tea</option>
</select>
</form>


<% 
System.out.println("Lang:"+session.getAttribute("lang"));
String value = request.getParameter("myfield");
System.out.println("Value: "+value);
%>

</body>
</html>