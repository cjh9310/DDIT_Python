package application;
	
import javafx.application.Application;
import javafx.event.Event;
import javafx.event.EventHandler;
import javafx.fxml.FXMLLoader;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.layout.VBox;


public class Main6 extends Application {
	
	Label lbl1;
	Label lbl2;
	Label lbl3;
	Label lbl4;
	Label lbl5;
	Label lbl6;
	
	
	@Override
	public void start(Stage primaryStage) {
		try {
			VBox root = (VBox)FXMLLoader.load(getClass().getResource("main6.fxml"));

			Scene scene = new Scene(root,400,400);
			
			lbl1 = (Label) scene.lookup("#lbl1");
			lbl2 = (Label) scene.lookup("#lbl2");
			lbl3 = (Label) scene.lookup("#lbl3");
			lbl4 = (Label) scene.lookup("#lbl4");
			lbl5 = (Label) scene.lookup("#lbl5");
			lbl6 = (Label) scene.lookup("#lbl6");
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
/*
	public void myclick() {
		String[] arr45 = {
			"1","2","3","4","5",		"6","7","8","9","10",
			"11","12","13","14","15",	"16","17","18","19","20",
			"21","22","23","24","25",	"26","27","28","29","30",
			"31","32","33","34","35",	"36","37","38","39","40",
			"41","42","43","44","45"
		};
		for(int i=0;i<7;i++) {
			int rnd = (int)(Math.random()*arr45.length);
			String a = arr45[rnd];
			String b = arr45[0];
			arr45[0] = a;
			arr45[rnd] = b;			
		}
		lbl1.setText(arr45[0]);
		lbl2.setText(arr45[1]);
		lbl3.setText(arr45[2]);
		lbl4.setText(arr45[3]);
		lbl5.setText(arr45[4]);
		lbl6.setText(arr45[5]);
	}
}
*/
	public void myclick() {
		String[] arr = null;
			for(int j=0; j<7; j++) {
				int rnd = (int)((Math.random()*45)+1);
				String a = arr[rnd];
				String b = arr[0];
				arr[0] = a;
				arr[rnd] = b;
			}
			
			lbl1.setText(arr[0]);
			lbl2.setText(arr[1]);
			lbl3.setText(arr[2]);
			lbl4.setText(arr[3]);
			lbl5.setText(arr[4]);
			lbl6.setText(arr[5]);
}
	public static void main(String[] args) {
		launch(args);
	}
}
