import 'package:flutter/material.dart';

class MyTextField extends StatelessWidget {

  final controller;
  final String hintText;
  final bool obscureText;

  const MyTextField({super.key, required this.controller, required this.hintText, required this.obscureText});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: EdgeInsets.only(left: 200, right: 200, top: 20),
      child: TextField(
        controller: controller,
        obscureText: obscureText,
        decoration: InputDecoration(
          enabledBorder: OutlineInputBorder(
            borderSide: BorderSide(color: Colors.black87),
            borderRadius: BorderRadius.all(Radius.circular(12.0))
          ),
          focusedBorder: OutlineInputBorder(
            borderSide: BorderSide(color: Colors.white),
            borderRadius: BorderRadius.all(Radius.circular(12.0))
          ),
          fillColor: Colors.white,
          filled: true,
          hintText: hintText,
          hintStyle: TextStyle(color: Colors.grey[400]),
        ),
      ),
    );
  }
}