import 'package:flutter/material.dart';

class MyButton extends StatelessWidget {
  final String buttonText;
  final VoidCallback? onTap;

  const MyButton({
    super.key,
    required this.buttonText,
    this.onTap, // Make this parameter optional
  });

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: onTap, // Trigger the onTap callback when the button is tapped
      child: Container(
        padding: EdgeInsets.all(20),
        margin: EdgeInsets.symmetric(horizontal: 600), // Adjust margin as needed
        decoration: BoxDecoration(
          color: Colors.black,
          borderRadius: BorderRadius.circular(12),
        ),
        child: Center(
          child: Text(
            buttonText,
            style: TextStyle(
              color: Colors.grey[200],
              fontWeight: FontWeight.bold,
            ),
          ),
        ),
      ),
    );
  }
}