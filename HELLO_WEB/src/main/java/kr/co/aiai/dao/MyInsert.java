package kr.co.aiai.dao;
import java.sql.*;

public class MyInsert {

	public static void main(String[] args) throws Exception {
		
		Class.forName("com.mysql.cj.jdbc.Driver");
		Connection conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3305/python", "root", "python");
		
		Statement stmt = conn.createStatement();
		String sql = "";

		sql += "insert into emp";
		sql += "(e_id,e_name,sex,addr)";
		sql += "values";
		sql += "('3','3','3','3')";
		
		int cnt = stmt.executeUpdate(sql);
		System.out.println("cnt"+cnt);
		
		stmt.close();
		conn.close();
	}
}



