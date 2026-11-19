import 'dart:convert';

import 'package:flutter/services.dart' show AssetBundle;
import 'package:shared_preferences/shared_preferences.dart';

import '../models/curriculo.dart';
import '../models/perfil.dart';
import '../models/progresso.dart';

/// Camada de dados. As telas só conhecem estas interfaces, então trocar
/// o armazenamento local por nuvem (Firebase, Supabase...) no futuro
/// significa escrever uma nova implementação, sem mexer na interface.

abstract class RepositorioPerfis {
  Future<List<PerfilCrianca>> listar();
  Future<void> salvar(PerfilCrianca perfil);
  Future<void> remover(String id);
}

abstract class RepositorioProgresso {
  Future<Progresso> carregar(String perfilId);
  Future<void> salvar(String perfilId, Progresso progresso);
}

abstract class RepositorioCurriculo {
  Future<TrilhaAno> trilha(int ano);
}

// ---------------------------------------------------------------------------
// Implementações locais (versão offline).

class RepositorioPerfisLocal implements RepositorioPerfis {
  static const _chave = 'perfis';
  final SharedPreferences prefs;

  RepositorioPerfisLocal(this.prefs);

  @override
  Future<List<PerfilCrianca>> listar() async {
    final texto = prefs.getString(_chave);
    if (texto == null) return [];
    return (jsonDecode(texto) as List)
        .map((p) => PerfilCrianca.fromJson(p as Map<String, dynamic>))
        .toList();
  }

  Future<void> _gravar(List<PerfilCrianca> perfis) => prefs.setString(
      _chave, jsonEncode(perfis.map((p) => p.toJson()).toList()));

  @override
  Future<void> salvar(PerfilCrianca perfil) async {
    final perfis = await listar();
    final i = perfis.indexWhere((p) => p.id == perfil.id);
    if (i >= 0) {
      perfis[i] = perfil;
    } else {
      perfis.add(perfil);
    }
    await _gravar(perfis);
  }

  @override
  Future<void> remover(String id) async {
    final perfis = await listar()
      ..removeWhere((p) => p.id == id);
    await _gravar(perfis);
    await prefs.remove('progresso_$id');
  }
}

class RepositorioProgressoLocal implements RepositorioProgresso {
  final SharedPreferences prefs;

  RepositorioProgressoLocal(this.prefs);

  @override
  Future<Progresso> carregar(String perfilId) async {
    final texto = prefs.getString('progresso_$perfilId');
    if (texto == null) return Progresso.vazio;
    return Progresso.fromJson(jsonDecode(texto) as Map<String, dynamic>);
  }

  @override
  Future<void> salvar(String perfilId, Progresso progresso) =>
      prefs.setString('progresso_$perfilId', jsonEncode(progresso.toJson()));
}

class RepositorioCurriculoAssets implements RepositorioCurriculo {
  final AssetBundle bundle;
  final _cache = <int, TrilhaAno>{};

  RepositorioCurriculoAssets(this.bundle);

  @override
  Future<TrilhaAno> trilha(int ano) async {
    final emCache = _cache[ano];
    if (emCache != null) return emCache;
    final texto = await bundle.loadString('assets/curriculo/ano_$ano.json');
    final trilha =
        TrilhaAno.fromJson(jsonDecode(texto) as Map<String, dynamic>);
    return _cache[ano] = trilha;
  }
}
