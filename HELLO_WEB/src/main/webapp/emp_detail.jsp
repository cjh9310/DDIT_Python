<%@page import="kr.co.aiai.dao.EmpVO"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%
EmpVO emp = (EmpVO)request.getAttribute("emp");
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script type="text/javascript">
function fn_list(){
	location.href = "emp_list"
}
function fn_mod(){
	location.href = "emp_mod?e_id=<%=emp.getE_id()%>";
}
function fn_del(){
	var flag = confirm("한번 지워진 데이터는 복구가 불가합니다.\n그래도 삭제하시렵니까?");
	if(!flag){
		return;
	}
	location.href = "emp_del_act?e_id=<%=emp.getE_id()%>";
}

</script>
</head>
<body>


	<table border="1px" style="width: 200px">
		<tr>
			<td>사번</td>
			<td>
				<%=emp.getE_id()%>
			</td>
		</tr>
		<tr>
			<td>이름</td>
			<td>
				<%=emp.getE_name()%>
			</td>
		</tr>
		<tr>
			<td>성별</td>
			<td>
				<%=emp.getSex()%>
			</td>
		</tr>
		<tr>
			<td>주소</td>
			<td>
				<%=emp.getAddr()%>
			</td>
		</tr>	
		<tr>
			<td colspan="2">
				<input type="button" value="목록" onclick="fn_list()" />
				<input type="button" value="수정" onclick="fn_mod()" />
				<input type="button" value="삭제" onclick="fn_del()" />
			</td>
		</tr>		
					
	</table>

</body>
</html>