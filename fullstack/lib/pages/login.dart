import 'package:flutter/material.dart';
import 'package:fullstack/components/myButton.dart';
import '../components/textfield.dart';
import '../pages/home.dart';

class LoginPage extends StatelessWidget{
  LoginPage({super.key});

  // for user and password
  final usernameController = TextEditingController();
  final passwordController = TextEditingController();

  // signing user in

  void signUserIn(BuildContext context) {
    // Get the username from the controller
    String username = usernameController.text;

    // Add your authentication logic here (e.g., verify username and password)
    // If authentication is successful, navigate to the HomePage and pass the username
    Navigator.push(
      context,
      MaterialPageRoute(
        builder: (context) => HomePage(username: username),
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
              SizedBox(height:50),

            // logo
              Icon(
                Icons.lock,
                size: 100
              ),
          
          
            // Welcome back

              SizedBox(height:50),

              Text('Welcome back! It\'s good to see you again.',
              style: TextStyle(
                color: Colors.black87,
                fontSize: 20,
                ),
              ),
          
            // username input
              MyTextField(
                controller: usernameController,
                hintText: "Username",
                obscureText: false,
              ),
            //password input
              MyTextField(
                controller: passwordController,
                hintText: "Password",
                obscureText: true,
              ),
          
            // no forgot password page (yet)
          
            SizedBox(height:50),

            // sign in
            MyButton (
              onTap: () => signUserIn(context),
              buttonText: "Sign in",
              ),
            //if not member, register

            SizedBox(height:100),

            const Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Text("Not a member? Register now.",
                style: TextStyle(color: Colors.blue))
              ],) 
          
          ]),
        ),
      )
    );
  }

}
