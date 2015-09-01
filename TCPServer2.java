import java.util.*;
import java.net.*;
import java.io.*;
/*
	Author: Vinoth Kumar Sadagopan(800850529), Sashank Santhanam(800878367)
	Description: The below code is for TCP Server
*/
class TCPServer2
{
	public static void main(String[] args) throws Exception
	{
		ServerSocket welcomeSocket = new ServerSocket(8777); // TCP Server socket is created
		Socket connectionSocket = welcomeSocket.accept();    // Socket to accept the client part
		ArrayList<String> As = new ArrayList<String>();  // arraylist to store the values recieved 
		try
		{
			

			while(true)
			{
			//Socket connectionSocket = welcomeSocket.accept();
				BufferedReader br=new BufferedReader(new InputStreamReader(connectionSocket.getInputStream())); // reads the mesage sent by the client
				PrintStream ps=new PrintStream(connectionSocket.getOutputStream());	
				String  message= br.readLine(); // reads the message and store it in a string
				if(message==null)

				{
					break;
				}
				As.add(message); // Stores the message in array
				
			 	ps.println(message); //sends the message back to the client



			}
			connectionSocket.close();
		}
		finally
		{
			connectionSocket.close();	
		}
		 
		



	}
}