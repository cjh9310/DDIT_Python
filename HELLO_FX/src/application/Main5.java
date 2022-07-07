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


public class Main5 extends Application {
	
	TextField tf_na;
	TextField tf_com;
	TextField tf_result;
	@Override
	public void start(Stage primaryStage) {
		try {
//			BorderPane root = new BorderPane();
			VBox root = (VBox)FXMLLoader.load(getClass().getResource("main5.fxml"));
			
			Scene scene = new Scene(root,400,400);
			
			tf_na = (TextField) scene.lookup("#tf_na");
			tf_com = (TextField) scene.lookup("#tf_com");
			tf_result = (TextField) scene.lookup("#tf_result");
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
		String com= "";
		String na= "";
		String result= "";
		
		na = tf_na.getText();
		double rnd = Math.random();
		
		if(rnd >0.5) {
			com="홀";
		}else {
			com="짝";
		}
		if(com.equals(na)) {
			result = "이김";
		}else {
			result = "짐";
		}
		tf_com.setText(com);
		tf_result.setText(result);
	}
	public static void main(String[] args) {
		launch(args);
	}
}
