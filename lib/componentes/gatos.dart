import 'package:flutter_svg/flutter_svg.dart';
import 'package:material_ui/material_ui.dart';

/// A tripulação felina da Galáxia do Saber, usada como avatar.
class Gato {
  final String id;
  final String nome;
  final String titulo;
  final String descricao;
  final String base;
  final String olho;
  final String? listras;
  final String? orelhaDireita;
  final String? mancha;
  final bool branco;
  final bool escuro;

  const Gato({
    required this.id,
    required this.nome,
    required this.titulo,
    required this.descricao,
    required this.base,
    required this.olho,
    this.listras,
    this.orelhaDireita,
    this.mancha,
    this.branco = false,
    this.escuro = false,
  });
}

const gatos = [
  Gato(
      id: 'jojo',
      nome: 'Jojô Melina',
      titulo: 'Capitã',
      descricao: 'Deusa soberana dos gatos',
      base: '#8E9196',
      listras: '#2E2F33',
      branco: true,
      olho: '#B9D84A',
      orelhaDireita: '#1E1E20',
      mancha: '<path d="M58 25 Q80 20 87 46 Q74 41 61 37 Z" fill="#1E1E20"/>'),
  Gato(
      id: 'nala',
      nome: 'Nala Pudinzinha',
      titulo: 'Capitã',
      descricao: 'A hacker mais rápida do universo',
      base: '#F2A03D',
      listras: '#D9781A',
      branco: true,
      olho: '#7CC36B'),
  Gato(
      id: 'shanti',
      nome: 'Shanti-Lee',
      titulo: 'Capitã',
      descricao: 'Ardilosamente fofa',
      base: '#A3A8AE',
      branco: true,
      olho: '#E3B23C'),
  Gato(
      id: 'luna',
      nome: 'Luna',
      titulo: 'Capitã',
      descricao: 'Rainha dos rebeldes libertários',
      base: '#26262B',
      escuro: true,
      olho: '#3DDC6E'),
  Gato(
      id: 'baguera',
      nome: 'Baguera',
      titulo: 'Capitão',
      descricao: 'Deus soberano do miado',
      base: '#17171B',
      escuro: true,
      olho: '#3FA9FF'),
];

Gato gatoPorId(String id) =>
    gatos.firstWhere((g) => g.id == id, orElse: () => gatos.first);

String svgGato(Gato c) {
  final b = StringBuffer(
      '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">');
  b.write('<path d="M15 47 L21 7 L46 30 Z" fill="${c.base}"/>'
      '<path d="M85 47 L79 7 L54 30 Z" fill="${c.orelhaDireita ?? c.base}"/>');
  b.write('<path d="M22 38 L25 17 L38 30 Z" fill="#F4A6B8"/>'
      '<path d="M78 38 L75 17 L62 30 Z" fill="#F4A6B8"/>');
  b.write('<ellipse cx="50" cy="57" rx="38" ry="34" fill="${c.base}"/>');
  if (c.mancha != null) b.write(c.mancha);
  if (c.listras != null) {
    b.write('<path d="M43 27 L45 39 M50 25 L50 39 M57 27 L55 39 M13 55 L24 57 '
        'M13 63 L24 63 M87 55 L76 57 M87 63 L76 63" stroke="${c.listras}" '
        'stroke-width="3.5" stroke-linecap="round"/>');
  }
  if (c.branco) {
    b.write('<path d="M50 36 L41 62 L59 62 Z" fill="#fff"/>'
        '<ellipse cx="50" cy="72" rx="21" ry="15" fill="#fff"/>');
  }
  b.write('<ellipse cx="35" cy="53" rx="8.5" ry="9.5" fill="${c.olho}"/>'
      '<ellipse cx="65" cy="53" rx="8.5" ry="9.5" fill="${c.olho}"/>');
  b.write('<ellipse cx="35" cy="53" rx="2.8" ry="7.2" fill="#111"/>'
      '<ellipse cx="65" cy="53" rx="2.8" ry="7.2" fill="#111"/>'
      '<circle cx="37.6" cy="49.4" r="2.3" fill="#fff"/>'
      '<circle cx="67.6" cy="49.4" r="2.3" fill="#fff"/>');
  b.write('<path d="M45 64 L55 64 L50 70 Z" fill="#F07C98"/>'
      '<path d="M50 70 Q46 76 41 73 M50 70 Q54 76 59 73" '
      'stroke="${c.escuro ? '#9a9a9a' : '#5a4a4a'}" stroke-width="2" '
      'fill="none" stroke-linecap="round"/>');
  b.write('<path d="M30 69 L7 65 M30 73 L7 75 M70 69 L93 65 M70 73 L93 75" '
      'stroke="${c.escuro ? '#d8d8d8' : '#6f6f6f'}" stroke-width="1.6" '
      'stroke-linecap="round"/>');
  b.write('</svg>');
  return b.toString();
}

class AvatarGato extends StatelessWidget {
  final String id;
  final double tamanho;
  const AvatarGato(this.id, {super.key, this.tamanho = 48});

  @override
  Widget build(BuildContext context) {
    final g = gatoPorId(id);
    return Semantics(
      label: g.nome,
      child: SvgPicture.string(svgGato(g), width: tamanho, height: tamanho),
    );
  }
}
