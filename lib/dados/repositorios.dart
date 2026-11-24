import 'dart:convert';

import 'package:flutter/services.dart' show AssetBundle;
import 'package:shared_preferences/shared_preferences.dart';

import '../modelos/conteudo.dart';
import '../modelos/perfil.dart';
import '../modelos/progresso.dart';
import '../modelos/rotina.dart';

/// Camada de dados. As telas só conhecem estas interfaces: trocar o
/// armazenamento local por nuvem no futuro é escrever outra implementação.

abstract class RepositorioPerfis {
  Future<List<PerfilCrianca>> listar();
  Future<void> salvar(PerfilCrianca perfil);
  Future<void> remover(String id);
}

abstract class RepositorioProgresso {
  Future<Progresso> carregar(String perfilId);
  Future<void> salvar(String perfilId, Progresso progresso);
}

/// Horário das aulas e provas de cada criança, e o PIN da área dos pais.
abstract class RepositorioPais {
  Future<Rotina> rotina(String perfilId);
  Future<void> salvarRotina(String perfilId, Rotina rotina);
  Future<String?> pin();
  Future<void> salvarPin(String? pin);
}

abstract class RepositorioConteudo {
  Future<ConteudoAno> ano(int ano);
  Future<List<Nivel>> niveis();
}

class RepositorioPerfisLocal implements RepositorioPerfis {
  static const _chave = 'perfis';
  final SharedPreferences prefs;
  RepositorioPerfisLocal(this.prefs);

  @override
  Future<List<PerfilCrianca>> listar() async {
    final t = prefs.getString(_chave);
    if (t == null) return [];
    return (jsonDecode(t) as List)
        .map((p) => PerfilCrianca.fromJson(p as Map<String, dynamic>))
        .toList();
  }

  @override
  Future<void> salvar(PerfilCrianca perfil) async {
    final lista = await listar();
    final i = lista.indexWhere((p) => p.id == perfil.id);
    if (i >= 0) {
      lista[i] = perfil;
    } else {
      lista.add(perfil);
    }
    await prefs.setString(
        _chave, jsonEncode(lista.map((p) => p.toJson()).toList()));
  }

  @override
  Future<void> remover(String id) async {
    final lista = await listar()
      ..removeWhere((p) => p.id == id);
    await prefs.setString(
        _chave, jsonEncode(lista.map((p) => p.toJson()).toList()));
    await prefs.remove('progresso_$id');
    await prefs.remove('rotina_$id');
  }
}

class RepositorioProgressoLocal implements RepositorioProgresso {
  final SharedPreferences prefs;
  RepositorioProgressoLocal(this.prefs);

  @override
  Future<Progresso> carregar(String perfilId) async {
    final t = prefs.getString('progresso_$perfilId');
    if (t == null) return Progresso.vazio;
    return Progresso.fromJson(jsonDecode(t) as Map<String, dynamic>);
  }

  @override
  Future<void> salvar(String perfilId, Progresso progresso) =>
      prefs.setString('progresso_$perfilId', jsonEncode(progresso.toJson()));
}

class RepositorioPaisLocal implements RepositorioPais {
  final SharedPreferences prefs;
  RepositorioPaisLocal(this.prefs);

  @override
  Future<Rotina> rotina(String perfilId) async {
    final t = prefs.getString('rotina_$perfilId');
    if (t == null) return Rotina.vazia;
    return Rotina.fromJson(jsonDecode(t) as Map<String, dynamic>);
  }

  @override
  Future<void> salvarRotina(String perfilId, Rotina rotina) =>
      prefs.setString('rotina_$perfilId', jsonEncode(rotina.toJson()));

  @override
  Future<String?> pin() async => prefs.getString('pais_pin');

  @override
  Future<void> salvarPin(String? pin) async {
    if (pin == null) {
      await prefs.remove('pais_pin');
    } else {
      await prefs.setString('pais_pin', pin);
    }
  }
}

class RepositorioConteudoAssets implements RepositorioConteudo {
  final AssetBundle bundle;
  final _anos = <int, ConteudoAno>{};
  List<Nivel>? _niveis;

  RepositorioConteudoAssets(this.bundle);

  @override
  Future<ConteudoAno> ano(int ano) async {
    final c = _anos[ano];
    if (c != null) return c;
    final t = await bundle.loadString('assets/conteudo/ano_$ano.json');
    return _anos[ano] =
        ConteudoAno.fromJson(jsonDecode(t) as Map<String, dynamic>);
  }

  @override
  Future<List<Nivel>> niveis() async {
    if (_niveis != null) return _niveis!;
    final t = await bundle.loadString('assets/conteudo/niveis.json');
    return _niveis = (jsonDecode(t) as List)
        .map((n) => Nivel.fromJson(n as Map<String, dynamic>))
        .toList();
  }
}
