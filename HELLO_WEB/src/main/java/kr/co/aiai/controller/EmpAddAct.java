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


@WebServlet("/emp_add_act")
public class EmpAddAct extends HttpServlet {

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		String e_name = request.getParameter("e_name");
		String sex = request.getParameter("sex");
		String addr = request.getParameter("addr");
		
		System.out.println("e_name:"+e_name);
		System.out.println("sex:"+sex);
		System.out.println("addr:"+addr);
		
		DaoEmp de = new DaoEmp();
		int cnt = -1;
		try {
			cnt = de.insert(new EmpVO("", e_name, sex, addr));
		} catch (Exception e) {
			e.printStackTrace();
		}
		request.setAttribute("cnt", cnt); 
		System.out.println("cnt:"+cnt);
		
		RequestDispatcher rd = request.getRequestDispatcher("/emp_add_act.jsp");
		rd.forward(request,response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}

}
