import 'dart:async';
import 'dart:math';

import 'package:material_ui/material_ui.dart';

import '../modelos/conteudo.dart';
import 'tema.dart';
import 'texto_rico.dart';
import 'visuais.dart';

/// Resultado de uma resposta, para o painel de retorno.
class Resposta {
  final bool certa;
  final String? respostaCerta;
  final String? explicacao;
  final String? nota;

  /// Em "ligar" e "separar", certa = terminou; semErros = acertou de primeira.
  final bool semErros;

  const Resposta(this.certa,
      {this.respostaCerta, this.explicacao, this.nota, this.semErros = true});
}

String respostaCertaDe(Exercicio e) => switch (e) {
      Escolha() => e.respostaCerta,
      VerdadeiroFalso() => e.resposta ? 'Verdadeiro' : 'Falso',
      Completar() => e.opcoes.first,
      Ordenar() => e.itens.join(' → '),
      _ => '',
    };

/// Mostra o exercício certo para o tipo.
class VistaExercicio extends StatelessWidget {
  final Exercicio exercicio;
  final String nome;
  final Widget mascote;
  final bool bloqueado;
  final Random aleatorio;
  final void Function(Resposta) onResposta;
  final VoidCallback onOuvir;
  final void Function(bool acertou)? onToque;

  const VistaExercicio({
    super.key,
    required this.exercicio,
    required this.nome,
    required this.mascote,
    required this.bloqueado,
    required this.aleatorio,
    required this.onResposta,
    required this.onOuvir,
    this.onToque,
  });

  @override
  Widget build(BuildContext context) {
    final e = exercicio;
    final pergunta = _Pergunta(
      texto: e is Completar ? 'Complete a frase:' : e.pergunta,
      nome: nome,
      mascote: mascote,
      onOuvir: onOuvir,
    );
    return switch (e) {
      Escolha() => _VistaEscolha(e, pergunta, nome, bloqueado, aleatorio, onResposta),
      VerdadeiroFalso() => _VistaVF(e, pergunta, bloqueado, onResposta),
      Completar() => _VistaCompletar(e, pergunta, nome, bloqueado, aleatorio, onResposta),
      Ordenar() => _VistaOrdenar(e, pergunta, nome, bloqueado, aleatorio, onResposta),
      Ligar() => _VistaLigar(e, pergunta, nome, aleatorio, onResposta, onToque),
      Separar() => _VistaSeparar(e, pergunta, nome, aleatorio, onResposta, onToque),
    };
  }
}

class _Pergunta extends StatelessWidget {
  final String texto;
  final String nome;
  final Widget mascote;
  final VoidCallback onOuvir;
  const _Pergunta(
      {required this.texto, required this.nome, required this.mascote, required this.onOuvir});

  @override
  Widget build(BuildContext context) {
    return Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
      mascote,
      const SizedBox(width: 10),
      Expanded(
        child: TextoRico(texto,
            nome: nome,
            estilo: const TextStyle(fontSize: 22, fontWeight: FontWeight.w900, height: 1.35)),
      ),
      const SizedBox(width: 6),
      _BotaoPequeno(texto: '🔊', rotulo: 'Ouvir a pergunta', onTap: onOuvir),
    ]);
  }
}

class _BotaoPequeno extends StatelessWidget {
  final String texto;
  final String rotulo;
  final VoidCallback onTap;
  const _BotaoPequeno({required this.texto, required this.rotulo, required this.onTap});

  @override
  Widget build(BuildContext context) => Semantics(
        button: true,
        label: rotulo,
        child: GestureDetector(
          onTap: onTap,
          child: Container(
            padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
            decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.circular(12),
              border: Border.all(color: Cores.linha, width: 2),
            ),
            child: Text(texto, style: const TextStyle(fontSize: 20)),
          ),
        ),
      );
}

enum EstadoOpcao { normal, escolhida, certa, errada, sumida }

/// Cartão de opção (resposta, chip, par...).
class Opcao extends StatelessWidget {
  final String texto;
  final String nome;
  final EstadoOpcao estado;
  final VoidCallback? onTap;
  final bool centro;
  final double fonte;
  final double alturaMin;

  const Opcao({
    super.key,
    required this.texto,
    required this.nome,
    required this.estado,
    this.onTap,
    this.centro = false,
    this.fonte = 19,
    this.alturaMin = 0,
  });

  @override
  Widget build(BuildContext context) {
    final (borda, fundo, cor) = switch (estado) {
      EstadoOpcao.escolhida => (const Color(0xFF84D8FF), const Color(0xFFDDF4FF), const Color(0xFF1899D6)),
      EstadoOpcao.certa => (const Color(0xFF3DBE5A), Cores.certoClaro, const Color(0xFF2A8A3E)),
      EstadoOpcao.errada => (Cores.errado, Cores.erradoClaro, const Color(0xFFC92B2B)),
      _ => (Cores.linha, Colors.white, Cores.tinta),
    };
    return AnimatedOpacity(
      duration: const Duration(milliseconds: 300),
      opacity: estado == EstadoOpcao.sumida ? 0.35 : 1,
      child: Semantics(
        button: true,
        selected: estado == EstadoOpcao.escolhida,
        child: GestureDetector(
          onTap: estado == EstadoOpcao.sumida ? null : onTap,
          child: AnimatedContainer(
            duration: const Duration(milliseconds: 150),
            constraints: BoxConstraints(minHeight: alturaMin),
            padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 13),
            alignment: centro ? Alignment.center : Alignment.centerLeft,
            decoration: BoxDecoration(
              color: fundo,
              borderRadius: BorderRadius.circular(16),
              border: Border.all(color: borda, width: 2),
              boxShadow: estado == EstadoOpcao.sumida
                  ? null
                  : [BoxShadow(color: borda, offset: const Offset(0, 4))],
            ),
            child: TextoRico(texto,
                nome: nome,
                alinhamento: centro ? TextAlign.center : TextAlign.start,
                estilo: TextStyle(
                    fontSize: fonte, fontWeight: FontWeight.w800, color: cor, height: 1.3)),
          ),
        ),
      ),
    );
  }
}

String _semMarcas(String s) =>
    s.replaceAll('**', '').replaceAllMapped(RegExp(r'\[\[(\d+)/(\d+)\]\]'), (m) => '${m[1]}/${m[2]}');

// ---------------------------------------------------------------------------

class _VistaEscolha extends StatefulWidget {
  final Escolha e;
  final Widget pergunta;
  final String nome;
  final bool bloqueado;
  final Random rnd;
  final void Function(Resposta) onResposta;
  const _VistaEscolha(this.e, this.pergunta, this.nome, this.bloqueado, this.rnd, this.onResposta);

  @override
  State<_VistaEscolha> createState() => _VistaEscolhaState();
}

class _VistaEscolhaState extends State<_VistaEscolha> {
  late final List<int> _ordem;
  int? _sel;
  bool _verificado = false;
  bool _dica = false;

  @override
  void initState() {
    super.initState();
    _ordem = [for (var i = 0; i < widget.e.opcoes.length; i++) i];
    if (widget.e.embaralhar) _ordem.shuffle(widget.rnd);
  }

  @override
  Widget build(BuildContext context) {
    final e = widget.e;
    final curtas = e.opcoes.every((o) => _semMarcas(o).length <= 12);
    final travado = _verificado || widget.bloqueado;
    EstadoOpcao estado(int i) {
      if (_verificado) {
        if (i == e.correta) return EstadoOpcao.certa;
        if (i == _sel) return EstadoOpcao.errada;
        return EstadoOpcao.normal;
      }
      return i == _sel ? EstadoOpcao.escolhida : EstadoOpcao.normal;
    }

    final opcoes = [
      for (final i in _ordem)
        Opcao(
          key: ValueKey('opcao$i'),
          texto: e.opcoes[i],
          nome: widget.nome,
          estado: estado(i),
          centro: curtas,
          fonte: curtas ? 22 : 19,
          alturaMin: curtas ? 66 : 0,
          onTap: travado ? null : () => setState(() => _sel = i),
        ),
    ];
    return Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
      widget.pergunta,
      Visuais(e.visuais, nome: widget.nome),
      const SizedBox(height: 16),
      if (curtas)
        GridView.count(
          crossAxisCount: 2,
          shrinkWrap: true,
          physics: const NeverScrollableScrollPhysics(),
          mainAxisSpacing: 12,
          crossAxisSpacing: 12,
          childAspectRatio: 2.2,
          children: opcoes,
        )
      else
        for (final o in opcoes) Padding(padding: const EdgeInsets.only(bottom: 12), child: o),
      if (e.dica != null && !_dica && !travado)
        Align(
          alignment: Alignment.centerLeft,
          child: TextButton(
            style: TextButton.styleFrom(
              backgroundColor: const Color(0xFFFFF4CC),
              foregroundColor: const Color(0xFF7A5A00),
              shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
            ),
            onPressed: () => setState(() => _dica = true),
            child: const Text('💡 Me dá uma dica', style: TextStyle(fontWeight: FontWeight.w900)),
          ),
        ),
      if (_dica)
        Container(
          margin: const EdgeInsets.only(top: 6),
          padding: const EdgeInsets.all(14),
          decoration: BoxDecoration(
              color: const Color(0xFFFFF4CC), borderRadius: BorderRadius.circular(16)),
          child: Column(children: [
            TextoRico('💡 ${e.dica}', nome: widget.nome, estilo: const TextStyle(fontSize: 17, height: 1.45)),
            Visuais(e.dicaVisuais, nome: widget.nome),
          ]),
        ),
      const SizedBox(height: 16),
      if (!travado)
        Botao3D(
          texto: 'VERIFICAR',
          onPressed: _sel == null
              ? null
              : () {
                  setState(() => _verificado = true);
                  widget.onResposta(Resposta(_sel == e.correta,
                      respostaCerta: e.respostaCerta, explicacao: e.explicacao));
                },
        ),
    ]);
  }
}

class _VistaVF extends StatefulWidget {
  final VerdadeiroFalso e;
  final Widget pergunta;
  final bool bloqueado;
  final void Function(Resposta) onResposta;
  const _VistaVF(this.e, this.pergunta, this.bloqueado, this.onResposta);

  @override
  State<_VistaVF> createState() => _VistaVFState();
}

class _VistaVFState extends State<_VistaVF> {
  bool? _sel;
  bool _verificado = false;

  @override
  Widget build(BuildContext context) {
    final travado = _verificado || widget.bloqueado;
    EstadoOpcao estado(bool v) {
      if (_verificado) {
        if (v == widget.e.resposta) return EstadoOpcao.certa;
        if (v == _sel) return EstadoOpcao.errada;
        return EstadoOpcao.normal;
      }
      return v == _sel ? EstadoOpcao.escolhida : EstadoOpcao.normal;
    }

    return Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
      widget.pergunta,
      const SizedBox(height: 22),
      Row(children: [
        for (final v in [true, false]) ...[
          if (!v) const SizedBox(width: 12),
          Expanded(
            child: Opcao(
              texto: v ? '✅ Verdadeiro' : '❌ Falso',
              nome: '',
              estado: estado(v),
              centro: true,
              fonte: 20,
              alturaMin: 80,
              onTap: travado ? null : () => setState(() => _sel = v),
            ),
          ),
        ],
      ]),
      const SizedBox(height: 20),
      if (!travado)
        Botao3D(
          texto: 'VERIFICAR',
          onPressed: _sel == null
              ? null
              : () {
                  setState(() => _verificado = true);
                  widget.onResposta(Resposta(_sel == widget.e.resposta,
                      respostaCerta: respostaCertaDe(widget.e), explicacao: widget.e.explicacao));
                },
        ),
    ]);
  }
}

class _VistaCompletar extends StatefulWidget {
  final Completar e;
  final Widget pergunta;
  final String nome;
  final bool bloqueado;
  final Random rnd;
  final void Function(Resposta) onResposta;
  const _VistaCompletar(this.e, this.pergunta, this.nome, this.bloqueado, this.rnd, this.onResposta);

  @override
  State<_VistaCompletar> createState() => _VistaCompletarState();
}

class _VistaCompletarState extends State<_VistaCompletar> {
  late final List<int> _ordem;
  int? _sel;
  bool _verificado = false;

  @override
  void initState() {
    super.initState();
    _ordem = [for (var i = 0; i < widget.e.opcoes.length; i++) i]..shuffle(widget.rnd);
  }

  @override
  Widget build(BuildContext context) {
    final e = widget.e;
    final travado = _verificado || widget.bloqueado;
    final partes = e.pergunta.split('___');
    final lacuna = _sel == null ? '        ' : e.opcoes[_sel!];
    EstadoOpcao estado(int i) {
      if (_verificado) {
        if (i == 0) return EstadoOpcao.certa;
        if (i == _sel) return EstadoOpcao.errada;
        return EstadoOpcao.normal;
      }
      return i == _sel ? EstadoOpcao.escolhida : EstadoOpcao.normal;
    }

    const estilo = TextStyle(fontSize: 22, height: 1.7, fontWeight: FontWeight.w800, color: Cores.tinta);
    return Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
      widget.pergunta,
      const SizedBox(height: 14),
      Text.rich(TextSpan(style: estilo, children: [
        ...TextoRico.spans(partes.first, widget.nome, estilo),
        if (partes.length > 1) ...[
          TextSpan(
            text: ' $lacuna ',
            style: const TextStyle(
              color: Color(0xFF1899D6),
              decoration: TextDecoration.underline,
              decorationThickness: 2,
            ),
          ),
          ...TextoRico.spans(partes.sublist(1).join('___'), widget.nome, estilo),
        ],
      ])),
      const SizedBox(height: 16),
      Wrap(
        alignment: WrapAlignment.center,
        spacing: 10,
        runSpacing: 10,
        children: [
          for (final i in _ordem)
            Opcao(
              texto: e.opcoes[i],
              nome: widget.nome,
              estado: estado(i),
              centro: true,
              fonte: 18,
              onTap: travado ? null : () => setState(() => _sel = i),
            ),
        ],
      ),
      const SizedBox(height: 20),
      if (!travado)
        Botao3D(
          texto: 'VERIFICAR',
          onPressed: _sel == null
              ? null
              : () {
                  setState(() => _verificado = true);
                  widget.onResposta(Resposta(_sel == 0,
                      respostaCerta: e.opcoes.first, explicacao: e.explicacao));
                },
        ),
    ]);
  }
}

class _VistaOrdenar extends StatefulWidget {
  final Ordenar e;
  final Widget pergunta;
  final String nome;
  final bool bloqueado;
  final Random rnd;
  final void Function(Resposta) onResposta;
  const _VistaOrdenar(this.e, this.pergunta, this.nome, this.bloqueado, this.rnd, this.onResposta);

  @override
  State<_VistaOrdenar> createState() => _VistaOrdenarState();
}

class _VistaOrdenarState extends State<_VistaOrdenar> {
  late final List<int> _banco;
  final _colocados = <int>[];
  bool _verificado = false;

  @override
  void initState() {
    super.initState();
    _banco = [for (var i = 0; i < widget.e.itens.length; i++) i]..shuffle(widget.rnd);
  }

  @override
  Widget build(BuildContext context) {
    final e = widget.e;
    final travado = _verificado || widget.bloqueado;
    return Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
      widget.pergunta,
      Container(
        margin: const EdgeInsets.only(top: 16),
        padding: const EdgeInsets.symmetric(vertical: 12),
        constraints: const BoxConstraints(minHeight: 120),
        decoration: const BoxDecoration(
          border: Border.symmetric(horizontal: BorderSide(color: Cores.linha, width: 2)),
        ),
        child: _colocados.isEmpty
            ? const Padding(
                padding: EdgeInsets.only(top: 30),
                child: Text('Toque nos itens abaixo, na ordem certa 👇',
                    textAlign: TextAlign.center, style: TextStyle(color: Color(0xFFC0C0C0))),
              )
            : Column(children: [
                for (var k = 0; k < _colocados.length; k++)
                  Padding(
                    padding: const EdgeInsets.only(bottom: 8),
                    child: Row(children: [
                      CircleAvatar(
                        radius: 12,
                        backgroundColor: _verificado
                            ? (_colocados[k] == k ? Cores.certo : Cores.errado)
                            : Cores.roxo,
                        child: Text('${k + 1}',
                            style: const TextStyle(fontSize: 13, color: Colors.white)),
                      ),
                      const SizedBox(width: 8),
                      Expanded(
                        child: Opcao(
                          texto: e.itens[_colocados[k]],
                          nome: widget.nome,
                          estado: EstadoOpcao.normal,
                          fonte: 17,
                          onTap: travado ? null : () => setState(() => _colocados.removeAt(k)),
                        ),
                      ),
                    ]),
                  ),
              ]),
      ),
      const SizedBox(height: 14),
      Wrap(
        alignment: WrapAlignment.center,
        spacing: 10,
        runSpacing: 10,
        children: [
          for (final i in _banco)
            Opcao(
              texto: e.itens[i],
              nome: widget.nome,
              estado: _colocados.contains(i) ? EstadoOpcao.sumida : EstadoOpcao.normal,
              fonte: 17,
              onTap: travado || _colocados.contains(i)
                  ? null
                  : () => setState(() => _colocados.add(i)),
            ),
        ],
      ),
      const SizedBox(height: 20),
      if (!travado)
        Botao3D(
          texto: 'VERIFICAR',
          onPressed: _colocados.length != e.itens.length
              ? null
              : () {
                  setState(() => _verificado = true);
                  var ok = true;
                  for (var k = 0; k < _colocados.length; k++) {
                    if (_colocados[k] != k) ok = false;
                  }
                  widget.onResposta(Resposta(ok,
                      respostaCerta: respostaCertaDe(e), explicacao: e.explicacao));
                },
        ),
    ]);
  }
}

class _VistaLigar extends StatefulWidget {
  final Ligar e;
  final Widget pergunta;
  final String nome;
  final Random rnd;
  final void Function(Resposta) onResposta;
  final void Function(bool)? onToque;
  const _VistaLigar(this.e, this.pergunta, this.nome, this.rnd, this.onResposta, this.onToque);

  @override
  State<_VistaLigar> createState() => _VistaLigarState();
}

class _VistaLigarState extends State<_VistaLigar> {
  late final List<int> _esq, _dir;
  int? _l, _r;
  final _feitos = <int>{};
  final _certos = <int>{};
  (int, int)? _erro;
  int _erros = 0;

  @override
  void initState() {
    super.initState();
    final n = widget.e.pares.length;
    _esq = [for (var i = 0; i < n; i++) i]..shuffle(widget.rnd);
    _dir = [for (var i = 0; i < n; i++) i]..shuffle(widget.rnd);
  }

  void _toque(bool esquerda, int i) {
    if (_feitos.contains(i) || _erro != null) return;
    setState(() => esquerda ? _l = i : _r = i);
    if (_l == null || _r == null) return;
    final l = _l!, r = _r!;
    _l = _r = null;
    if (l == r) {
      widget.onToque?.call(true);
      setState(() => _certos.add(l));
      Timer(const Duration(milliseconds: 350), () {
        if (!mounted) return;
        setState(() {
          _certos.remove(l);
          _feitos.add(l);
        });
        if (_feitos.length == widget.e.pares.length) {
          Timer(const Duration(milliseconds: 300), () {
            widget.onResposta(Resposta(true,
                semErros: _erros == 0,
                nota: _erros > 0
                    ? 'Você corrigiu $_erros ${_erros > 1 ? 'erros' : 'erro'} sozinho!'
                    : 'Todos os pares certos de primeira! 🌟'));
          });
        }
      });
    } else {
      widget.onToque?.call(false);
      setState(() {
        _erros++;
        _erro = (l, r);
      });
      Timer(const Duration(milliseconds: 500), () {
        if (mounted) setState(() => _erro = null);
      });
    }
  }

  EstadoOpcao _estado(bool esquerda, int i) {
    if (_feitos.contains(i)) return EstadoOpcao.sumida;
    if (_certos.contains(i)) return EstadoOpcao.certa;
    if (_erro != null && (esquerda ? _erro!.$1 : _erro!.$2) == i) return EstadoOpcao.errada;
    if ((esquerda ? _l : _r) == i) return EstadoOpcao.escolhida;
    return EstadoOpcao.normal;
  }

  @override
  Widget build(BuildContext context) {
    final pares = widget.e.pares;
    return Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
      widget.pergunta,
      const SizedBox(height: 18),
      for (var linha = 0; linha < pares.length; linha++)
        Padding(
          padding: const EdgeInsets.only(bottom: 10),
          child: IntrinsicHeight(
            child: Row(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
              Expanded(
                child: Opcao(
                  texto: pares[_esq[linha]].$1,
                  nome: widget.nome,
                  estado: _estado(true, _esq[linha]),
                  centro: true,
                  fonte: 17,
                  alturaMin: 62,
                  onTap: () => _toque(true, _esq[linha]),
                ),
              ),
              const SizedBox(width: 10),
              Expanded(
                child: Opcao(
                  texto: pares[_dir[linha]].$2,
                  nome: widget.nome,
                  estado: _estado(false, _dir[linha]),
                  centro: true,
                  fonte: 17,
                  alturaMin: 62,
                  onTap: () => _toque(false, _dir[linha]),
                ),
              ),
            ]),
          ),
        ),
    ]);
  }
}

class _VistaSeparar extends StatefulWidget {
  final Separar e;
  final Widget pergunta;
  final String nome;
  final Random rnd;
  final void Function(Resposta) onResposta;
  final void Function(bool)? onToque;
  const _VistaSeparar(this.e, this.pergunta, this.nome, this.rnd, this.onResposta, this.onToque);

  @override
  State<_VistaSeparar> createState() => _VistaSepararState();
}

class _VistaSepararState extends State<_VistaSeparar> {
  late final List<({String texto, int grupo})> _itens;
  int _i = 0;
  int _erros = 0;
  int? _tocado;
  bool _ocupado = false;

  @override
  void initState() {
    super.initState();
    _itens = List.of(widget.e.itens)..shuffle(widget.rnd);
  }

  void _toque(int g) {
    if (_ocupado) return;
    final certo = g == _itens[_i].grupo;
    widget.onToque?.call(certo);
    setState(() {
      _ocupado = true;
      _tocado = g;
      if (!certo) _erros++;
    });
    Timer(Duration(milliseconds: certo ? 550 : 1500), () {
      if (!mounted) return;
      if (_i + 1 < _itens.length) {
        setState(() {
          _i++;
          _tocado = null;
          _ocupado = false;
        });
      } else {
        widget.onResposta(Resposta(true,
            semErros: _erros == 0,
            explicacao: widget.e.explicacao,
            nota: _erros > 0
                ? 'Errou $_erros, mas viu a resposta certa. Continue!'
                : 'Tudo certo de primeira! 🌟'));
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    final item = _itens[_i];
    final acertou = _tocado != null && _tocado == item.grupo;
    final errou = _tocado != null && !acertou;
    return Column(crossAxisAlignment: CrossAxisAlignment.stretch, children: [
      widget.pergunta,
      const SizedBox(height: 20),
      Center(
        child: AnimatedContainer(
          duration: const Duration(milliseconds: 150),
          constraints: const BoxConstraints(maxWidth: 360),
          width: double.infinity,
          padding: const EdgeInsets.all(22),
          decoration: BoxDecoration(
            color: acertou ? Cores.certoClaro : errou ? Cores.erradoClaro : Colors.white,
            borderRadius: BorderRadius.circular(20),
            border: Border.all(
                color: acertou ? Cores.certo : errou ? Cores.errado : Cores.roxo, width: 3),
            boxShadow: const [BoxShadow(color: Cores.roxoEscuro, offset: Offset(0, 5))],
          ),
          child: TextoRico(item.texto,
              nome: widget.nome,
              alinhamento: TextAlign.center,
              estilo: const TextStyle(fontSize: 24, fontWeight: FontWeight.w900)),
        ),
      ),
      const SizedBox(height: 10),
      Text('${_i + 1} de ${_itens.length}',
          textAlign: TextAlign.center, style: const TextStyle(color: Cores.apagado)),
      const SizedBox(height: 18),
      Row(children: [
        for (var g = 0; g < widget.e.grupos.length; g++) ...[
          if (g > 0) const SizedBox(width: 10),
          Expanded(
            child: Opcao(
              texto: widget.e.grupos[g],
              nome: widget.nome,
              estado: _tocado == null
                  ? EstadoOpcao.normal
                  : g == item.grupo
                      ? EstadoOpcao.certa
                      : g == _tocado
                          ? EstadoOpcao.errada
                          : EstadoOpcao.normal,
              centro: true,
              fonte: 17,
              alturaMin: 66,
              onTap: () => _toque(g),
            ),
          ),
        ],
      ]),
    ]);
  }
}
