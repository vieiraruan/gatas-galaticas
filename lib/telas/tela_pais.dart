import 'dart:math';

import 'package:flutter/services.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:go_router/go_router.dart';
import 'package:material_ui/material_ui.dart';

import '../componentes/gatos.dart';
import '../componentes/hud.dart';
import '../componentes/nave.dart';
import '../componentes/tema.dart';
import '../logica/nave.dart';
import '../logica/regras.dart';
import '../modelos/perfil.dart';
import '../modelos/rotina.dart';
import '../providers.dart';

const _diasSemana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta'];

String _dataBr(DateTime d) =>
    '${d.day.toString().padLeft(2, '0')}/${d.month.toString().padLeft(2, '0')}/${d.year}';

// ---------------------------------------------------------------------------
// Portão: PIN dos pais

/// Mostra `child` só depois do PIN dos pais (ou da criação do PIN).
class PortaoPais extends ConsumerWidget {
  final Widget child;
  const PortaoPais({super.key, required this.child});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    if (ref.watch(paisLiberadoProvider)) return child;
    final pin = ref.watch(pinProvider);
    return Scaffold(
      body: FundoEspacial(
        child: pin.when(
          loading: () => const Center(child: CircularProgressIndicator()),
          error: (e, _) => Center(child: Text('Erro: $e')),
          data: (p) => _TelaPin(pinSalvo: p),
        ),
      ),
    );
  }
}

class _TelaPin extends ConsumerStatefulWidget {
  final String? pinSalvo;
  const _TelaPin({required this.pinSalvo});

  @override
  ConsumerState<_TelaPin> createState() => _TelaPinState();
}

class _TelaPinState extends ConsumerState<_TelaPin> {
  String _digitado = '';
  String? _primeiro; // ao criar: o PIN digitado na 1ª vez
  String? _erro;

  bool get _criando => widget.pinSalvo == null;

  Future<void> _tecla(String t) async {
    if (_digitado.length >= 4) return;
    setState(() {
      _digitado += t;
      _erro = null;
    });
    if (_digitado.length < 4) return;
    final pin = _digitado;
    if (!_criando) {
      if (pin == widget.pinSalvo) {
        ref.read(paisLiberadoProvider.notifier).liberar();
      } else {
        setState(() {
          _digitado = '';
          _erro = 'PIN errado. Tente de novo.';
        });
      }
      return;
    }
    if (_primeiro == null) {
      setState(() {
        _primeiro = pin;
        _digitado = '';
      });
    } else if (_primeiro == pin) {
      await ref.read(acoesProvider).salvarPin(pin);
      ref.read(paisLiberadoProvider.notifier).liberar();
    } else {
      setState(() {
        _primeiro = null;
        _digitado = '';
        _erro = 'Os PINs não batem. Vamos recomeçar.';
      });
    }
  }

  Future<void> _esqueci() async {
    final rnd = Random();
    final a = 12 + rnd.nextInt(8), b = 6 + rnd.nextInt(4);
    final campo = TextEditingController();
    final ok = await showDialog<bool>(
      context: context,
      builder: (c) => AlertDialog(
        title: const Text('Esqueceu o PIN?'),
        content: Column(mainAxisSize: MainAxisSize.min, children: [
          Text('Para provar que é um adulto: quanto é $a × $b?'),
          TextField(
            key: const Key('campoEsqueci'),
            controller: campo,
            keyboardType: TextInputType.number,
            inputFormatters: [FilteringTextInputFormatter.digitsOnly],
          ),
        ]),
        actions: [
          TextButton(onPressed: () => Navigator.pop(c, false), child: const Text('Cancelar')),
          TextButton(
              onPressed: () => Navigator.pop(c, campo.text.trim() == '${a * b}'),
              child: const Text('Apagar PIN')),
        ],
      ),
    );
    if (ok == true) {
      await ref.read(acoesProvider).salvarPin(null);
    } else if (ok == false && mounted && campo.text.isNotEmpty) {
      setState(() => _erro = 'Resposta errada.');
    }
  }

  @override
  Widget build(BuildContext context) {
    final titulo = !_criando
        ? 'Digite o PIN dos pais'
        : _primeiro == null
            ? 'Crie um PIN de 4 números'
            : 'Digite o PIN de novo';
    return SafeArea(
      child: ListView(padding: const EdgeInsets.fromLTRB(24, 8, 24, 24), children: [
        Align(
          alignment: Alignment.centerLeft,
          child: IconButton(
            tooltip: 'Voltar',
            icon: const Icon(Icons.arrow_back, color: Colors.white),
            onPressed: () => context.go('/'),
          ),
        ),
        const Text('🔐', textAlign: TextAlign.center, style: TextStyle(fontSize: 56)),
        const Text('Área dos pais',
            textAlign: TextAlign.center,
            style: TextStyle(color: Cores.ouro, fontSize: 28, fontWeight: FontWeight.w900)),
        const SizedBox(height: 6),
        Text(titulo,
            textAlign: TextAlign.center,
            style: const TextStyle(color: Colors.white, fontSize: 18)),
        if (_criando)
          const Text('O PIN protege o cadastro, o horário e as provas das crianças.',
              textAlign: TextAlign.center, style: TextStyle(color: Cores.textoClaro)),
        const SizedBox(height: 16),
        Row(mainAxisAlignment: MainAxisAlignment.center, children: [
          for (var i = 0; i < 4; i++)
            Container(
              width: 22,
              height: 22,
              margin: const EdgeInsets.symmetric(horizontal: 8),
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                color: i < _digitado.length ? Cores.ouro : Colors.transparent,
                border: Border.all(color: Cores.ouro, width: 2),
              ),
            ),
        ]),
        if (_erro != null)
          Padding(
            padding: const EdgeInsets.only(top: 10),
            child: Text(_erro!,
                textAlign: TextAlign.center, style: const TextStyle(color: Color(0xFFFFB3B3))),
          ),
        const SizedBox(height: 18),
        for (final linha in const [
          ['1', '2', '3'],
          ['4', '5', '6'],
          ['7', '8', '9'],
          ['', '0', '⌫'],
        ])
          Padding(
            padding: const EdgeInsets.only(bottom: 10),
            child: Row(mainAxisAlignment: MainAxisAlignment.center, children: [
              for (final t in linha)
                Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 8),
                  child: SizedBox(
                    width: 76,
                    child: t.isEmpty
                        ? const SizedBox(height: 54)
                        : Botao3D.branco(
                            key: Key('tecla$t'),
                            texto: t,
                            onPressed: () => t == '⌫'
                                ? setState(() => _digitado = _digitado.isEmpty
                                    ? ''
                                    : _digitado.substring(0, _digitado.length - 1))
                                : _tecla(t),
                          ),
                  ),
                ),
            ]),
          ),
        if (!_criando)
          TextButton(
            onPressed: _esqueci,
            child: const Text('Esqueci o PIN', style: TextStyle(color: Cores.textoClaro)),
          ),
      ]),
    );
  }
}

// ---------------------------------------------------------------------------
// Lista de filhos

class TelaPais extends ConsumerWidget {
  const TelaPais({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final perfis = ref.watch(perfisProvider);
    final hoje = ref.watch(relogioProvider)();
    return PortaoPais(
      child: Scaffold(
        backgroundColor: const Color(0xFFF4F2FF),
        appBar: AppBar(
          title: const Text('👨‍👩‍👧 Área dos pais'),
          leading: IconButton(
            tooltip: 'Sair da área dos pais',
            icon: const Icon(Icons.close),
            onPressed: () {
              ref.read(paisLiberadoProvider.notifier).trancar();
              context.go('/');
            },
          ),
        ),
        body: perfis.when(
          loading: () => const Center(child: CircularProgressIndicator()),
          error: (e, _) => Center(child: Text('Erro: $e')),
          data: (lista) => ListView(padding: const EdgeInsets.all(16), children: [
            const Text('Seus filhos',
                style: TextStyle(fontSize: 22, fontWeight: FontWeight.w900)),
            const SizedBox(height: 4),
            const Text(
                'Cadastre cada criança, ajuste o horário das aulas, marque as provas e acompanhe os estudos.',
                style: TextStyle(color: Cores.apagado)),
            const SizedBox(height: 12),
            if (lista.isEmpty)
              const Card(
                child: Padding(
                  padding: EdgeInsets.all(16),
                  child: Text('Nenhuma criança cadastrada ainda.'),
                ),
              ),
            for (final p in lista) _CartaoFilho(perfil: p, hoje: hoje),
            const SizedBox(height: 12),
            Botao3D(
              texto: '➕ CADASTRAR FILHO',
              onPressed: () => context.go('/pais/novo-perfil'),
            ),
            const SizedBox(height: 10),
            Botao3D.branco(texto: '🔑 Trocar PIN', onPressed: () => _trocarPin(context, ref)),
          ]),
        ),
      ),
    );
  }

  Future<void> _trocarPin(BuildContext context, WidgetRef ref) async {
    await ref.read(acoesProvider).salvarPin(null);
    ref.read(paisLiberadoProvider.notifier).trancar();
  }
}

class _CartaoFilho extends ConsumerWidget {
  final PerfilCrianca perfil;
  final DateTime hoje;
  const _CartaoFilho({required this.perfil, required this.hoje});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final progresso = ref.watch(progressoProvider(perfil.id)).value;
    final rotina = ref.watch(rotinaProvider(perfil.id)).value;
    final prova = rotina?.proximas(hoje).firstOrNull;
    final xpHoje = progresso?.xpPorDia[chaveDia(hoje)] ?? 0;
    return Card(
      margin: const EdgeInsets.only(bottom: 10),
      child: InkWell(
        borderRadius: BorderRadius.circular(12),
        onTap: () => context.go('/pais/f/${perfil.id}'),
        child: Padding(
          padding: const EdgeInsets.all(12),
          child: Row(children: [
            AvatarGato(perfil.gato, tamanho: 56),
            const SizedBox(width: 12),
            Expanded(
              child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                Text('${perfil.nome} · ${perfil.ano}º ano',
                    style: const TextStyle(fontSize: 18, fontWeight: FontWeight.w900)),
                if (progresso != null)
                  Text(
                      'Hoje: $xpHoje/$metaXpDia XP · 🔥 ${sequenciaDias(progresso.xpPorDia, hoje)} dias seguidos',
                      style: const TextStyle(color: Cores.apagado)),
                if (prova != null)
                  Text(
                      '📝 Prova de ${nomesMaterias[prova.materia]} em ${_dataBr(prova.data)}',
                      style: const TextStyle(color: Color(0xFFB06A00), fontWeight: FontWeight.w900)),
              ]),
            ),
            const Icon(Icons.chevron_right),
          ]),
        ),
      ),
    );
  }
}

// ---------------------------------------------------------------------------
// Uma criança: acompanhamento, horário, provas e perfil

class TelaPaisFilho extends ConsumerWidget {
  final String perfilId;
  const TelaPaisFilho({super.key, required this.perfilId});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final sessao = ref.watch(sessaoProvider(perfilId));
    return PortaoPais(
      child: sessao.when(
        skipLoadingOnReload: true,
        loading: () => const Scaffold(body: Center(child: CircularProgressIndicator())),
        error: (e, _) => Scaffold(body: Center(child: Text('Erro: $e'))),
        data: (s) => s == null
            ? const Scaffold(body: Center(child: Text('Criança não encontrada.')))
            : DefaultTabController(
                length: 4,
                child: Scaffold(
                  backgroundColor: const Color(0xFFF4F2FF),
                  appBar: AppBar(
                    leading: IconButton(
                      tooltip: 'Voltar',
                      icon: const Icon(Icons.arrow_back),
                      onPressed: () => context.go('/pais'),
                    ),
                    title: Text('${s.perfil.nome} · ${s.perfil.ano}º ano'),
                    actions: [
                      TextButton(
                        onPressed: () => context.go('/c/${s.perfil.id}'),
                        child: const Text('▶ Jogar'),
                      ),
                    ],
                    bottom: const TabBar(labelPadding: EdgeInsets.symmetric(horizontal: 2), tabs: [
                      Tab(text: '📊 Estudos'),
                      Tab(text: '🏫 Horário'),
                      Tab(text: '📝 Provas'),
                      Tab(text: '👤 Perfil'),
                    ]),
                  ),
                  body: TabBarView(children: [
                    _AbaEstudos(s: s),
                    _AbaHorario(s: s),
                    _AbaProvas(s: s),
                    _AbaPerfil(s: s),
                  ]),
                ),
              ),
      ),
    );
  }
}

class _Secao extends StatelessWidget {
  final String titulo;
  final List<Widget> filhos;
  const _Secao(this.titulo, this.filhos);

  @override
  Widget build(BuildContext context) => Card(
        margin: const EdgeInsets.only(bottom: 12),
        child: Padding(
          padding: const EdgeInsets.all(14),
          child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Text(titulo, style: const TextStyle(fontSize: 17, fontWeight: FontWeight.w900)),
            const SizedBox(height: 8),
            ...filhos,
          ]),
        ),
      );
}

class _AbaEstudos extends StatelessWidget {
  final Sessao s;
  const _AbaEstudos({required this.s});

  @override
  Widget build(BuildContext context) {
    final p = s.progresso;
    final dias = [
      for (var i = 6; i >= 0; i--) DateTime(s.hoje.year, s.hoje.month, s.hoje.day - i)
    ];
    final xps = [for (final d in dias) p.xpPorDia[chaveDia(d)] ?? 0];
    final maiorXp = max(metaXpDia, xps.fold(0, max));
    final diasEstudados = xps.where((x) => x > 0).length;
    const letras = ['S', 'T', 'Q', 'Q', 'S', 'S', 'D'];

    // Reforço: missões com 1 estrela no nível atual.
    final reforco = <String>[];
    var missoesFeitas = 0;
    for (final pl in s.planetasAbertos) {
      final r = s.regras(pl);
      for (final n in r.nos) {
        if (n is! NoMissao) continue;
        final e = r.estrelas(n);
        if (e > 0) missoesFeitas++;
        if (e == 1) reforco.add('${nomesMaterias[materiaDoPlaneta(pl)]} · ${n.setor.titulo} · ${n.missao.titulo}');
      }
    }

    return ListView(padding: const EdgeInsets.all(14), children: [
      _Secao('Resumo', [
        Row(children: [
          AvatarGato(s.perfil.gato, tamanho: 52),
          const SizedBox(width: 12),
          Expanded(
            child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              Text('${patente(p.xp)} · nível ${nivelJogador(p.xp)} · ${p.xp} XP',
                  style: const TextStyle(fontWeight: FontWeight.w900)),
              Text('🔥 ${s.sequencia} dias seguidos · $diasEstudados de 7 dias com estudo'),
              Text('✅ $missoesFeitas missões concluídas · 🐟 ${p.peixinhos} peixinhos'),
              Text('🛸 Nave: ${p.pecas.length}/${pecasNave.length} peças'),
            ]),
          ),
        ]),
      ]),
      _Secao('Últimos 7 dias (XP)', [
        SizedBox(
          height: 120,
          child: Row(crossAxisAlignment: CrossAxisAlignment.end, children: [
            for (var i = 0; i < 7; i++)
              Expanded(
                child: Column(mainAxisAlignment: MainAxisAlignment.end, children: [
                  Text('${xps[i]}', style: const TextStyle(fontSize: 11, color: Cores.apagado)),
                  Container(
                    height: max(3, 70 * xps[i] / maiorXp).toDouble(),
                    margin: const EdgeInsets.symmetric(horizontal: 6),
                    decoration: BoxDecoration(
                      color: xps[i] >= metaXpDia ? Cores.certo : Cores.roxo,
                      borderRadius: BorderRadius.circular(6),
                    ),
                  ),
                  const SizedBox(height: 4),
                  Text(letras[dias[i].weekday - 1],
                      style: TextStyle(
                          fontWeight: i == 6 ? FontWeight.w900 : FontWeight.normal)),
                ]),
              ),
          ]),
        ),
        const Text('Verde = meta do dia batida.', style: TextStyle(fontSize: 12, color: Cores.apagado)),
      ]),
      _Secao('Por matéria (bimestres abertos)', [
        for (final g in galaxias)
          if (partesDaGalaxia(s.conteudo, g.materia).isNotEmpty) _LinhaMateria(s: s, info: g),
      ]),
      if (s.provasProximas.isNotEmpty)
        _Secao('Preparação para as provas', [
          for (final prova in s.provasProximas) _LinhaPreparo(s: s, prova: prova),
        ]),
      _Secao('Precisa de reforço', [
        if (reforco.isEmpty)
          const Text('Nenhuma missão com só 1 estrela. 👏')
        else ...[
          const Text('Missões feitas com 1 estrela no nível atual. Vale jogar de novo:',
              style: TextStyle(color: Cores.apagado)),
          const SizedBox(height: 4),
          for (final t in reforco.take(8)) Text('• $t'),
        ],
      ]),
    ]);
  }
}

class _LinhaMateria extends StatelessWidget {
  final Sessao s;
  final InfoGalaxia info;
  const _LinhaMateria({required this.s, required this.info});

  @override
  Widget build(BuildContext context) {
    final partes = partesDaGalaxia(s.conteudo, info.materia);
    var feitas = 0, total = 0;
    for (final x in partes.where((x) => s.bimestreAberto(x.bimestre.numero))) {
      final r = s.regras(x.planeta).resumo;
      feitas += r.feitas;
      total += r.total;
    }
    final acertos = s.progresso.acertosPorMateria[info.materia] ?? 0;
    final respostas = s.progresso.respostasPorMateria[info.materia] ?? 0;
    final pct = respostas == 0 ? null : (acertos * 100 / respostas).round();
    return Padding(
      padding: const EdgeInsets.only(bottom: 10),
      child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
        Row(children: [
          Expanded(
            child: Text('${info.emoji} ${nomesMaterias[info.materia]}',
                style: const TextStyle(fontWeight: FontWeight.w900)),
          ),
          Text(pct == null ? 'sem respostas ainda' : '$pct% de acertos',
              style: TextStyle(
                  color: pct == null
                      ? Cores.apagado
                      : pct >= 70
                          ? const Color(0xFF2A8A3E)
                          : const Color(0xFFB12A2A),
                  fontWeight: FontWeight.w900)),
        ]),
        const SizedBox(height: 4),
        BarraProgresso(
            valor: total == 0 ? 0 : feitas / total, cor: partes.first.planeta.cor, altura: 8),
        Text('$feitas de $total etapas concluídas',
            style: const TextStyle(fontSize: 12, color: Cores.apagado)),
      ]),
    );
  }
}

class _LinhaPreparo extends StatelessWidget {
  final Sessao s;
  final Prova prova;
  const _LinhaPreparo({required this.s, required this.prova});

  @override
  Widget build(BuildContext context) {
    var feitas = 0, total = 0;
    for (final a in prova.assuntos) {
      final x = s.setorPorId(a);
      if (x == null) continue;
      final r = s.regras(x.planeta).resumoDoSetor(x.setor);
      feitas += r.feitas;
      total += r.total;
    }
    final dias = prova.diasAte(s.hoje);
    return Padding(
      padding: const EdgeInsets.only(bottom: 8),
      child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
        Text(
            '${nomesMaterias[prova.materia]} · ${_dataBr(prova.data)} (${dias == 0 ? 'hoje' : 'em $dias dias'})',
            style: const TextStyle(fontWeight: FontWeight.w900)),
        if (total > 0) ...[
          BarraProgresso(valor: feitas / total, cor: Cores.ouro, altura: 8),
          Text('$feitas de $total etapas dos assuntos da prova',
              style: const TextStyle(fontSize: 12, color: Cores.apagado)),
        ] else
          const Text('Sem assuntos do app marcados: o treino usa o bimestre todo.',
              style: TextStyle(fontSize: 12, color: Cores.apagado)),
      ]),
    );
  }
}

class _AbaHorario extends ConsumerStatefulWidget {
  final Sessao s;
  const _AbaHorario({required this.s});

  @override
  ConsumerState<_AbaHorario> createState() => _AbaHorarioState();
}

class _AbaHorarioState extends ConsumerState<_AbaHorario> {
  late Map<int, List<String>> _horario = {
    for (final e in widget.s.rotina.horario.entries) e.key: List.of(e.value)
  };
  bool _mudou = false;

  void _alternar(int dia, String materia) => setState(() {
        final l = _horario.putIfAbsent(dia, () => []);
        l.contains(materia) ? l.remove(materia) : l.add(materia);
        _mudou = true;
      });

  Future<void> _salvar({bool limpar = false}) async {
    final s = widget.s;
    if (limpar) _horario = {};
    await ref.read(acoesProvider).salvarRotina(
        s.perfil.id, s.rotina.copyWith(horario: {
          for (final e in _horario.entries)
            if (e.value.isNotEmpty) e.key: e.value
        }));
    if (!mounted) return;
    setState(() => _mudou = false);
    ScaffoldMessenger.of(context)
        .showSnackBar(SnackBar(content: Text(limpar ? 'Voltamos ao rodízio sugerido.' : 'Horário salvo!')));
  }

  @override
  Widget build(BuildContext context) {
    final usandoSugestao = !_horario.values.any((l) => l.isNotEmpty);
    return ListView(padding: const EdgeInsets.all(14), children: [
      const Text(
          'Marque as matérias que têm aula em cada dia. As "Missões de hoje" da criança seguem esse horário, para reforçar o que foi visto na escola.',
          style: TextStyle(color: Cores.apagado)),
      if (usandoSugestao)
        const Padding(
          padding: EdgeInsets.only(top: 6),
          child: Text('Sem horário cadastrado: o app usa o rodízio sugerido pela BNCC.',
              style: TextStyle(fontWeight: FontWeight.w900)),
        ),
      const SizedBox(height: 10),
      for (var d = 1; d <= 5; d++)
        _Secao(_diasSemana[d - 1], [
          Wrap(spacing: 6, runSpacing: 6, children: [
            for (final g in galaxias)
              FilterChip(
                key: Key('aula$d${g.materia}'),
                label: Text('${g.emoji} ${nomesMaterias[g.materia]}'),
                selected: _horario[d]?.contains(g.materia) ?? false,
                onSelected: (_) => _alternar(d, g.materia),
              ),
          ]),
        ]),
      Botao3D(texto: 'SALVAR HORÁRIO', onPressed: _mudou ? _salvar : null),
      const SizedBox(height: 8),
      Botao3D.branco(
          texto: 'Usar o rodízio sugerido', onPressed: () => _salvar(limpar: true)),
    ]);
  }
}

class _AbaProvas extends ConsumerWidget {
  final Sessao s;
  const _AbaProvas({required this.s});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final provas = List.of(s.rotina.provas)..sort((a, b) => a.data.compareTo(b.data));
    final futuras = provas.where((p) => p.diasAte(s.hoje) >= 0).toList();
    final passadas = provas.where((p) => p.diasAte(s.hoje) < 0).toList().reversed;
    Widget cartao(Prova p, {bool passada = false}) {
      final assuntos = [
        for (final a in p.assuntos)
          if (s.setorPorId(a) case final x?) x.planeta.setores[x.setor].titulo,
      ];
      return Card(
        color: passada ? const Color(0xFFEDEDED) : null,
        child: ListTile(
          title: Text('${galaxiaDe(p.materia).emoji} ${nomesMaterias[p.materia]} · ${_dataBr(p.data)}',
              style: const TextStyle(fontWeight: FontWeight.w900)),
          subtitle: Text([
            if (assuntos.isNotEmpty) assuntos.join(' · '),
            if (p.observacao.isNotEmpty) p.observacao,
          ].join('\n')),
          isThreeLine: assuntos.isNotEmpty && p.observacao.isNotEmpty,
          trailing: IconButton(
            tooltip: 'Apagar prova',
            icon: const Icon(Icons.delete_outline),
            onPressed: () => ref.read(acoesProvider).salvarRotina(s.perfil.id,
                s.rotina.copyWith(provas: [for (final x in s.rotina.provas) if (x.id != p.id) x])),
          ),
          onTap: passada ? null : () => _editar(context, ref, p),
        ),
      );
    }

    return ListView(padding: const EdgeInsets.all(14), children: [
      const Text(
          'Em época de prova, marque a matéria, a data e os assuntos. A criança vê um aviso com contagem regressiva, as missões do dia passam a priorizar esses assuntos e aparece o botão "Treinar para a prova".',
          style: TextStyle(color: Cores.apagado)),
      const SizedBox(height: 10),
      Botao3D(texto: '➕ NOVA PROVA', onPressed: () => _editar(context, ref, null)),
      const SizedBox(height: 12),
      if (futuras.isEmpty) const Text('Nenhuma prova marcada.'),
      for (final p in futuras) cartao(p),
      if (passadas.isNotEmpty) ...[
        const SizedBox(height: 12),
        const Text('Provas que já passaram', style: TextStyle(fontWeight: FontWeight.w900)),
        for (final p in passadas) cartao(p, passada: true),
      ],
    ]);
  }

  Future<void> _editar(BuildContext context, WidgetRef ref, Prova? original) async {
    final nova = await showModalBottomSheet<Prova>(
      context: context,
      isScrollControlled: true,
      builder: (c) => _FormProva(s: s, original: original),
    );
    if (nova == null) return;
    await ref.read(acoesProvider).salvarRotina(
        s.perfil.id,
        s.rotina.copyWith(provas: [
          for (final x in s.rotina.provas)
            if (x.id != nova.id) x,
          nova,
        ]));
  }
}

class _FormProva extends StatefulWidget {
  final Sessao s;
  final Prova? original;
  const _FormProva({required this.s, this.original});

  @override
  State<_FormProva> createState() => _FormProvaState();
}

class _FormProvaState extends State<_FormProva> {
  late String _materia = widget.original?.materia ?? 'matematica';
  late DateTime _data =
      widget.original?.data ?? DateTime(widget.s.hoje.year, widget.s.hoje.month, widget.s.hoje.day + 7);
  late final Set<String> _assuntos = {...?widget.original?.assuntos};
  late final _obs = TextEditingController(text: widget.original?.observacao ?? '');

  @override
  void dispose() {
    _obs.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final s = widget.s;
    final partes = partesDaGalaxia(s.conteudo, _materia);
    return DraggableScrollableSheet(
      expand: false,
      initialChildSize: 0.9,
      builder: (c, sc) => ListView(
        controller: sc,
        padding: EdgeInsets.fromLTRB(18, 16, 18, 24 + MediaQuery.viewInsetsOf(context).bottom),
        children: [
          Text(widget.original == null ? '📝 Nova prova' : '📝 Editar prova',
              style: const TextStyle(fontSize: 22, fontWeight: FontWeight.w900)),
          const SizedBox(height: 12),
          const Text('Matéria', style: TextStyle(fontWeight: FontWeight.w900)),
          Wrap(spacing: 6, runSpacing: 6, children: [
            for (final g in galaxias)
              ChoiceChip(
                key: Key('materia${g.materia}'),
                label: Text('${g.emoji} ${nomesMaterias[g.materia]}'),
                selected: _materia == g.materia,
                onSelected: (_) => setState(() {
                  _materia = g.materia;
                  _assuntos.clear();
                }),
              ),
          ]),
          const SizedBox(height: 12),
          const Text('Data', style: TextStyle(fontWeight: FontWeight.w900)),
          OutlinedButton.icon(
            icon: const Icon(Icons.event),
            label: Text(_dataBr(_data)),
            onPressed: () async {
              final d = await showDatePicker(
                context: context,
                initialDate: _data,
                firstDate: DateTime(s.hoje.year - 1),
                lastDate: DateTime(s.hoje.year + 2),
              );
              if (d != null) setState(() => _data = d);
            },
          ),
          const SizedBox(height: 12),
          const Text('Assuntos que caem na prova', style: TextStyle(fontWeight: FontWeight.w900)),
          const Text('Os planetas da galáxia. Marque um ou mais.',
              style: TextStyle(color: Cores.apagado, fontSize: 13)),
          for (final x in partes)
            for (final setor in x.planeta.setores)
              CheckboxListTile(
                key: Key('assunto${setor.id}'),
                dense: true,
                contentPadding: EdgeInsets.zero,
                value: _assuntos.contains(setor.id),
                title: Text(setor.titulo),
                subtitle: Text('${x.bimestre.numero}º bimestre'),
                onChanged: (v) => setState(() =>
                    v == true ? _assuntos.add(setor.id) : _assuntos.remove(setor.id)),
              ),
          const SizedBox(height: 8),
          TextField(
            key: const Key('campoObservacao'),
            controller: _obs,
            maxLines: 2,
            decoration: const InputDecoration(
              labelText: 'Outros assuntos ou recados (opcional)',
              border: OutlineInputBorder(),
            ),
          ),
          const SizedBox(height: 14),
          Botao3D(
            texto: 'SALVAR PROVA',
            onPressed: () => Navigator.pop(
              context,
              Prova(
                id: widget.original?.id ?? DateTime.now().microsecondsSinceEpoch.toString(),
                materia: _materia,
                data: _data,
                assuntos: _assuntos.toList(),
                observacao: _obs.text.trim(),
              ),
            ),
          ),
        ],
      ),
    );
  }
}

class _AbaPerfil extends ConsumerWidget {
  final Sessao s;
  const _AbaPerfil({required this.s});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    return ListView(padding: const EdgeInsets.all(14), children: [
      _Secao('Perfil', [
        Row(children: [
          AvatarGato(s.perfil.gato, tamanho: 60),
          const SizedBox(width: 12),
          Expanded(
            child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              Text(s.perfil.nome, style: const TextStyle(fontSize: 20, fontWeight: FontWeight.w900)),
              Text('${s.perfil.ano}º ano · capitã(o) ${gatoPorId(s.perfil.gato).nome}'),
              Text('Nível: ${s.nivel.emoji} ${s.nivel.nome}'),
            ]),
          ),
        ]),
        const SizedBox(height: 12),
        Botao3D.branco(
          texto: '✏️ Editar nome, ano ou capitão',
          onPressed: () => context.go('/pais/f/${s.perfil.id}/editar'),
        ),
      ]),
      _Secao('Nave Gatística', [
        Center(child: NaveGatistica(pecas: s.progresso.pecas, tamanho: 120)),
        Text('${s.progresso.pecas.length}/${pecasNave.length} peças construídas. '
            'Suprimentos: ${[for (final x in suprimentos) '${x.emoji} ${s.progresso.suprimentos[x.materia] ?? 0}'].join('  ')}'),
      ]),
      const SizedBox(height: 8),
      Botao3D(
        texto: '🗑️ REMOVER CRIANÇA',
        cor: Cores.errado,
        corSombra: const Color(0xFFD63434),
        onPressed: () async {
          final ok = await showDialog<bool>(
            context: context,
            builder: (c) => AlertDialog(
              title: Text('Remover ${s.perfil.nome}?'),
              content: const Text('Todo o progresso, o horário e as provas desta criança serão apagados.'),
              actions: [
                TextButton(onPressed: () => Navigator.pop(c, false), child: const Text('Cancelar')),
                TextButton(onPressed: () => Navigator.pop(c, true), child: const Text('Remover')),
              ],
            ),
          );
          if (ok != true) return;
          await ref.read(acoesProvider).removerPerfil(s.perfil.id);
          if (context.mounted) context.go('/pais');
        },
      ),
    ]);
  }
}

