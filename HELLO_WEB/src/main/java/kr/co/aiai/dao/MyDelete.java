package kr.co.aiai.dao;
import java.sql.*;

public class MyDelete {

	public static void main(String[] args) throws Exception {
		
		Class.forName("com.mysql.cj.jdbc.Driver");
		Connection conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3305/python", "root", "python");
		
		Statement stmt = conn.createStatement();
		String sql = "";

		sql += "delete emp";
		sql += "where ";
		sql += "e_id= '3'";
		
		
		int cnt = stmt.executeUpdate(sql);
		System.out.println("cnt"+cnt);
		
		stmt.close();
		conn.close();
	}
}



