import 'package:go_router/go_router.dart';
import 'package:material_ui/material_ui.dart';

import 'componentes/tema.dart';
import 'telas/tela_galaxia.dart';
import 'telas/tela_labirinto.dart';
import 'telas/tela_novo_perfil.dart';
import 'telas/tela_partida.dart';
import 'telas/tela_perfis.dart';
import 'telas/tela_planeta.dart';

GoRouter criarRoteador() => GoRouter(routes: [
      GoRoute(
        path: '/',
        builder: (_, _) => const TelaPerfis(),
        routes: [
          GoRoute(
            path: 'novo-perfil',
            builder: (_, _) => const TelaNovoPerfil(),
          ),
          GoRoute(
            path: 'c/:perfilId',
            builder: (_, s) => TelaGalaxia(perfilId: s.pathParameters['perfilId']!),
            routes: [
              GoRoute(
                path: 'editar',
                builder: (_, s) =>
                    TelaNovoPerfil(perfilId: s.pathParameters['perfilId']),
              ),
              GoRoute(
                path: 'p/:planetaId',
                builder: (_, s) => TelaPlaneta(
                  perfilId: s.pathParameters['perfilId']!,
                  planetaId: s.pathParameters['planetaId']!,
                ),
                routes: [
                  GoRoute(
                    path: 'no/:indice',
                    builder: (_, s) => TelaPartida(
                      perfilId: s.pathParameters['perfilId']!,
                      planetaId: s.pathParameters['planetaId']!,
                      indice: int.parse(s.pathParameters['indice']!),
                    ),
                  ),
                  GoRoute(
                    path: 'labirinto/:indice',
                    builder: (_, s) => TelaLabirinto(
                      perfilId: s.pathParameters['perfilId']!,
                      planetaId: s.pathParameters['planetaId']!,
                      indice: int.parse(s.pathParameters['indice']!),
                    ),
                  ),
                ],
              ),
            ],
          ),
        ],
      ),
    ]);

class AppGalaxia extends StatefulWidget {
  const AppGalaxia({super.key});

  @override
  State<AppGalaxia> createState() => _AppGalaxiaState();
}

class _AppGalaxiaState extends State<AppGalaxia> {
  final _roteador = criarRoteador();

  @override
  Widget build(BuildContext context) => MaterialApp.router(
        title: 'Galáxia do Saber',
        debugShowCheckedModeBanner: false,
        theme: temaGalaxia(),
        routerConfig: _roteador,
      );
}
