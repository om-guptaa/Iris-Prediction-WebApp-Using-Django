# Iris-Prediction-WebApp-Using-Django
A webapp made using django and python which takes in four input parameters and classify according to ML model trained.

To run the app,clone or download all the files.
Go to cmd and directory of files.
RUN command
python manage.py runserver 


import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class EnvironmentFileComparison {
    public static void main(String[] args) {
        File envFile1 = new File("env1.properties");
        File envFile2 = new File("env2.properties");
        File appFile = new File("app.properties");
        Map<String, String> env1 = new HashMap<>();
        Map<String, String> env2 = new HashMap<>();
        Map<String, String> appValues = new HashMap<>();

        try {
            // Read values from env1 file
            Scanner scanEnvFile1 = new Scanner(envFile1);
            while (scanEnvFile1.hasNextLine()) {
                String line = scanEnvFile1.nextLine();
                if (!line.startsWith("#")) {
                    String[] keyValue = line.split("=");
                    if (keyValue.length == 2) {
                        String value = keyValue[1];
                        // Check if value contains ${...}
                        if (value.matches(".*\\$\\{.*\\}.*")) {
                            // Extract all ${...} occurrences
                            Pattern pattern = Pattern.compile("\\$\\{(.+?)\\}");
                            Matcher matcher = pattern.matcher(value);
                            StringBuilder sb = new StringBuilder(value);
                            while (matcher.find()) {
                                String token = matcher.group(1);
                                String appValue = appValues.get(token);
                                if (appValue != null) {
                                    sb.replace(matcher.start(), matcher.end(), appValue);
                                }
                            }
                            value = sb.toString();
                        }
                        env1.put(keyValue[0], value);
                    }
                }
            }
            scanEnvFile1.close();

            // Read values from env2 file
            Scanner scanEnvFile2 = new Scanner(envFile2);
            while (scanEnvFile2.hasNextLine()) {
                String line = scanEnvFile2.nextLine();
                if (!line.startsWith("#")) {
                    String[] keyValue = line.split("=");
                    if (keyValue.length == 2) {
                        String value = keyValue[1];
                        // Check if value contains ${...}
                        if (value.matches(".*\\$\\{.*\\}.*")) {
                            // Extract all ${...} occurrences
                            Pattern pattern = Pattern.compile("\\$\\{(.+?)\\}");
                            Matcher matcher = pattern.matcher(value);
                            StringBuilder sb = new StringBuilder(value);
                            while (matcher.find()) {
                                String token = matcher.group(1);
                                String appValue = appValues.get(token);
                                if (appValue != null) {
                                    sb.replace(matcher.start(), matcher.end(), appValue);
                                }
                            }
                            value = sb.toString();
                        }
                        env2.put(keyValue[0], value);
                    }
                }
            }
            scanEnvFile2.close();

            // Read values from app file
            Scanner scanAppFile = new Scanner(appFile);
            while (scanAppFile.hasNextLine()) {
                String line = scanAppFile.nextLine();
                if (!line.startsWith("#")) {
                    String[] keyValue = line.split("=");
                    if (keyValue.length == 2) {
                        appValues.put(keyValue[0], keyValue[1]);
                    }
                }
            }
            scanAppFile.close();

        } catch (FileNotFoundException e) {
            System.out.println("File not found.");
        }

        // Compare env1 and env2 maps and create a new map with missing keys
        Map<String, String> missingKeysMap = new HashMap<>();
        Set<String> keys1 = env1.keySet();
        Set<String> keys2 = env2.keySet();

        for

