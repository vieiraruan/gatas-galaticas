import 'package:go_router/go_router.dart';
import 'package:material_ui/material_ui.dart';

import '../logica/regras.dart';
import '../providers.dart';
import 'gatos.dart';
import 'tema.dart';

/// Barra do topo: avatar com nível, patente, XP, sequência e peixinhos.
class Hud extends StatelessWidget {
  final Sessao sessao;
  const Hud({super.key, required this.sessao});

  @override
  Widget build(BuildContext context) {
    final xp = sessao.progresso.xp;
    return Container(
      color: Colors.white,
      padding: EdgeInsets.fromLTRB(14, MediaQuery.paddingOf(context).top + 8, 14, 10),
      child: Row(children: [
        GestureDetector(
          onTap: () => context.go('/c/${sessao.perfil.id}/nave'),
          child: Stack(clipBehavior: Clip.none, children: [
            Container(
              width: 48,
              height: 48,
              alignment: Alignment.center,
              decoration: BoxDecoration(
                color: const Color(0xFFEFEBFF),
                shape: BoxShape.circle,
                border: Border.all(color: Cores.roxo, width: 3),
              ),
              child: AvatarGato(sessao.perfil.gato, tamanho: 38),
            ),
            Positioned(
              right: -8,
              bottom: -6,
              child: Container(
                padding: const EdgeInsets.symmetric(horizontal: 5, vertical: 1),
                decoration: BoxDecoration(
                  color: Cores.ouro,
                  borderRadius: BorderRadius.circular(10),
                  border: Border.all(color: Colors.white, width: 2),
                ),
                child: Text('Nv ${nivelJogador(xp)}',
                    style: const TextStyle(
                        fontSize: 11, fontWeight: FontWeight.w900, color: Color(0xFF6B4E00))),
              ),
            ),
          ]),
        ),
        const SizedBox(width: 12),
        Expanded(
          child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Text('${patente(xp)} ${sessao.perfil.nome} · ${xp % xpPorNivel}/$xpPorNivel XP',
                maxLines: 1,
                overflow: TextOverflow.ellipsis,
                style: const TextStyle(fontSize: 12, color: Cores.apagado)),
            const SizedBox(height: 4),
            BarraProgresso(valor: (xp % xpPorNivel) / xpPorNivel, cor: Cores.ouro, altura: 10),
          ]),
        ),
        const SizedBox(width: 10),
        Text('🔥${sessao.sequencia}',
            style: const TextStyle(fontSize: 17, fontWeight: FontWeight.w900)),
        const SizedBox(width: 8),
        Text('🐟${sessao.progresso.peixinhos}',
            style: const TextStyle(
                fontSize: 17, fontWeight: FontWeight.w900, color: Color(0xFF1C8FE0))),
      ]),
    );
  }
}

class BarraProgresso extends StatelessWidget {
  final double valor;
  final Color cor;
  final double altura;
  final Color fundo;

  const BarraProgresso({
    super.key,
    required this.valor,
    required this.cor,
    this.altura = 10,
    this.fundo = Cores.linha,
  });

  @override
  Widget build(BuildContext context) {
    return ClipRRect(
      borderRadius: BorderRadius.circular(altura),
      child: SizedBox(
        height: altura,
        child: Stack(fit: StackFit.expand, children: [
          Positioned.fill(child: ColoredBox(color: fundo)),
          FractionallySizedBox(
            alignment: Alignment.centerLeft,
            widthFactor: valor.clamp(0, 1).toDouble(),
            heightFactor: 1,
            child: DecoratedBox(
              decoration: BoxDecoration(
                  color: cor, borderRadius: BorderRadius.circular(altura)),
            ),
          ),
        ]),
      ),
    );
  }
}
