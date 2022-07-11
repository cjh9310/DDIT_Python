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


@WebServlet("/emp_del_act")
public class EmpDelAct extends HttpServlet {

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		String e_id = request.getParameter("e_id");
		System.out.println("e_id:"+e_id);

		DaoEmp de = new DaoEmp();
		int cnt = -1;
		try {
			cnt = de.delete(new EmpVO(e_id,"","",""));
		} catch (Exception e) {
			e.printStackTrace();
		}
		request.setAttribute("cnt", cnt); 
		System.out.println("cnt:"+cnt);
		
		RequestDispatcher rd = request.getRequestDispatcher("/emp_del_act.jsp");
		rd.forward(request,response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}

}
