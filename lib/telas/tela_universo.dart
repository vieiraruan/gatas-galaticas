import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:material_ui/material_ui.dart';

import '../componentes/astros.dart';
import '../componentes/gatos.dart';
import '../componentes/hud.dart';
import '../componentes/nave.dart';
import '../componentes/tema.dart';
import '../logica/nave.dart';
import '../logica/regras.dart';
import '../modelos/rotina.dart';
import '../providers.dart';

/// Universo do ano: provas chegando, meta e missões do dia, a Nave
/// Gatística e as galáxias (uma por matéria).
class TelaUniverso extends ConsumerWidget {
  final String perfilId;
  const TelaUniverso({super.key, required this.perfilId});

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
    final aulasHoje = s.rotina.horario[s.hoje.weekday] ?? const <String>[];
    const claro = TextStyle(color: Cores.textoClaro, fontSize: 15);
    return Column(
      children: [
        Hud(sessao: s),
        Expanded(
          child: ListView(
            padding: const EdgeInsets.fromLTRB(16, 18, 16, 40),
            children: [
              const Text('🌌', textAlign: TextAlign.center, style: TextStyle(fontSize: 40)),
              Text('Universo do ${s.perfil.ano}º ano',
                  textAlign: TextAlign.center,
                  style: const TextStyle(
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
              for (final prova in s.provasProximas) ...[
                const SizedBox(height: 12),
                _CartaoProva(s: s, prova: prova),
              ],
              if (aulasHoje.isNotEmpty) ...[
                const SizedBox(height: 12),
                _Aviso('🏫 Hoje tem aula de: ${aulasHoje.map((m) => nomesMaterias[m] ?? m).join(', ')}'),
              ],
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
              _CartaoNave(s: s, onTap: () => context.go('/c/${s.perfil.id}/nave')),
              const SizedBox(height: 18),
              const Text('GALÁXIAS', textAlign: TextAlign.center, style: claro),
              const SizedBox(height: 8),
              GridView.count(
                shrinkWrap: true,
                physics: const NeverScrollableScrollPhysics(),
                crossAxisCount: 2,
                mainAxisSpacing: 12,
                crossAxisSpacing: 12,
                childAspectRatio: 0.82,
                children: [
                  for (final g in galaxias)
                    if (partesDaGalaxia(s.conteudo, g.materia).isNotEmpty)
                      _CartaoGalaxia(
                        s: s,
                        info: g,
                        onTap: () => context.go('/c/${s.perfil.id}/g/${g.materia}'),
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
                                '${n.descricao}\n${b.planetas.where((p) => RegrasPlaneta(p, s.progresso, n.id).resumo.chefao).length}/${b.planetas.length} chefões 👑',
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
              const SizedBox(height: 26),
              Row(children: [
                Expanded(
                  child: Botao3D.branco(
                      texto: '👨‍👩‍👧 Pais', onPressed: () => mostrarPainelAdulto(context, s)),
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
                  Text(
                      '${p.nomeCurto.toUpperCase()}'
                      '${m.no is NoMissao ? ' · ${(m.no as NoMissao).setor.titulo}' : ''}',
                      maxLines: 1,
                      overflow: TextOverflow.ellipsis,
                      style: TextStyle(fontSize: 12, color: p.corEscura, fontWeight: FontWeight.w900)),
                  Text(m.no.rotulo,
                      style: const TextStyle(fontSize: 17, fontWeight: FontWeight.w900)),
                  if (m.motivo != null)
                    Text(m.motivo!,
                        style: const TextStyle(
                            fontSize: 13, color: Color(0xFFB06A00), fontWeight: FontWeight.w900)),
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
          const Text('👨‍👩‍👧 Para os pais',
              style: TextStyle(fontSize: 22, fontWeight: FontWeight.w900)),
          const SizedBox(height: 10),
          for (final t in [
            '• Cada matéria é uma galáxia. Cada assunto é um planeta, com missões, revisão 🏆 e cápsula 📦. Cada bimestre da galáxia termina com um chefão.',
            '• Os planetas do bimestre do calendário e dos anteriores ficam abertos; os dos próximos bimestres ficam trancados.',
            '• Cada missão rende suprimentos da matéria. Com eles a criança constrói a Nave Gatística, em 4 etapas.',
            '• "Missões de hoje" segue o horário das aulas que você cadastrar na Área dos pais (ou o rodízio da BNCC). Provas marcadas por você passam na frente.',
            '• No meio das missões aparecem desafios relâmpago, e às vezes uma prova surpresa com perguntas do que já foi estudado.',
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
          Botao3D.ouro(
            texto: '🔐 ÁREA DOS PAIS',
            onPressed: () {
              Navigator.pop(c);
              context.go('/pais/f/${s.perfil.id}');
            },
          ),
          const SizedBox(height: 8),
          Botao3D(texto: 'FECHAR', onPressed: () => Navigator.pop(c)),
        ],
      ),
    ),
  );
}

class _CartaoProva extends StatelessWidget {
  final Sessao s;
  final Prova prova;
  const _CartaoProva({required this.s, required this.prova});

  @override
  Widget build(BuildContext context) {
    final dias = prova.diasAte(s.hoje);
    final quando = dias == 0
        ? 'é HOJE!'
        : dias == 1
            ? 'é amanhã!'
            : 'em $dias dias';
    final assuntos = [
      for (final a in prova.assuntos)
        if (s.setorPorId(a) case final x?) x.planeta.setores[x.setor].titulo,
      if (prova.observacao.isNotEmpty) prova.observacao,
    ];
    final treino = s.treino(prova);
    return Container(
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(
        color: const Color(0xFFFFF4CC),
        borderRadius: BorderRadius.circular(18),
        border: Border.all(color: Cores.ouro, width: 3),
      ),
      child: Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
        Text('📝 Prova de ${nomesMaterias[prova.materia] ?? prova.materia} $quando',
            style: const TextStyle(fontSize: 18, fontWeight: FontWeight.w900, color: Color(0xFF7A5A00))),
        if (assuntos.isNotEmpty)
          Text('Assuntos: ${assuntos.join(' · ')}',
              style: const TextStyle(fontSize: 14, color: Color(0xFF7A5A00))),
        if (treino != null) ...[
          const SizedBox(height: 8),
          Botao3D.ouro(
            texto: '🎯 TREINAR PARA A PROVA',
            altura: 46,
            onPressed: () => context.go('/c/${s.perfil.id}/treino/${prova.id}'),
          ),
        ],
      ]),
    );
  }
}

class _CartaoNave extends StatelessWidget {
  final Sessao s;
  final VoidCallback onTap;
  const _CartaoNave({required this.s, required this.onTap});

  @override
  Widget build(BuildContext context) {
    final pecas = s.progresso.pecas;
    final etapa = etapaAtual(pecas);
    final pronta = navePronta(pecas);
    final total = s.progresso.suprimentos.values.fold(0, (a, b) => a + b);
    final daParaConstruir = pecasNave.any(
        (p) => pecaLiberada(p, pecas) && podePagar(p, s.progresso.suprimentos));
    return GestureDetector(
      onTap: onTap,
      child: Container(
        padding: const EdgeInsets.all(12),
        decoration: BoxDecoration(
          color: const Color(0xFF151A4A),
          borderRadius: BorderRadius.circular(22),
          border: Border.all(color: Cores.ciano, width: 3),
          boxShadow: const [BoxShadow(color: Color(0xFF0E5A80), offset: Offset(0, 6))],
        ),
        child: Row(children: [
          NaveGatistica(pecas: pecas, tamanho: 74),
          const SizedBox(width: 12),
          Expanded(
            child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              const Text('NAVE GATÍSTICA',
                  style: TextStyle(fontSize: 12, color: Cores.textoClaro, fontWeight: FontWeight.w900)),
              Text(pronta ? 'Pronta para o salto! 🌀' : 'Etapa $etapa: ${etapasNave[etapa - 1]}',
                  style: const TextStyle(fontSize: 18, fontWeight: FontWeight.w900, color: Colors.white)),
              const SizedBox(height: 6),
              BarraProgresso(valor: pecas.length / pecasNave.length, cor: Cores.ciano, altura: 10),
              const SizedBox(height: 4),
              Text('🔧 ${pecas.length}/${pecasNave.length} peças · 📦 $total suprimentos',
                  style: const TextStyle(fontSize: 13, color: Cores.ouro)),
              if (daParaConstruir)
                const Text('✨ Dá para construir uma peça nova!',
                    style: TextStyle(fontSize: 13, color: Colors.white, fontWeight: FontWeight.w900)),
            ]),
          ),
        ]),
      ),
    );
  }
}

class _CartaoGalaxia extends StatelessWidget {
  final Sessao s;
  final InfoGalaxia info;
  final VoidCallback onTap;
  const _CartaoGalaxia({required this.s, required this.info, required this.onTap});

  @override
  Widget build(BuildContext context) {
    final partes = partesDaGalaxia(s.conteudo, info.materia);
    final cor = partes.first.planeta.cor;
    var ganhas = 0, maximo = 0, planetas = 0;
    for (final x in partes) {
      planetas += x.planeta.setores.length;
      if (!s.bimestreAberto(x.bimestre.numero)) continue;
      final r = s.regras(x.planeta).resumo;
      ganhas += r.ganhas;
      maximo += r.maximo;
    }
    final prova = s.provasProximas.where((p) => p.materia == info.materia).firstOrNull;
    return Semantics(
      button: true,
      label: info.nome,
      child: GestureDetector(
        onTap: onTap,
        child: Container(
          padding: const EdgeInsets.all(10),
          decoration: BoxDecoration(
            color: const Color(0xFF151A4A),
            borderRadius: BorderRadius.circular(22),
            border: Border.all(color: cor, width: 3),
            boxShadow: [BoxShadow(color: partes.first.planeta.corEscura, offset: const Offset(0, 6))],
          ),
          child: Column(children: [
            Expanded(child: DesenhoGalaxia(cor: cor, emoji: info.emoji, tamanho: 96)),
            Text(info.nome,
                textAlign: TextAlign.center,
                style: const TextStyle(fontSize: 15, fontWeight: FontWeight.w900, color: Colors.white)),
            Text('${nomesMaterias[info.materia]} · $planetas planetas',
                textAlign: TextAlign.center,
                style: const TextStyle(fontSize: 11, color: Cores.textoClaro)),
            const SizedBox(height: 5),
            BarraProgresso(valor: maximo == 0 ? 0 : ganhas / maximo, cor: cor, altura: 8),
            const SizedBox(height: 3),
            Text(prova != null ? '📝 Prova chegando!' : '⭐ $ganhas/$maximo',
                style: const TextStyle(fontSize: 12, color: Cores.ouro, fontWeight: FontWeight.w900)),
          ]),
        ),
      ),
    );
  }
}
