import 'package:flutter/material.dart';


class ProfilePage extends StatelessWidget {
  final String username;

  ProfilePage({super.key, required this.username});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.green[100],
      body: SafeArea( //avoids notch area
        child: Center(
          child: Column(
            children: [
              SizedBox(height: 50),

              Text(
                '$username\' profile page.',
                style: TextStyle(
                  color: Colors.black87,
                  fontSize: 50,
                  fontWeight: FontWeight.bold
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}