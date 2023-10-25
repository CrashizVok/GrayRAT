import java.io.*;
import java.net.*;

public class Client {
    public static void main(String[] args) throws IOException {
        int port = 12345;
        InetAddress inetAddress = InetAddress.getByName("192.168.1.101"); //replace with your Kali Linux IP
        Socket socket = new Socket(inetAddress, port);
        DataInputStream dataInputStream = new DataInputStream(socket.getInputStream());
        DataOutputStream dataOutputStream = new DataOutputStream(socket.getOutputStream());

        System.out.println("Client is running...");
        System.out.println("Sending command to server: ");
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        String command = bufferedReader.readLine();
        dataOutputStream.writeUTF(command);
        dataOutputStream.flush();
        System.out.println("Command sent successfully");

        String serverResponse = dataInputStream.readUTF();
        System.out.println("Server response: " + serverResponse);

        socket.close();
    }
}
