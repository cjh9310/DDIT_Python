package kr.co.aiai.controller;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import kr.co.aiai.dao.DaoEmp;
import kr.co.aiai.dao.EmpVO;

@WebServlet("/emp_mod_act")
public class EmpModAct extends HttpServlet {

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		String e_id = request.getParameter("e_id");
		String e_name = request.getParameter("e_name");
		String sex = request.getParameter("sex");
		String addr = request.getParameter("addr");
		
//		System.out.println("e_id:"+e_id);
//		System.out.println("e_name:"+e_name);
//		System.out.println("sex:"+sex);
//		System.out.println("addr:"+addr); 한글이 출력되나 실험.
		
		DaoEmp de = new DaoEmp();
		int cnt = -1;
		try {
			cnt = de.update(new EmpVO(e_id, e_name, sex, addr));
		} catch (Exception e) {
			e.printStackTrace();
		}
		request.setAttribute("cnt", cnt);  // 큰 따옴표를 int로 쓰더니 오류 떳음
		System.out.println("cnt : " + cnt);
		
		RequestDispatcher rd = request.getRequestDispatcher("/emp_mod_act.jsp");
		rd.forward(request,response);
	
	
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response); 
		// deGet을 호출   post 호출이 필요해도 get방식으로 써도 됨.
		// 만약 포트스 방식으로 하고 싶으면 위에를 다 지우고 아래에서 실행시켜야함.
		           
	}

}
