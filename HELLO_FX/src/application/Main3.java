package application;
	
import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.Button;

import javafx.scene.control.TextField;
import javafx.scene.layout.VBox;


public class Main3 extends Application {
	
TextField tf1;
TextField tf2;
TextField tf3;
	@Override
	public void start(Stage primaryStage) {
		try {
//			BorderPane root = new BorderPane();
			VBox root = (VBox)FXMLLoader.load(getClass().getResource("main3.fxml"));
			
			Scene scene = new Scene(root,400,400);
			
			tf1 = (TextField) scene.lookup("#tf1");
			tf2 = (TextField) scene.lookup("#tf2");
			tf3 = (TextField) scene.lookup("#tf3");
			
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
		String a = tf1.getText();  // 우선 String으로 받고
		String b = tf2.getText();
		int aa = Integer.parseInt(a);
		int bb = Integer.parseInt(b);
		int result = aa+bb;
		tf3.setText(result+"");
	}

	
	
	public static void main(String[] args) {
		launch(args);
	}
}
