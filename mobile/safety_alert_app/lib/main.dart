import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'package:geolocator/geolocator.dart';

void main() {
  runApp(SafetyApp());
}

class SafetyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Safety Alert',
      home: PanicScreen(),
      debugShowCheckedModeBanner: false,
    );
  }
}

class PanicScreen extends StatefulWidget {
  @override
  _PanicScreenState createState() => _PanicScreenState();
}

class _PanicScreenState extends State<PanicScreen> {

Future<void> sendAlert() async {

  print("Starting sendAlert()");

  double latitude = 17.3850;
  double longitude = 78.4867;

  final response = await http.post(
    Uri.parse("http://localhost:8000/trigger-alert"),
    headers: {"Content-Type": "application/json"},
    body: jsonEncode({
      "user_name": "Bindhu",
      "latitude": latitude,
      "longitude": longitude,
      "contacts": ["+918074305770"]
    }),
  );

  print("API Response: ${response.body}");
}

@override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      body: Center(
        child: GestureDetector(
          onLongPress: () {
  print("PANIC BUTTON PRESSED");
  sendAlert();
},
          child: Container(
            width: 200,
            height: 200,
            decoration: BoxDecoration(
              color: Colors.red,
              shape: BoxShape.circle,
            ),
            child: Center(
              child: Text(
                "PANIC",
                style: TextStyle(
                  color: Colors.white,
                  fontSize: 32,
                  fontWeight: FontWeight.bold,
                ),
              ),
            ),
          ),
        ),
      ),
    );
  }
}