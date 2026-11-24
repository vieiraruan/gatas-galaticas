import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:material_ui/material_ui.dart';

import '../componentes/astros.dart';
import '../componentes/tema.dart';
import '../componentes/texto_rico.dart';
import '../componentes/visuais.dart';
import '../logica/regras.dart';
import '../modelos/conteudo.dart';
import '../providers.dart';

/// Caminho de um planeta (assunto): missões, revisão e cápsula.
/// `planetaId` é a matéria do bimestre no conteúdo e `setor` é o assunto;
/// setor -1 mostra a estação do chefão e null mostra o bimestre inteiro.
class TelaPlaneta extends ConsumerWidget {
  final String perfilId;
  final String planetaId;
  final int? setor;
  const TelaPlaneta({super.key, required this.perfilId, required this.planetaId, this.setor});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final sessao = ref.watch(sessaoProvider(perfilId));
    return Scaffold(
      body: FundoEspacial(
        child: sessao.when(
          skipLoadingOnReload: true,
          loading: () => const Center(child: CircularProgressIndicator()),
          error: (e, _) => Center(child: Text('Erro: $e')),
          data: (s) {
            final p = s?.planeta(planetaId);
            if (s == null || p == null) {
              return const Center(
                  child: Text('Planeta não encontrado.', style: TextStyle(color: Colors.white)));
            }
            return _Caminho(s: s, planeta: p, setor: setor);
          },
        ),
      ),
    );
  }
}

class _Caminho extends ConsumerStatefulWidget {
  final Sessao s;
  final Planeta planeta;
  final int? setor;
  const _Caminho({required this.s, required this.planeta, this.setor});

  @override
  ConsumerState<_Caminho> createState() => _CaminhoState();
}

class _CaminhoState extends ConsumerState<_Caminho> {
  final _chaveAtual = GlobalKey();

  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addPostFrameCallback((_) {
      final c = _chaveAtual.currentContext;
      final ro = c?.findRenderObject();
      if (c != null && ro is RenderBox && ro.hasSize) Scrollable.ensureVisible(c, alignment: 0.4);
    });
  }

  @override
  Widget build(BuildContext context) {
    final s = widget.s, p = widget.planeta;
    final r = s.regras(p);
    final res = r.resumo;
    final so = widget.setor;
    final materia = materiaDoPlaneta(p);
    const desloc = [0.0, 50, 74, 50, 0, -50, -74, -50];
    final atual = so != null && so >= 0 ? r.atualDoSetor(so) : r.atual;
    final capsulaPronta = [for (var i = 0; i < r.nos.length; i++) r.capsulaPronta(i)];
    final filhos = <Widget>[];
    var k = 0;
    for (var i = 0; i < r.nos.length; i++) {
      final no = r.nos[i];
      if (so != null && setorDoNo(no) != so) continue;
      if (no is NoMissao && no.setor.missoes.first == no.missao) {
        k = 0;
        filhos.add(_BannerSetor(
          planeta: p,
          setor: no.setor,
          indice: no.indiceSetor,
          onResumo: () => _resumo(context, p, no.setor, no.indiceSetor),
        ));
      }
      if (no is NoChefao) {
        filhos.add(_BannerChefao(planeta: p));
      }
      final ehAtual = i == atual || capsulaPronta[i];
      filhos.add(Transform.translate(
        offset: Offset(no is NoChefao ? 0 : desloc[k % 8].toDouble(), 0),
        child: _No(
          key: i == atual ? _chaveAtual : null,
          no: no,
          planeta: p,
          estrelas: r.estrelas(no),
          bloqueado: r.bloqueado(i),
          atual: ehAtual,
          foguete: i == atual,
          capsulaAberta: no is NoCapsula && r.capsulaAberta(no),
          onTap: () => _abrirNo(context, r, i),
        ),
      ));
      k++;
    }
    final titulo = so == null
        ? p.nome
        : so < 0
            ? 'Estação do chefão'
            : p.setores[so].titulo;
    final estrelasTopo = so == null || so < 0
        ? '⭐ ${res.ganhas}/${res.maximo}'
        : '⭐ ${r.resumoDoSetor(so).ganhas}/${r.resumoDoSetor(so).maximo}';
    return Column(children: [
      Container(
        color: p.cor,
        padding: EdgeInsets.fromLTRB(4, MediaQuery.paddingOf(context).top + 4, 14, 10),
        child: Row(children: [
          IconButton(
            tooltip: 'Voltar para a galáxia',
            icon: const Icon(Icons.arrow_back, color: Colors.white),
            onPressed: () => context.go('/c/${s.perfil.id}/g/$materia'),
          ),
          if (so != null && so >= 0)
            DesenhoPlaneta(cor: Colors.white, semente: p.setores[so].id, tamanho: 42)
          else
            Text(so == null ? p.emoji : p.chefaoEmoji, style: const TextStyle(fontSize: 30)),
          const SizedBox(width: 8),
          Expanded(
            child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              Text(titulo,
                  style: const TextStyle(
                      color: Colors.white, fontSize: 19, fontWeight: FontWeight.w900)),
              Text('${galaxiaDe(materia).nome} · ${s.nivel.emoji} ${s.nivel.nome} · $estrelasTopo',
                  style: const TextStyle(color: Colors.white, fontSize: 12)),
            ]),
          ),
          Text('🐟${s.progresso.peixinhos}',
              style: const TextStyle(
                  color: Cores.ciano, fontSize: 17, fontWeight: FontWeight.w900)),
        ]),
      ),
      Expanded(
        child: SingleChildScrollView(
          padding: const EdgeInsets.only(bottom: 70),
          child: Column(children: filhos),
        ),
      ),
    ]);
  }

  void _abrirNo(BuildContext context, RegrasPlaneta r, int i) {
    final s = widget.s, p = widget.planeta, no = r.nos[i];
    if (no is NoCapsula && r.capsulaPronta(i)) {
      _abrirCapsula(context, no);
      return;
    }
    final bloqueado = r.bloqueado(i);
    final estrelas = r.estrelas(no);
    final vazio = emBreve(no);
    final n = s.nivel;
    final descricao = switch (no) {
      NoMissao(:final missao, :final setor) => vazio
          ? (missao.descricao ?? 'Missão em construção.')
          : 'Planeta ${setor.titulo} · ${n.perguntasMissao} perguntas',
      NoRevisao() => 'Mistura as missões do planeta · ${n.perguntasRevisao} perguntas',
      NoCapsula() => r.capsulaAberta(no)
          ? 'Você já abriu esta cápsula!'
          : 'Termine a revisão para abrir.',
      NoChefao() =>
        'Derrote o chefão acertando ${n.perguntasChefao} perguntas de todos os planetas do bimestre ${p.emoji}',
      _ => '',
    };
    showModalBottomSheet<void>(
      context: context,
      backgroundColor: Colors.white,
      shape: const RoundedRectangleBorder(
          borderRadius: BorderRadius.vertical(top: Radius.circular(22))),
      builder: (c) => SafeArea(
        child: Padding(
          padding: const EdgeInsets.fromLTRB(18, 18, 18, 18),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              Text('${no.emoji} ${no.rotulo}',
                  style: const TextStyle(fontSize: 22, fontWeight: FontWeight.w900)),
              const SizedBox(height: 4),
              Text(descricao, style: const TextStyle(fontSize: 16, color: Color(0xFF555555))),
              Text('Nível: ${n.emoji} ${n.nome}',
                  style: const TextStyle(fontSize: 16, color: Color(0xFF555555))),
              if (estrelas > 0)
                Text('★' * estrelas + '☆' * (3 - estrelas),
                    style: const TextStyle(fontSize: 22, color: Cores.ouro)),
              const SizedBox(height: 12),
              if (vazio)
                const Text('🛠️ As perguntas desta missão ainda estão sendo escritas.',
                    style: TextStyle(fontSize: 15))
              else if (bloqueado && no is NoChefao)
                const Text('🔒 Complete as missões de todos os planetas do bimestre para enfrentar o chefão.',
                    style: TextStyle(fontSize: 15))
              else if (bloqueado && no is! NoCapsula)
                const Text('🔒 Termine a missão anterior para liberar esta.',
                    style: TextStyle(fontSize: 15)),
              const SizedBox(height: 8),
              if (vazio || bloqueado || no is NoCapsula)
                Botao3D.branco(texto: 'OK', onPressed: () => Navigator.pop(c))
              else if (no is NoChefao)
                Botao3D.ouro(
                  texto: '⚔️ ENFRENTAR O CHEFÃO',
                  onPressed: () {
                    Navigator.pop(c);
                    context.go('/c/${s.perfil.id}/p/${p.id}/no/$i');
                  },
                )
              else
                Botao3D(
                  cor: p.cor,
                  corSombra: p.corEscura,
                  texto: estrelas > 0 ? '🚀 JOGAR DE NOVO' : '🚀 DECOLAR',
                  onPressed: () {
                    Navigator.pop(c);
                    context.go('/c/${s.perfil.id}/p/${p.id}/no/$i');
                  },
                ),
            ],
          ),
        ),
      ),
    );
  }

  Future<void> _abrirCapsula(BuildContext context, NoCapsula no) async {
    final s = widget.s;
    final ganho = peixinhosDaCapsula(s.nivel, ref.read(aleatorioProvider));
    await ref.read(acoesProvider).abrirCapsula(
        perfilId: s.perfil.id, nivel: s.perfil.nivel, noId: no.id, peixinhos: ganho);
    if (!context.mounted) return;
    await showDialog<void>(
      context: context,
      builder: (c) => Dialog(
        backgroundColor: Cores.espaco,
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(24)),
        child: Padding(
          padding: const EdgeInsets.all(22),
          child: Column(mainAxisSize: MainAxisSize.min, children: [
            const Text('Cápsula de suprimentos!',
                textAlign: TextAlign.center,
                style: TextStyle(color: Cores.ouro, fontSize: 24, fontWeight: FontWeight.w900)),
            const Text('📦', style: TextStyle(fontSize: 96)),
            Text('+$ganho 🐟',
                style: const TextStyle(
                    color: Cores.ciano, fontSize: 34, fontWeight: FontWeight.w900)),
            const SizedBox(height: 6),
            const Text('A tripulação felina agradece os peixinhos! 😻',
                textAlign: TextAlign.center,
                style: TextStyle(color: Colors.white, fontSize: 17)),
            const SizedBox(height: 16),
            Botao3D.ouro(texto: 'GUARDAR NA NAVE', onPressed: () => Navigator.pop(c)),
          ]),
        ),
      ),
    );
  }

  void _resumo(BuildContext context, Planeta p, Setor setor, int indice) {
    final nome = widget.s.perfil.nome;
    showModalBottomSheet<void>(
      context: context,
      isScrollControlled: true,
      backgroundColor: Colors.white,
      builder: (c) => DraggableScrollableSheet(
        expand: false,
        initialChildSize: 0.9,
        builder: (c, sc) => ListView(
          controller: sc,
          padding: const EdgeInsets.fromLTRB(18, 16, 18, 30),
          children: [
            Text('📖 Resumo do planeta',
                style: const TextStyle(fontSize: 20, fontWeight: FontWeight.w900)),
            Text(setor.titulo,
                style: TextStyle(fontSize: 24, fontWeight: FontWeight.w900, color: p.cor)),
            for (final m in setor.missoes) ...[
              const SizedBox(height: 16),
              Text('${m.emoji} ${m.titulo}',
                  style: const TextStyle(fontSize: 19, fontWeight: FontWeight.w900)),
              if (m.briefing.isEmpty)
                Text(m.descricao ?? 'Em construção.',
                    style: const TextStyle(fontSize: 16, color: Cores.apagado)),
              for (final card in m.briefing)
                Container(
                  margin: const EdgeInsets.only(top: 10),
                  padding: const EdgeInsets.all(14),
                  decoration: BoxDecoration(
                    border: Border.all(color: Cores.linha, width: 2),
                    borderRadius: BorderRadius.circular(18),
                  ),
                  child: Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
                    Text(card.emoji, style: const TextStyle(fontSize: 32)),
                    const SizedBox(width: 12),
                    Expanded(
                      child: Column(children: [
                        TextoRico(card.texto,
                            nome: nome, estilo: const TextStyle(fontSize: 17, height: 1.4)),
                        Visuais(card.visuais, nome: nome),
                      ]),
                    ),
                  ]),
                ),
            ],
            const SizedBox(height: 18),
            Botao3D(cor: p.cor, corSombra: p.corEscura, texto: 'ENTENDI!', onPressed: () => Navigator.pop(c)),
          ],
        ),
      ),
    );
  }
}

class _BannerSetor extends StatelessWidget {
  final Planeta planeta;
  final Setor setor;
  final int indice;
  final VoidCallback onResumo;
  const _BannerSetor(
      {required this.planeta, required this.setor, required this.indice, required this.onResumo});

  @override
  Widget build(BuildContext context) {
    return Container(
      margin: const EdgeInsets.fromLTRB(14, 22, 14, 18),
      padding: const EdgeInsets.fromLTRB(16, 12, 12, 12),
      decoration: BoxDecoration(
        color: planeta.cor,
        borderRadius: BorderRadius.circular(18),
        boxShadow: [BoxShadow(color: planeta.corEscura, offset: const Offset(0, 4))],
      ),
      child: Row(children: [
        Expanded(
          child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Text(setor.subtitulo.isEmpty ? 'PLANETA ${indice + 1}' : setor.subtitulo,
                style: const TextStyle(color: Colors.white70, fontSize: 11, fontWeight: FontWeight.w900)),
            Text(setor.titulo,
                style: const TextStyle(color: Colors.white, fontSize: 19, fontWeight: FontWeight.w900)),
          ]),
        ),
        OutlinedButton(
          style: OutlinedButton.styleFrom(
            foregroundColor: Colors.white,
            side: const BorderSide(color: Colors.white70, width: 2),
            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
          ),
          onPressed: onResumo,
          child: const Text('📖 Resumo', style: TextStyle(fontWeight: FontWeight.w900)),
        ),
      ]),
    );
  }
}

class _BannerChefao extends StatelessWidget {
  final Planeta planeta;
  const _BannerChefao({required this.planeta});

  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,
      margin: const EdgeInsets.fromLTRB(14, 26, 14, 18),
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(
        gradient: const LinearGradient(colors: [Color(0xFF5B1468), Color(0xFF2A0733)]),
        borderRadius: BorderRadius.circular(18),
      ),
      child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
        const Text('MISSÃO FINAL',
            style: TextStyle(color: Colors.white70, fontSize: 11, fontWeight: FontWeight.w900)),
        Text('${planeta.chefaoEmoji} ${planeta.chefaoNome}',
            style: const TextStyle(color: Colors.white, fontSize: 19, fontWeight: FontWeight.w900)),
      ]),
    );
  }
}

class _No extends StatelessWidget {
  final No no;
  final Planeta planeta;
  final int estrelas;
  final bool bloqueado;
  final bool atual;
  final bool foguete;
  final bool capsulaAberta;
  final VoidCallback onTap;

  const _No({
    super.key,
    required this.no,
    required this.planeta,
    required this.estrelas,
    required this.bloqueado,
    required this.atual,
    required this.foguete,
    required this.capsulaAberta,
    required this.onTap,
  });

  @override
  Widget build(BuildContext context) {
    final vazio = emBreve(no);
    var icone = no.emoji;
    Color cor = planeta.cor, sombra = planeta.corEscura;
    if (no is NoRevisao) {
      cor = const Color(0xFFCE82FF);
      sombra = const Color(0xFFA568CC);
    }
    if (no is NoChefao) {
      cor = const Color(0xFF6A1B7A);
      sombra = const Color(0xFF3B0C45);
    }
    if (no is NoCapsula) {
      icone = capsulaAberta ? '🐾' : '📦';
      cor = const Color(0xFFFFB020);
      sombra = const Color(0xFFCC8A10);
      if (bloqueado || !atual && !capsulaAberta) {
        cor = const Color(0xFFE5E5E5);
        sombra = const Color(0xFFBDBDBD);
      }
    } else if (vazio) {
      icone = '🛠️';
      cor = const Color(0xFF3A3F70);
      sombra = const Color(0xFF262A55);
    } else if (bloqueado) {
      icone = '🔒';
      cor = const Color(0xFFE5E5E5);
      sombra = const Color(0xFFBDBDBD);
    } else if (estrelas > 0) {
      cor = Cores.ouro;
      sombra = Cores.ouroEscuro;
      if (no is NoMissao) icone = '⭐';
    }
    final tamanho = no is NoChefao ? 92.0 : 74.0;
    return Semantics(
      button: true,
      label: no.rotulo,
      child: GestureDetector(
        onTap: onTap,
        child: Padding(
          padding: const EdgeInsets.symmetric(vertical: 8),
          child: Column(mainAxisSize: MainAxisSize.min, children: [
            if (atual)
              Container(
                margin: const EdgeInsets.only(bottom: 6),
                padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                decoration: BoxDecoration(
                  color: Colors.white,
                  borderRadius: BorderRadius.circular(10),
                  border: Border.all(color: Cores.linha, width: 2),
                ),
                child: Text(
                  no is NoCapsula ? 'ABRIR!' : no is NoChefao ? 'BATALHA!' : 'DECOLAR',
                  style: TextStyle(color: planeta.cor, fontWeight: FontWeight.w900),
                ),
              ),
            Row(mainAxisSize: MainAxisSize.min, children: [
              if (foguete) const Text('🚀 ', style: TextStyle(fontSize: 26)),
              Container(
                width: tamanho,
                height: tamanho,
                alignment: Alignment.center,
                decoration: BoxDecoration(
                  color: cor,
                  shape: BoxShape.circle,
                  border: atual ? Border.all(color: Colors.white, width: 4) : null,
                  boxShadow: [BoxShadow(color: sombra, offset: const Offset(0, 6))],
                ),
                child: Text(icone, style: TextStyle(fontSize: tamanho * 0.45)),
              ),
            ]),
            const SizedBox(height: 6),
            SizedBox(
              width: 160,
              child: Text(no.rotulo,
                  textAlign: TextAlign.center,
                  style: const TextStyle(
                      color: Colors.white, fontSize: 13, fontWeight: FontWeight.w900)),
            ),
            if (no is! NoCapsula && estrelas > 0)
              Text('★' * estrelas + '☆' * (3 - estrelas),
                  style: const TextStyle(color: Cores.ouro, fontSize: 15)),
          ]),
        ),
      ),
    );
  }
}
