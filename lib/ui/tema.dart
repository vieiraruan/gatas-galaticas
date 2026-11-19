import 'package:material_ui/material_ui.dart';

const corPrimaria = Color(0xFF3D5AFE);

/// Cores por componente curricular, para a criança reconhecer a matéria.
Color corDoComponente(String componente) {
  switch (componente) {
    case 'Língua Portuguesa':
      return const Color(0xFFE53935);
    case 'Matemática':
      return const Color(0xFF1E88E5);
    case 'Ciências':
      return const Color(0xFF43A047);
    case 'História':
      return const Color(0xFF8E24AA);
    case 'Geografia':
      return const Color(0xFFFB8C00);
    default:
      return const Color(0xFF546E7A);
  }
}

ThemeData temaApp() {
  final esquema = ColorScheme.fromSeed(seedColor: corPrimaria);
  return ThemeData(
    colorScheme: esquema,
    useMaterial3: true,
    scaffoldBackgroundColor: const Color(0xFFF6F7FF),
    textTheme: Typography.blackMountainView.apply(
      bodyColor: const Color(0xFF1B1B2F),
      displayColor: const Color(0xFF1B1B2F),
    ),
    filledButtonTheme: FilledButtonThemeData(
      style: FilledButton.styleFrom(
        minimumSize: const Size(64, 56),
        textStyle: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
      ),
    ),
    cardTheme: CardThemeData(
      elevation: 0,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(20)),
    ),
  );
}
