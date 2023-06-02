import 'package:flutter/material.dart';
import 'package:prac2/screens/home_screen.dart';

void main() {
  runApp(const App());
}

class App extends StatelessWidget {
  const App({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(
        textTheme: const TextTheme(
          displayLarge: TextStyle(
            color: Color(0xFF232B55),
          ),
        ),
        cardColor: const Color(0xFFF4EDDB),
        colorScheme: const ColorScheme(
          brightness: Brightness.light,
          primary: Color(0xFF232B55),
          onPrimary: Color(0xFF14626C),
          secondary: Color(0xFFE7116C),
          onSecondary: Color(0xFFE7146C),
          error: Color(0xFFE76211),
          onError: Color(0xFFE76214),
          background: Color(0xFFE7626C),
          onBackground: Color(0xFFE7626C),
          surface: Color(0xFF11116C),
          onSurface: Color(0xFF22226C),
        ),
      ),
      home: const HomeScreen(),
    );
  }
}
