package kr.co.aiai.dao;


import java.sql.*;

public class MySelect {

//	static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";
//	static final String DB_URL = "jdbc:mysql://127.0.0.1:3305/python";
//	static final String USERNAME = "root";
//	static final String PASSWORD = "python";

	public static void main(String[] args) throws  Exception {

		Class.forName("com.mysql.cj.jdbc.Driver");

		Connection conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3305/python", "root", "python");

		Statement stmt = conn.createStatement();

		String sql = "select * from emp";

		ResultSet rs = stmt.executeQuery(sql);

		while (rs.next()) {

			String e_id = rs.getString("e_id");

			String e_name = rs.getString("e_name");

			System.out.println("e_id = " + e_id + " , " + "e_name = " + e_name);

		}
		rs.close();
		stmt.close();
		conn.close();

	}

}