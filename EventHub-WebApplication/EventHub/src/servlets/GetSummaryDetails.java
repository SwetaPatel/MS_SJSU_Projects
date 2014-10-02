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
import javax.servlet.http.HttpSession;

import org.codehaus.jettison.json.JSONException;
import org.codehaus.jettison.json.JSONObject;

/**
 * Servlet implementation class GetSummaryDetails
 */
public class GetSummaryDetails extends HttpServlet {
	private static final long serialVersionUID = 1L;

	/**
	 * @see HttpServlet#HttpServlet()
	 */

	DatabaseConnection connection = DatabaseConnection.getInstance();
	Connection con = connection.setConnection();
	PreparedStatement ps;
	PreparedStatement ps1;

	ResultSet r;
	ResultSet r1;

	String result;
	String result1;

	public GetSummaryDetails() {
		super();
		// TODO Auto-generated constructor stub
	}

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse
	 *      response)
	 */
	protected void doGet(HttpServletRequest request,
			HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub

		response.setContentType("application/json");
		HttpSession session = request.getSession();
		int id = (Integer)session.getAttribute("userId");
		System.out.println("Got idddd:"+id);

		System.out.println("Got eventName in servlet: " + id);
		String query = "select * from userOrder where userId=\"" + id
				+ "\" GROUP BY userOrderName;";

		String result = "";
		String result1 = "";

		try {
			System.out.println(query);
			ps = con.prepareStatement(query);
			r = ps.executeQuery();

			r.last();
			int total = r.getRow();

			r.beforeFirst();
			System.out.println(total);

			String[] resultArray = new String[total];
			int i = 0;

			while (r.next()) {
				String query1 = "select * from userOrder where userId=\"" + id
						+ "\" and userOrderName=\"" + r.getString(3) + "\";";

				System.out.println(query1);
				ps1 = con.prepareStatement(query1);
				r1 = ps1.executeQuery();

				while (r1.next()) {
					
					result1 += r1.getString(3) + "$" + r1.getString(4) + "$"
							+ r1.getString(5) + "|";

				}
				resultArray[i] = result1;
				i++;

				result1 = result1 + "*";
			}

			System.out.println(" result is:  " + result1);

			
			JSONObject resp = new JSONObject();
			
			if (total != 0)
			{
			resp.put("status", 200);
			resp.put("responseText", result1.substring(0, result1.length() - 1));
			}
			else{
				
				resp.put("status", 300);
				resp.put("responseText", "NoRecords");

			}
			response.getWriter().write(resp.toString());

		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();

		} catch (JSONException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}

	// String result = "";
	// try {
	// System.out.println(query);
	// ps = con.prepareStatement(query);
	// r = ps.executeQuery();
	// while(r.next()){
	// result += r.getString(4)+"$"+r.getString(5)+"|";
	// }
	// System.out.println("Our result is:  "+ result);
	// JSONObject resp = new JSONObject();
	// resp.put("status",200);
	// resp.put("responseText",result.substring(0, result.length()-1));
	// response.getWriter().write(resp.toString());
	// System.out.println("My Response is: "+resp);

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse
	 *      response)
	 */
	protected void doPost(HttpServletRequest request,
			HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
	}

}
