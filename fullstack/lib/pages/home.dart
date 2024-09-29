import 'package:flutter/material.dart';
import 'package:fullstack/components/myButton.dart';
import '../pages/login.dart';

class HomePage extends StatelessWidget {

  HomePage({super.key, required this.username});

  final String username;

  void signUserOut(BuildContext context) {

    // If authentication is successful, navigate to the HomePage and pass the username
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => LoginPage(),
      ),
    );

    // The Navigator.push method is correctly used here without trying to assign its result to a variable or use it in an invalid way.
  }




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
                'You have signed in. Welcome back, $username!',
                style: TextStyle(
                  color: Colors.black87,
                  fontSize: 20,
                ),
              ),
              
              Expanded(child: Container()),

              MyButton (
                onTap: () => signUserOut(context),
                buttonText: "Sign Out"
              ),

              SizedBox(height: 20),

            ],
          ),
        ),
      ),
    );
  }
}
