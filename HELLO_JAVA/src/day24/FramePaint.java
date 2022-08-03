package day24;

import java.awt.Frame;
import java.awt.Graphics;

public class FramePaint extends Frame {
	int cnt = 0;
		 @Override 
	public void paint(Graphics g) {
			 System.out.println("cnt: "+cnt);
			 g.drawLine(0, 0, 200, 200); 
			 g.drawString("BABO:"+cnt, 100, 100);
			 cnt++;
			 super.paint(g); 
			 
		 
	}
	public static void main(String[] args) {
		FramePaint fp = new FramePaint();
		fp.setSize(400,400);
		fp.setVisible(true);
	}
	
}
