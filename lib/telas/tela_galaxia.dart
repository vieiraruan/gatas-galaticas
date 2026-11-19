import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:material_ui/material_ui.dart';

import '../componentes/gatos.dart';
import '../componentes/hud.dart';
import '../componentes/tema.dart';
import '../logica/regras.dart';
import '../providers.dart';

/// Mapa da galáxia: meta do dia, missões do dia, bimestre, nível e planetas.
class TelaGalaxia extends ConsumerWidget {
  final String perfilId;
  const TelaGalaxia({super.key, required this.perfilId});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final sessao = ref.watch(sessaoProvider(perfilId));
    return Scaffold(
      body: FundoEspacial(
        child: sessao.when(
          skipLoadingOnReload: true,
          loading: () => const Center(child: CircularProgressIndicator()),
          error: (e, _) => Center(
              child: Text('Erro: $e', style: const TextStyle(color: Colors.white))),
          data: (s) => s == null
              ? const Center(
                  child: Text('Astronauta não encontrado.',
                      style: TextStyle(color: Colors.white)))
              : _Mapa(s),
        ),
      ),
    );
  }
}

class _Mapa extends ConsumerWidget {
  final Sessao s;
  const _Mapa(this.s);

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final gato = gatoPorId(s.perfil.gato);
    final b = s.bimestre;
    final hoje = s.missoesHoje;
    const claro = TextStyle(color: Cores.textoClaro, fontSize: 15);
    return Column(
      children: [
        Hud(sessao: s),
        Expanded(
          child: ListView(
            padding: const EdgeInsets.fromLTRB(16, 18, 16, 40),
            children: [
              const Text('🚀', textAlign: TextAlign.center, style: TextStyle(fontSize: 40)),
              const Text('Galáxia do Saber',
                  textAlign: TextAlign.center,
                  style: TextStyle(
                      fontSize: 28, fontWeight: FontWeight.w900, color: Colors.white)),
              const SizedBox(height: 4),
              Text.rich(
                TextSpan(children: [
                  TextSpan(text: '${gato.titulo} ${gato.nome}, '),
                  TextSpan(
                      text: gato.descricao[0].toLowerCase() + gato.descricao.substring(1),
                      style: const TextStyle(fontStyle: FontStyle.italic)),
                  const TextSpan(text: ', e a tripulação felina precisam de você!'),
                ]),
                textAlign: TextAlign.center,
                style: const TextStyle(color: Color(0xFFC9CFF5), fontSize: 15),
              ),
              const SizedBox(height: 8),
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  for (final g in gatos)
                    Transform.scale(
                        scale: g.id == gato.id ? 1.25 : 1,
                        child: AvatarGato(g.id, tamanho: 34)),
                ],
              ),
              const SizedBox(height: 12),
              _MetaDoDia(xp: s.xpHoje),
              const SizedBox(height: 18),
              const Text('MISSÕES DE HOJE', textAlign: TextAlign.center, style: claro),
              const SizedBox(height: 8),
              if (hoje.isEmpty)
                const _Aviso('Nenhuma missão disponível neste bimestre ainda. 🛠️')
              else
                for (final m in hoje)
                  _CartaoMissaoHoje(
                    m: m,
                    onTap: () => context.go(
                        '/c/${s.perfil.id}/p/${m.planeta.id}/no/${m.indice}'),
                  ),
              const SizedBox(height: 18),
              const Text('BIMESTRE', textAlign: TextAlign.center, style: claro),
              const SizedBox(height: 8),
              Row(
                children: [
                  for (final bi in s.conteudo.bimestres)
                    Expanded(
                      child: Padding(
                        padding: const EdgeInsets.symmetric(horizontal: 3),
                        child: _Chip(
                          titulo: '${bi.numero}º',
                          subtitulo: !s.bimestreAberto(bi.numero)
                              ? '🔒'
                              : bi.numero == s.bimestreAtual
                                  ? 'agora'
                                  : '',
                          ligado: bi.numero == b.numero,
                          cor: Cores.ciano,
                          onTap: s.bimestreAberto(bi.numero)
                              ? () => ref
                                  .read(bimestreEscolhidoProvider.notifier)
                                  .escolher(bi.numero)
                              : null,
                        ),
                      ),
                    ),
                ],
              ),
              const SizedBox(height: 18),
              const Text('NÍVEL DA MISSÃO', textAlign: TextAlign.center, style: claro),
              const SizedBox(height: 8),
              for (var linha = 0; linha < s.niveis.length; linha += 2)
                Padding(
                  padding: const EdgeInsets.only(bottom: 8),
                  child: IntrinsicHeight(
                    child: Row(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
                      for (final n in s.niveis.skip(linha).take(2)) ...[
                        if (n != s.niveis[linha]) const SizedBox(width: 8),
                        Expanded(
                          child: _Chip(
                            titulo: '${n.emoji} ${n.nome}',
                            subtitulo:
                                '${n.descricao}\n${b.planetas.where((p) => RegrasPlaneta(p, s.progresso, n.id).resumo.chefao).length}/${b.planetas.length} planetas 👑',
                            ligado: n.id == s.perfil.nivel,
                            cor: n.cor,
                            onTap: () => ref
                                .read(acoesProvider)
                                .salvarPerfil(s.perfil.copyWith(nivel: n.id)),
                          ),
                        ),
                      ],
                    ]),
                  ),
                ),
              const SizedBox(height: 10),
              for (var i = 0; i < b.planetas.length; i++) ...[
                if (i > 0) const _Conector(),
                _CartaoPlaneta(
                  s: s,
                  indice: i,
                  onTap: () => context.go('/c/${s.perfil.id}/p/${b.planetas[i].id}'),
                ),
              ],
              const SizedBox(height: 26),
              Row(children: [
                Expanded(
                  child: Botao3D.branco(
                      texto: '👩‍🏫 Adulto', onPressed: () => mostrarPainelAdulto(context, s)),
                ),
                const SizedBox(width: 10),
                Expanded(
                  child: Botao3D.branco(
                      texto: '👥 Trocar', onPressed: () => context.go('/')),
                ),
              ]),
            ],
          ),
        ),
      ],
    );
  }
}

class _MetaDoDia extends StatelessWidget {
  final int xp;
  const _MetaDoDia({required this.xp});

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 10),
      decoration: BoxDecoration(
        color: Colors.white.withValues(alpha: 0.08),
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: Colors.white24),
      ),
      child: Row(children: [
        const Text('🎯 Meta do dia',
            style: TextStyle(color: Colors.white, fontWeight: FontWeight.w900)),
        const SizedBox(width: 10),
        Expanded(child: BarraProgresso(valor: xp / metaXpDia, cor: Cores.ouro, altura: 12)),
        const SizedBox(width: 10),
        Text('${xp.clamp(0, metaXpDia)}/$metaXpDia',
            style: const TextStyle(color: Colors.white, fontWeight: FontWeight.w900)),
      ]),
    );
  }
}

class _CartaoMissaoHoje extends StatelessWidget {
  final MissaoDoDia m;
  final VoidCallback onTap;
  const _CartaoMissaoHoje({required this.m, required this.onTap});

  @override
  Widget build(BuildContext context) {
    final p = m.planeta;
    return Padding(
      padding: const EdgeInsets.only(bottom: 8),
      child: Material(
        color: Colors.white,
        borderRadius: BorderRadius.circular(18),
        child: InkWell(
          borderRadius: BorderRadius.circular(18),
          onTap: onTap,
          child: Container(
            padding: const EdgeInsets.all(10),
            decoration: BoxDecoration(
              borderRadius: BorderRadius.circular(18),
              border: Border.all(color: p.cor, width: 3),
            ),
            child: Row(children: [
              Container(
                width: 48,
                height: 48,
                alignment: Alignment.center,
                decoration: BoxDecoration(color: p.cor, shape: BoxShape.circle),
                child: Text(m.no.emoji, style: const TextStyle(fontSize: 26)),
              ),
              const SizedBox(width: 12),
              Expanded(
                child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                  Text(p.nomeCurto.toUpperCase(),
                      style: TextStyle(fontSize: 12, color: p.corEscura, fontWeight: FontWeight.w900)),
                  Text(m.no.rotulo,
                      style: const TextStyle(fontSize: 17, fontWeight: FontWeight.w900)),
                ]),
              ),
              Icon(Icons.rocket_launch, color: p.cor),
            ]),
          ),
        ),
      ),
    );
  }
}

class _Chip extends StatelessWidget {
  final String titulo;
  final String subtitulo;
  final bool ligado;
  final Color cor;
  final VoidCallback? onTap;

  const _Chip({
    required this.titulo,
    required this.subtitulo,
    required this.ligado,
    required this.cor,
    this.onTap,
  });

  @override
  Widget build(BuildContext context) {
    return Semantics(
      button: true,
      selected: ligado,
      child: GestureDetector(
        onTap: onTap,
        child: Opacity(
          opacity: onTap == null ? 0.5 : 1,
          child: Container(
            padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 6),
            alignment: Alignment.center,
            decoration: BoxDecoration(
              color: ligado ? cor.withValues(alpha: 0.25) : Colors.white.withValues(alpha: 0.06),
              borderRadius: BorderRadius.circular(16),
              border: Border.all(color: ligado ? cor : Colors.white24, width: ligado ? 3 : 2),
            ),
            child: Column(mainAxisSize: MainAxisSize.min, children: [
              Text(titulo,
                  textAlign: TextAlign.center,
                  style: const TextStyle(
                      color: Colors.white, fontWeight: FontWeight.w900, fontSize: 16)),
              if (subtitulo.isNotEmpty)
                Text(subtitulo,
                    textAlign: TextAlign.center,
                    style: const TextStyle(color: Cores.textoClaro, fontSize: 11)),
            ]),
          ),
        ),
      ),
    );
  }
}

class _CartaoPlaneta extends StatelessWidget {
  final Sessao s;
  final int indice;
  final VoidCallback onTap;
  const _CartaoPlaneta({required this.s, required this.indice, required this.onTap});

  @override
  Widget build(BuildContext context) {
    final p = s.bimestre.planetas[indice];
    final r = s.regras(p);
    final res = r.resumo;
    return Padding(
      padding: EdgeInsets.only(left: indice.isOdd ? 22 : 0, right: indice.isOdd ? 0 : 22),
      child: GestureDetector(
        onTap: onTap,
        child: Container(
          padding: const EdgeInsets.all(14),
          decoration: BoxDecoration(
            color: const Color(0xFF151A4A),
            borderRadius: BorderRadius.circular(26),
            border: Border.all(color: p.cor, width: 3),
            boxShadow: [BoxShadow(color: p.corEscura, offset: const Offset(0, 7))],
          ),
          child: Row(children: [
            Container(
              width: 76,
              height: 76,
              alignment: Alignment.center,
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                gradient: RadialGradient(colors: [p.cor, p.corEscura]),
              ),
              child: Text(p.emoji, style: const TextStyle(fontSize: 40)),
            ),
            const SizedBox(width: 14),
            Expanded(
              child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                Text('PLANETA ${indice + 1} · ${p.nomeCurto.toUpperCase()}',
                    style: const TextStyle(fontSize: 12, color: Cores.textoClaro)),
                Text(p.nome,
                    style: const TextStyle(
                        fontSize: 20, fontWeight: FontWeight.w900, color: Colors.white)),
                const SizedBox(height: 6),
                BarraProgresso(
                    valor: res.maximo == 0 ? 0 : res.ganhas / res.maximo, cor: p.cor, altura: 10),
                const SizedBox(height: 4),
                Text(
                  r.temConteudo
                      ? '⭐ ${res.ganhas}/${res.maximo} · ${res.feitas}/${res.total} missões${res.chefao ? ' · 👑' : ''}'
                      : '🛠️ Missões em construção',
                  style: const TextStyle(fontSize: 13, color: Cores.ouro),
                ),
              ]),
            ),
          ]),
        ),
      ),
    );
  }
}

class _Conector extends StatelessWidget {
  const _Conector();
  @override
  Widget build(BuildContext context) => Center(
        child: Container(
          width: 6,
          height: 24,
          margin: const EdgeInsets.symmetric(vertical: 4),
          decoration: BoxDecoration(
            color: Colors.white38,
            borderRadius: BorderRadius.circular(3),
          ),
        ),
      );
}

class _Aviso extends StatelessWidget {
  final String texto;
  const _Aviso(this.texto);
  @override
  Widget build(BuildContext context) => Container(
        padding: const EdgeInsets.all(14),
        decoration: BoxDecoration(
          color: Colors.white.withValues(alpha: 0.08),
          borderRadius: BorderRadius.circular(16),
        ),
        child: Text(texto,
            textAlign: TextAlign.center, style: const TextStyle(color: Colors.white)),
      );
}

/// Explicações para o adulto, como no material original.
void mostrarPainelAdulto(BuildContext context, Sessao s) {
  showModalBottomSheet<void>(
    context: context,
    isScrollControlled: true,
    backgroundColor: Colors.white,
    shape: const RoundedRectangleBorder(
        borderRadius: BorderRadius.vertical(top: Radius.circular(24))),
    builder: (c) => DraggableScrollableSheet(
      expand: false,
      initialChildSize: 0.85,
      builder: (c, sc) => ListView(
        controller: sc,
        padding: const EdgeInsets.fromLTRB(20, 16, 20, 32),
        children: [
          const Text('👩‍🏫 Para o adulto',
              style: TextStyle(fontSize: 22, fontWeight: FontWeight.w900)),
          const SizedBox(height: 10),
          for (final t in [
            '• Cada bimestre tem planetas (as matérias). Cada planeta tem setores (os assuntos), missões, revisões 🏆, cápsulas 📦 e um chefão no final.',
            '• O app abre no bimestre do calendário escolar. Os anteriores ficam abertos para revisar; os próximos ficam trancados.',
            '• "Missões de hoje" segue o rodízio da BNCC: Português e Matemática todo dia, mais Ciências, História ou Geografia. Sexta é dia de revisão.',
            '• Níveis: cada um tem progresso e estrelas próprios. Comece no Fácil; quando vencer o chefão, suba de nível. O Gênio do Universo tem tempo por pergunta.',
            '• Sessões curtas: 2 missões (cerca de 8 minutos). Meta do dia: $metaXpDia XP.',
            '• Cada missão começa com cartões de explicação. Leia junto e peça para a criança explicar com as palavras dela. O botão 🔊 lê em voz alta.',
            '• Errou? Aparece a explicação e a pergunta volta no fim. No chefão, cada acerto tira vida do monstro. Ninguém "perde".',
            '• Em Matemática os números mudam a cada partida.',
            '• Missões com 🛠️ ainda não têm perguntas: o conteúdo desses bimestres está sendo escrito.',
            '• O progresso fica salvo neste aparelho.',
          ])
            Padding(
              padding: const EdgeInsets.only(bottom: 8),
              child: Text(t, style: const TextStyle(fontSize: 15, height: 1.45)),
            ),
          const SizedBox(height: 8),
          Botao3D.branco(
            texto: '✏️ Editar nome, ano ou capitão',
            onPressed: () {
              Navigator.pop(c);
              context.go('/c/${s.perfil.id}/editar');
            },
          ),
          const SizedBox(height: 8),
          Botao3D(texto: 'FECHAR', onPressed: () => Navigator.pop(c)),
        ],
      ),
    ),
  );
}
