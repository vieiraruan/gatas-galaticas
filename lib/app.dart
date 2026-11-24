import 'package:go_router/go_router.dart';
import 'package:material_ui/material_ui.dart';

import 'componentes/tema.dart';
import 'telas/tela_galaxia.dart';
import 'telas/tela_labirinto.dart';
import 'telas/tela_nave.dart';
import 'telas/tela_novo_perfil.dart';
import 'telas/tela_pais.dart';
import 'telas/tela_partida.dart';
import 'telas/tela_perfis.dart';
import 'telas/tela_planeta.dart';
import 'telas/tela_universo.dart';

GoRouter criarRoteador() => GoRouter(routes: [
      GoRoute(
        path: '/',
        builder: (_, _) => const TelaPerfis(),
        routes: [
          GoRoute(
            path: 'pais',
            builder: (_, _) => const TelaPais(),
            routes: [
              GoRoute(
                path: 'novo-perfil',
                builder: (_, _) => const PortaoPais(child: TelaNovoPerfil()),
              ),
              GoRoute(
                path: 'f/:perfilId',
                builder: (_, s) => TelaPaisFilho(perfilId: s.pathParameters['perfilId']!),
                routes: [
                  GoRoute(
                    path: 'editar',
                    builder: (_, s) => PortaoPais(
                        child: TelaNovoPerfil(perfilId: s.pathParameters['perfilId'])),
                  ),
                ],
              ),
            ],
          ),
          GoRoute(
            path: 'c/:perfilId',
            builder: (_, s) => TelaUniverso(perfilId: s.pathParameters['perfilId']!),
            routes: [
              GoRoute(
                path: 'nave',
                builder: (_, s) => TelaNave(perfilId: s.pathParameters['perfilId']!),
              ),
              GoRoute(
                path: 'g/:materia',
                builder: (_, s) => TelaGalaxia(
                  perfilId: s.pathParameters['perfilId']!,
                  materia: s.pathParameters['materia']!,
                ),
              ),
              GoRoute(
                path: 'surpresa',
                builder: (_, s) => TelaPartida.surpresa(perfilId: s.pathParameters['perfilId']!),
              ),
              GoRoute(
                path: 'treino/:provaId',
                builder: (_, s) => TelaPartida.treino(
                  perfilId: s.pathParameters['perfilId']!,
                  provaId: s.pathParameters['provaId']!,
                ),
              ),
              GoRoute(
                path: 'p/:planetaId',
                builder: (_, s) => TelaPlaneta(
                  perfilId: s.pathParameters['perfilId']!,
                  planetaId: s.pathParameters['planetaId']!,
                ),
                routes: [
                  GoRoute(
                    path: 's/:setor',
                    builder: (_, s) => TelaPlaneta(
                      perfilId: s.pathParameters['perfilId']!,
                      planetaId: s.pathParameters['planetaId']!,
                      setor: int.parse(s.pathParameters['setor']!),
                    ),
                  ),
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
        locale: const Locale('pt', 'BR'),
        supportedLocales: const [Locale('pt', 'BR')],
        localizationsDelegates: GlobalMaterialLocalizations.delegates,
        routerConfig: _roteador,
      );
}
