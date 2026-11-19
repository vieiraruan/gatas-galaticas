import 'package:material_ui/material_ui.dart';
import 'package:go_router/go_router.dart';

import 'features/mission/tela_missao.dart';
import 'features/profiles/tela_novo_perfil.dart';
import 'features/profiles/tela_perfis.dart';
import 'features/track/tela_trilha.dart';
import 'ui/tema.dart';

final roteador = GoRouter(
  routes: [
    GoRoute(
      path: '/',
      builder: (context, state) => const TelaPerfis(),
      routes: [
        GoRoute(
          path: 'novo-perfil',
          builder: (context, state) => const TelaNovoPerfil(),
        ),
        GoRoute(
          path: 'perfil/:perfilId',
          builder: (context, state) =>
              TelaTrilha(perfilId: state.pathParameters['perfilId']!),
          routes: [
            GoRoute(
              path: 'missao/:missaoId',
              builder: (context, state) => TelaMissao(
                perfilId: state.pathParameters['perfilId']!,
                missaoId: state.pathParameters['missaoId']!,
              ),
            ),
          ],
        ),
      ],
    ),
  ],
);

class AppAprender extends StatelessWidget {
  final GoRouter? router;

  const AppAprender({super.key, this.router});

  @override
  Widget build(BuildContext context) {
    return MaterialApp.router(
      title: 'Trilha do Saber',
      debugShowCheckedModeBanner: false,
      theme: temaApp(),
      routerConfig: router ?? roteador,
    );
  }
}
