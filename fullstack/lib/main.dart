import 'package:flutter/material.dart';
import 'pages/home.dart';
import 'pages/login.dart';
import 'pages/profile.dart';


void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: LoginPage(),
      //home: HomePage()
      //home: ProfilePage()
    );
  }
}
