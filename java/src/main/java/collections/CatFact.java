package collections;

import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Scanner;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

public class CatFact {

    private final static String CAT_URL = "https://catfact.ninja/fact";

    public void getCatFacts() {

        try {
            URL url = new URL(CAT_URL);
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();

            conn.setRequestMethod("GET");
            conn.connect();

            int responseCode = conn.getResponseCode();

            if (responseCode != 200){
                throw new Exception("Error getting data.  Response code: " + String.valueOf(responseCode));
            }

            String data = "";

            Scanner scanner = new Scanner(url.openStream());

            while (scanner.hasNext()){
                data += scanner.nextLine();
            }

            scanner.close();

            JSONParser jsonParser = new JSONParser();
            JSONObject JSONObject = (JSONObject) jsonParser.parse(data);

            //Get the required data using its key
            System.out.println(String.valueOf(JSONObject.get("fact")));


        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
    
}
