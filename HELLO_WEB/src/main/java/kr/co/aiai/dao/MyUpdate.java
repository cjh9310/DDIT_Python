package kr.co.aiai.dao;
import java.sql.*;

public class MyUpdate {

	public static void main(String[] args) throws Exception {

		Class.forName("com.mysql.cj.jdbc.Driver");
		Connection conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3305/python", "root", "python");
		Statement stmt = conn.createStatement();
		
		String sql = "";
		sql += "update emp ";
		sql += "set ";
		sql += "e_name = '4', ";
		sql += "sex = '4', ";
		sql += "addr = '4' ";
		sql += "where ";
		sql += "e_id = '3' ";

		int cnt = stmt.executeUpdate(sql);
		System.out.println("cnt:"+cnt);

		stmt.close();
		conn.close();
	}
}



