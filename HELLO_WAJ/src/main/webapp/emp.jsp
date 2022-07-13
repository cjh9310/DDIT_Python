<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
<script src="jquery-3.6.0.min.js"></script>
<script type="text/javascript">
function fn_list(){
	var param = "";
	param += "dummy=" + Math.random();
	param += "&a=777";
	$.ajax({
		url : "ajaxlist",
		data : param,
		dataType : "json",
		type : "post",
		async: false,  // 여기까지 실행기.
		success : function(res) { //아래부터 출력 
			var list = res;  // console.log(res)로 res열어보면 리스트처럼 되어있어서 list화 시킴
			
			var html = ``;
			
			for(var i=0; i<list.length; i++){
				var e_id = list[i].e_id;
				var e_name = list[i].e_name;
				var sex = list[i].sex;
				var addr = list[i].addr;
				html += `
				<tr>
					<td><a href="javascript:fn_one('`+e_id+`')">`+e_id+`</a></td> // 사본 숫자들을 누를 수 있게...
					<td>`+e_name+`</td>
					<td>`+sex+`</td>
					<td>`+addr+`</td>
				</tr>
				`;
			}
			$("#mytbody").html(html);
		}
	});
}

function fn_one(e_id){ // 사본 숫자들을 누르면 테이블에 출력
	var param = "";
	param += "dummy=" + Math.random();
	param += "&e_id="+e_id;
	$.ajax({
		url : "ajaxone",
		data : param,
		dataType : "json",
		type : "post",
		async: false,
		success : function(res) {
			var emp = res;
			$("#e_id").val(emp.e_id);
			$("#e_name").val(emp.e_name);
			$("#sex").val(emp.sex);
			$("#addr").val(emp.addr);
		}
	});
}
function fn_add(){
	var param = "";
	param += "dummy=" + Math.random();
	param += "&e_name="+$("#e_name").val();
	param += "&sex="+$("#sex").val();
	param += "&addr="+$("#addr").val();
	
	$.ajax({
		url : "ajaxadd",
		data : param,
		dataType : "json",
		type : "post",
		async: false,
		success : function(res) {
			var cnt = res.cnt;
			if(cnt==1){
				alert("정상적으로 출력되었습니다.");
				fn_list();       // 리로드
				$("#e_id").val("");
				$("#e_name").val("");
				$("#sex").val("");
				$("#addr").val("");
			}
		}
	});
}
function fn_del(){
	var param = "";
	param += "dummy=" + Math.random();
	param += "&e_id="+$("#e_id").val();
	
	
	$.ajax({
		url : "ajaxdel",
		data : param,
		dataType : "json",
		type : "post",
		async: false,
		success : function(res) {
			var cnt = res.cnt;
			if(cnt==1){
				alert("정상적으로 삭제되었습니다.");
				fn_list();       // 리로드
				$("#e_id").val("");
				$("#e_name").val("");
				$("#sex").val("");
				$("#addr").val("");
			}
		}
	});
} 

function fn_mod(){
	var param = "";
	param += "dummy="   +Math.random();
	param += "&e_id="   +$("#e_id").val();
	param += "&e_name=" +$("#e_name").val();
	param += "&sex="    +$("#sex").val();
	param += "&addr="   +$("#addr").val();
	
	$.ajax({
		url : "ajaxmod",
		data : param,
		dataType : "json",
		type : "post",
		async: false,
		success : function(res) {
			var cnt = res.cnt;
			if(cnt==1){
				alert("정상적으로 수정되었습니다.");
				fn_list();       // 리로드
				$("#e_id").val("");
				$("#e_name").val("");
				$("#sex").val("");
				$("#addr").val("");
			}
		}
	});
}

</script>
</head>
<body onload="fn_list()">
<table border="1px">
	<thead>
		<tr>
			<td>사번</td>
			<td>이름</td>
			<td>성별</td>
			<td>주소</td>
		</tr>
	</thead>
	<tbody id = "mytbody">
		<tr>
			<td>1</td>
			<td>1</td>
			<td>1</td>
			<td>1</td>
		</tr>
	</tbody>
</table>

<table border="1px">
	<tr>
		<td>사번</td>
		<td>
			<input type= "text" id="e_id"/>
		</td>
	</tr>
	<tr>
		<td>이름</td>
		<td>
			<input type= "text" id="e_name"/>
		</td>
	</tr>
	<tr>
		<td>성별</td>
		<td>
			<input type= "text" id="sex"/>
		</td>
	</tr>
	<tr>
		<td>주소</td>
		<td>
			<input type= "text" id="addr"/>
		</td>
	</tr>
	<tr>
		<td colspan="2">
			<input type="submit" value="추가" onclick="fn_add()"/>
			<input type="button" value="수정" onclick="fn_mod()"/>
			<input type="button" value="삭제" onclick="fn_del()"/>
		</td>
	</tr>

</table>
</body>
</html>