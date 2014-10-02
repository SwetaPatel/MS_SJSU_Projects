package servlets;

import java.sql.Connection;
import java.sql.DriverManager;

public class DatabaseConnection {
	
	private static DatabaseConnection instance = null;
	Connection conn; 
	private DatabaseConnection(){
		
	}	
	public static DatabaseConnection getInstance(){
		if(instance == null){
			instance = new DatabaseConnection();
			return instance;
		}
		return instance;
	}
	
	 	
	public Connection setConnection(){  
		try{  	     
			Class.forName("com.mysql.jdbc.Driver").newInstance();
			conn = DriverManager.getConnection("jdbc:mysql://localhost/eventhub","root","root");
			System.out.println(conn);
			if(!conn.isClosed()){
				System.out.println("Successfully Connected to " + "MySQL server using TCP/IP");
			} 
		}catch(Exception e){ 
			System.out.println("Could not connect to the MYSQL database.");
		  e.printStackTrace();
		}  
		return conn;  
	}  

}


