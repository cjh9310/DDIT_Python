<%@page import="kr.co.aiai.dao.EmpVO"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%
int cnt = (int)request.getAttribute("cnt");
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script type="text/javascript">
var cnt = <%=cnt%>;

if(cnt == 1){
	alert("정상적으로 추가되었습니다.");
	location.href = "emp_list";
} else {
	history.back();
}

</script>
</head>
<body>

</body>
</html>