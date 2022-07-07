package application;
	
import java.util.Random;

import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.layout.VBox;


public class Maina extends Application {
	
	TextField tf1,tf2,tf3,tf4;
	
	@Override
	public void start(Stage primaryStage) {
		try {
//			BorderPane root = new BorderPane();
			VBox root = (VBox)FXMLLoader.load(getClass().getResource("maina.fxml"));
			
			Scene scene = new Scene(root,400,400);
			
			tf1 =(TextField) scene.lookup("#tf1");
			tf2 =(TextField) scene.lookup("#tf2");
			tf3 =(TextField) scene.lookup("#tf3");
			tf4 =(TextField) scene.lookup("#tf4");
			
			Button btn = (Button) scene.lookup("#btn");
			btn.setOnMouseClicked(new EventHandler<Event>() {
				@Override
				public void handle(Event event) {
					myclick();
				}
			});
			
			
			scene.getStylesheets().add(getClass().getResource("application.css").toExternalForm());
			primaryStage.setScene(scene);
			primaryStage.show();
		} catch(Exception e) {
			e.printStackTrace();
		}
	}
	
	public void myclick() {
		String a = tf1.getText();
		String b = tf2.getText();
		String c = tf3.getText();

		int t1 = Integer.parseInt(a);
		int t2 = Integer.parseInt(b);
		int t3 = Integer.parseInt(c);
		int result=0;
		
		for(int i=t1; i<=t2; i++) {
			if(i%t3==0) {
				result += i;
			}
		}
		tf4.setText(result+"");
		
		
	}
	
	
	public static void main(String[] args) {
		launch(args);
	}
}
