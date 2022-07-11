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
	String p = request.getParameter("p");
	int pp = Integer.parseInt(p);
		
%>

<%
for(int i=1;i<=9;i++){
	out.println(pp+"*"+i+"="+(pp*i)+"<br/>");
}
%>
<br/>
<%for(int i=1;i<=9;i++){%>
	<%=pp%>*<%=i%>=<%=(pp*i)%><br/>
<%}%>
<!-- out.println과 같은 역할 요즘 추세 디자이너가 보기 쉬움 jstl -->


</body>
</html>