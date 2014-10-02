package servlets;


import java.io.BufferedReader;
import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import org.codehaus.jettison.json.JSONException;
import org.codehaus.jettison.json.JSONObject;

/**
 * Servlet implementation class FBRegisterLoginUser
 */
public class FBRegisterLoginUser extends HttpServlet {
	private static final long serialVersionUID = 1L;


	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		HttpSession session = request.getSession();

		response.setContentType("application/json");
		StringBuffer jb = new StringBuffer();
		String line = null;
		try {
			BufferedReader reader = request.getReader();
			while ((line = reader.readLine()) != null)
				jb.append(line);
		} catch (Exception e)
		{ 
			e.printStackTrace(); 

		}


		try {
			JSONObject jsonObject = new JSONObject(jb.toString());
			System.out.println("jsonObject:"+jsonObject.toString());
			String email = jsonObject.getString("email");

			Connection con = null;
			ResultSet rs;
			Statement stmt = null;
			int rowCount = 0;

			Class.forName("com.mysql.jdbc.Driver").newInstance();

			//con = DriverManager.getConnection("jdbc:mysql://localhost:3306/eventPlanning","root","ruh12ruh");
			DatabaseConnection connection = DatabaseConnection.getInstance();
			con = connection.setConnection();
			stmt = con.createStatement();
			stmt.setEscapeProcessing(true);
			if(!con.isClosed()){
				System.out.println("Successfully Connected!");
			}

			String query = "Select userId from eventhub.user where userName = '"+email+"'";
			System.out.println("Query: "+query);
			rs = stmt.executeQuery(query);
			System.out.println("rs: "+rs);
			JSONObject resp = new JSONObject();


			if(rs!= null && rs.next()){
				session.setAttribute("userId", rs.getInt("userId"));
				System.out.println("Session UserID: "+session.getAttribute("userId"));
				resp.put("errorCode", 200);
				resp.put("responseText", "Success");
			}
			else{	
				String query2 =  "INSERT INTO eventhub.user(password,firstName,lastName,userName,securityQuestion,answer)"+
						"VALUES ('null','null','null','"+email+"','null','null')";
				System.out.println("Query: "+query2);
				rowCount = stmt.executeUpdate(query2);
				if(rowCount>0){
					//login user and start session
					String query3 = "Select userId from eventhub.user where userName = '"+email+"'";
					System.out.println("Query: "+query);
					rs = stmt.executeQuery(query);
					if(rs != null && rs.next()){
						session.setAttribute("userId",rs.getInt("userId"));
						resp.put("errorCode", 200);
						resp.put("responseText", "Success");
					}
					else{
						resp.put("errorCode", 300);
						resp.put("responseText", "Failure");
					}
				}
				else{
					resp.put("errorCode", 300);
					resp.put("responseText", "Failure");	
				}
			}
			response.getWriter().write(resp.toString());

		}catch (JSONException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (InstantiationException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IllegalAccessException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}



	}
}
