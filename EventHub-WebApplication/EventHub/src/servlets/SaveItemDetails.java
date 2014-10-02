package servlets;

import java.io.BufferedReader;
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
 * Servlet implementation class SaveItemDetails
 */
public class SaveItemDetails extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
	
	DatabaseConnection connection = DatabaseConnection.getInstance();
	Connection con = connection.setConnection();
	PreparedStatement ps;
	ResultSet r;
//	String result;
    /**
     * @see HttpServlet#HttpServlet()
     */
    public SaveItemDetails() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub

		response.setContentType("application/json");
		StringBuffer jb = new StringBuffer();
		String line = null;
		try {
			BufferedReader reader = request.getReader();
			while ((line = reader.readLine()) != null)
				jb.append(line);
		} catch (Exception e)
		{ 

		}

		try {
			
			HttpSession session = request.getSession();
			int userId = (Integer)session.getAttribute("userId");
			System.out.println("UserId:"+userId);
			


			JSONObject jsonObject = new JSONObject(jb.toString());
			System.out.println("jsonObject:"+jsonObject.toString());

			
			String orderName = jsonObject.getString("orderName");
			System.out.println("ordername:"+orderName);
			
			String strItem = jsonObject.getString("itemsString");
					
			String temp1 = strItem.substring(0, strItem.length() - 1);
			String[] strWithoutDollar;
			
			strWithoutDollar = temp1.split("\\|");
			
			String itemName ="";
			String itemCost = "";
			String orderStatus = "Active";
			String result = "";

			
			for (int i = 0; i < strWithoutDollar.length; i++) {
								
				String[] strWithoutPipe = strWithoutDollar[i].split("&");
				for (int j = 0; j < strWithoutPipe.length; j++){
								
				itemName = strWithoutPipe[0];
				System.out.println("itemName:"+itemName);
				itemCost = strWithoutPipe[1];
				System.out.println("itemCost:"+itemCost);
								}
				
				String query = "INSERT INTO eventhub.userOrder(userOrderName,toDoItemName,toDoItemCost,userOrderStatus,userId)"+
						"VALUES ('"+orderName+"','"+itemName+"','"+itemCost+"','"+orderStatus+"', '"+ userId+"');";
				System.out.println("Query: "+query);
				ps = con.prepareStatement(query);
				int rowCount =  ps.executeUpdate();
								
				if(rowCount>0){
					 result = "true";
					System.out.println("Insert Successful");
			}
			
			
			}
			if (result == "true")
			{
				JSONObject resp = new JSONObject();
				resp.put("errorCode",200);
				resp.put("responseText","Success");
				response.getWriter().write(resp.toString());
				System.out.println("Response: "+resp);
			}	
			
		} catch (JSONException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		} catch (SQLException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}
	}

}
