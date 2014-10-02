package servlets;


import java.io.IOException;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.codehaus.jettison.json.JSONException;
import org.codehaus.jettison.json.JSONObject;
import servlets.DatabaseConnection;

/**
 * Servlet implementation class GetToDoListItems
 */
public class GetToDoListItems extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
	DatabaseConnection connection = DatabaseConnection.getInstance();
	Connection con = connection.setConnection();
	PreparedStatement ps;
	ResultSet r;
	String result;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public GetToDoListItems() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		response.setContentType("application/json");
		String id = request.getParameter("item");
		System.out.println("Got id in servlet: " + id);
		String query = "select * from toDoItemList where eventName=\""+id+"\";";
		
		String result = "";
		try {
			System.out.println(query);
			ps = con.prepareStatement(query);
			r = ps.executeQuery();
			while(r.next()){
				result += r.getString(1)+"$"+r.getString(2)+"$"+r.getString(4)+"|";
							
			}		
			System.out.println("Our result is:  "+ result);	
			JSONObject resp = new JSONObject();
			resp.put("status",200);
			resp.put("responseText",result.substring(0, result.length()-1));
			response.getWriter().write(resp.toString());
			System.out.println("My Response is: "+resp);
		
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			
		} catch (JSONException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}		
		
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
	}


}
