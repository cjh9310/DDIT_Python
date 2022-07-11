<%@page import="kr.co.aiai.dao.EmpVO"%>
<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>

<%
String a = (String) request.getAttribute("a");
ArrayList<EmpVO> list = (ArrayList<EmpVO>)request.getAttribute("b");
%>

<table border = "1px">
	<tr>
		<td>사번</td>
		<td>이름</td>
		<td>성별</td>
		<td>주소</td>
	</tr>
<%for(int i=0;i<list.size();i++){%>
<%	EmpVO temp = (EmpVO)list.get(i); %>

	<tr>
		<td><%=temp.getE_id() %>사번</td>
		<td><%=temp.getE_name() %>이름</td>
		<td><%=temp.getSex() %>성별</td>
		<td><%=temp.getAddr() %>주소</td>
	</tr>
<%}%>
</table>



</body>
</html>