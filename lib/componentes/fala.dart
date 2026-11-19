import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_tts/flutter_tts.dart';

/// Leitura em voz alta (botão "Ouvir"), em português do Brasil.
class Fala {
  FlutterTts? _tts;

  Future<void> falar(String texto) async {
    try {
      final tts = _tts ??= FlutterTts();
      await tts.setLanguage('pt-BR');
      await tts.setSpeechRate(0.45);
      await tts.stop();
      await tts.speak(texto);
    } catch (_) {
      // Sem voz disponível no aparelho: o botão simplesmente não fala.
    }
  }

  Future<void> parar() async {
    try {
      await _tts?.stop();
    } catch (_) {}
  }
}

final falaProvider = Provider<Fala>((ref) => Fala());
