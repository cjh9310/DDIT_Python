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

@WebServlet("/emp_mod")
public class EmpMod extends HttpServlet {

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String e_id = request.getParameter("e_id");
		
		DaoEmp de = new DaoEmp();
		EmpVO vo = null;
		try {
			vo = de.getOne(new EmpVO(e_id,"","",""));
		} catch (Exception e) {
			e.printStackTrace();
		}
		request.setAttribute("emp", vo); 
		
		RequestDispatcher rd = request.getRequestDispatcher("/emp_mod.jsp");
		rd.forward(request,response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doGet(request, response);
	}

}
