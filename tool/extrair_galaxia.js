// Extrai o conteúdo da Galáxia do Saber (artifact HTML) para o JSON do app.
// Uso: node extrair.js <index.html> <saida.json>
const fs = require('fs'), vm = require('vm');
const html = fs.readFileSync(process.argv[2], 'utf8');
let js = html.slice(html.indexOf('<script>') + 8, html.lastIndexOf('</script>'));
js = js.slice(0, js.indexOf('/* ================= ESTADO'));
const noop = () => {};
const ctx = { console, Math, String, Number, Array, Object, JSON, Date,
  document: { getElementById: () => null, addEventListener: noop, querySelectorAll: () => [] },
  window: { addEventListener: noop }, navigator: {}, location: { protocol: 'file:', hostname: '' },
  setTimeout: noop, setInterval: noop, clearInterval: noop };
vm.createContext(ctx);
js = js.replace(/^const /gm, 'var ').replace(/^let /gm, 'var ');
const corte = js.indexOf('/* ---------- geradores de perguntas');
const parteA = js.slice(0, corte);
const parteB = js.slice(corte).replace('function rose(', 'function __rose_orig(').replace('function clock(', 'function __clock_orig(');
vm.runInContext(parteA, ctx);

// ---- substitui os desenhos por marcadores ----
const REG = [];
const tok = o => { REG.push(o); return `⟦V${REG.length - 1}⟧`; };
vm.runInContext(`
  var __svg = {bar, pizza, grid100, numline, rose: (...a)=>__rose_orig(...a), clock: (...a)=>__clock_orig(...a)};
  F = (n,d) => '⟦F:'+n+'/'+d+'⟧';
  bar = (...a) => __tok({tipo:'svg', svg: __svg.bar(...a)});
  pizza = (...a) => __tok({tipo:'svg', svg: __svg.pizza(...a)});
  grid100 = (...a) => __tok({tipo:'svg', svg: __svg.grid100(...a)});
  numline = (...a) => __tok({tipo:'svg', svg: __svg.numline(...a)});
  rose = (...a) => __tok({tipo:'svg', svg: __svg.rose(...a)});
  clock = (...a) => __tok({tipo:'svg', svg: __svg.clock(...a)});
  wholes = (a,k) => __tok({tipo:'svgs', svgs: [...Array(a).fill(0).map(()=>__svg.bar(10,10,{w:140,h:28,c:'#2FB36D'})), __svg.bar(10,k,{w:140,h:28,c:'#2FB36D'})]});
  cmp = (list,c='#FF8A3D') => __tok({tipo:'comparar', itens: list.map(([n,d])=>({n,d,svg:__svg.bar(d,n,{w:220,h:36,c})}))});
  groups = (n,size) => __tok({tipo:'grupos', n, tamanho:size});
  tab = (d,n) => __tok({tipo:'tabuada', d, n});
  cash = list => __tok({tipo:'dinheiro', valores:list});
  pv = nums => __tok({tipo:'valorPosicional', numeros:nums});
  NOME = () => '{nome}';
  function genEx(gid,t){const q=GEN[gid].f(t);return {t:'mc',q:q.q,v:q.vis||'',o:[q.ok,...q.opts.filter(x=>x!==q.ok)],fixed:q.order?q.opts:null,e:q.exp,h:q.hint,hv:q.hv||''}}
`, Object.assign(ctx, { __tok: tok }));
vm.runInContext(parteB, ctx);

// Textos/visuais que já viraram HTML fixo (POEM, TXT, BIGE, emo, inv) são tratados no conversor.
function visuais(s) {
  // separa marcadores de visual e blocos HTML especiais
  const out = [];
  if (!s) return out;
  s = String(s);
  const re = /⟦V(\d+)⟧|<div class="(emo|inv|poem|txtbox)"[^>]*?(?:font-size:(\d+)px)?[^>]*>([\s\S]*?)<\/div>/g;
  let m;
  while ((m = re.exec(s))) {
    if (m[1] !== undefined) out.push(REG[+m[1]]);
    else if (m[2] === 'emo') out.push({ tipo: 'emoji', texto: m[4], tamanho: m[3] ? +m[3] : 48 });
    else out.push({ tipo: 'caixa', estilo: { inv: 'destaque', poem: 'poema', txtbox: 'texto' }[m[2]], texto: texto(m[4]) });
  }
  return out;
}
function texto(s) {
  if (s === undefined || s === null) return s;
  s = String(s)
    .replace(/⟦V\d+⟧/g, '')
    .replace(/<div class="(emo|inv|poem|txtbox)"[\s\S]*?<\/div>/g, '')
    .replace(/<br\s*\/?>/g, '\n')
    .replace(/<\/?b>/g, '**')
    .replace(/<span class="blank"[^>]*>.*?<\/span>/g, '___')
    .replace(/<[^>]+>/g, '')
    .replace(/&nbsp;/g, ' ').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&')
    .replace(/⟦F:(\d+)\/(\d+)⟧/g, '[[$1/$2]]');
  return s.trim();
}
// texto que pode conter visual embutido: devolve [texto, visuais]
const tv = s => [texto(s), visuais(s)];

function exercicio(ex) {
  const e = ex.e ? texto(ex.e) : undefined;
  switch (ex.t) {
    case 'mc': {
      const [q, vq] = tv(ex.q);
      const vis = [...vq, ...visuais(ex.v)];
      const r = { tipo: 'escolha', pergunta: q, opcoes: (ex.fixed || ex.o).map(texto) };
      r.correta = ex.fixed ? ex.fixed.indexOf(ex.o[0]) : 0;
      r.embaralhar = !ex.fixed;
      if (vis.length) r.visuais = vis;
      if (ex.h) { r.dica = texto(ex.h); const hv = visuais(ex.hv); if (hv.length) r.dicaVisuais = hv; }
      if (e) r.explicacao = e;
      return r;
    }
    case 'tf': return { tipo: 'verdadeiroFalso', pergunta: texto(ex.q), resposta: ex.a, explicacao: e };
    case 'fill': return { tipo: 'completar', pergunta: texto(ex.q), opcoes: ex.o.map(texto), explicacao: e };
    case 'ord': return { tipo: 'ordenar', pergunta: texto(ex.q), itens: ex.o.map(texto), explicacao: e };
    case 'mat': return { tipo: 'ligar', pergunta: texto(ex.q), pares: ex.p.map(p => p.map(texto)) };
    case 'srt': return { tipo: 'separar', pergunta: texto(ex.q), grupos: ex.g.map(texto), itens: ex.it.map(([a, b]) => ({ texto: texto(a), grupo: b })), explicacao: e };
  }
  throw new Error('tipo ' + ex.t);
}

const VARIANTES = 5; // por modelo de pergunta gerada
function gerados(gen, big) {
  vm.runInContext(`DF = () => ({big: ${big ? 1 : 0}})`, ctx);
  const G = ctx.GEN[gen], out = [], vistos = new Set();
  for (let t = 0; t < G.n; t++) {
    let tent = 0, n = 0;
    while (n < VARIANTES && tent++ < 40) {
      const ex = exercicio(ctx.genEx(gen, t));
      const k = ex.pergunta + JSON.stringify(ex.visuais || '') + ex.opcoes.join();
      if (vistos.has(k)) continue;
      vistos.add(k); out.push(Object.assign(ex, { modelo: t })); n++;
    }
  }
  return out;
}

const W = ctx.WORLDS;
const planetas = W.map(w => ({
  id: w.id,
  disciplina: w.name,
  nomeCurto: w.short,
  nome: w.world,
  emoji: w.e,
  cor: w.c, corEscura: w.cd, corClara: w.sl,
  chefao: { emoji: w.boss[0], nome: w.boss[1] },
  decoracao: w.deco,
  setores: w.units.map((u, ui) => ({
    id: `${w.id}-s${ui + 1}`,
    titulo: u.title,
    subtitulo: u.sub,
    missoes: u.lessons.map(l => {
      const m = { id: l.id, titulo: l.name, emoji: l.e,
        briefing: l.learn.map(c => {
          const [t, v] = tv(c[1]);
          const vis = [...v, ...(c[2] ? visuais(c[2]()) : [])];
          return Object.assign({ emoji: c[0], texto: t }, vis.length ? { visuais: vis } : {});
        }) };
      if (l.gen) { m.geradas = true; m.exercicios = gerados(l.gen, false); m.exerciciosDesafio = gerados(l.gen, true); }
      else m.exercicios = l.ex.map(exercicio);
      return m;
    }),
  })),
}));

const saida = {
  origem: 'Galáxia do Saber (material interativo do Bernardo), IV Unidade do 4º ano',
  niveis: ctx.DIFFS.map(d => ({ id: d.id, nome: d.name, emoji: d.e, cor: d.dc, descricao: d.desc,
    perguntasMissao: d.n, perguntasRevisao: d.nr, perguntasChefao: d.nb, opcoes: d.opts, itensSeparar: d.items,
    dicas: d.hint, tempoSegundos: d.timer, multiplicador: d.mult, desafio: !!d.big })),
  planetas,
};
fs.writeFileSync(process.argv[3], JSON.stringify(saida, null, 1));
const nm = planetas.reduce((s, p) => s + p.setores.reduce((a, u) => a + u.missoes.length, 0), 0);
const ne = planetas.reduce((s, p) => s + p.setores.reduce((a, u) => a + u.missoes.reduce((b, m) => b + m.exercicios.length, 0), 0), 0);
console.log('planetas', planetas.length, 'missões', nm, 'exercícios', ne);
