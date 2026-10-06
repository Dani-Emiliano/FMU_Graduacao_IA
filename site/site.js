// Microinterações do site: tema, revelar ao rolar, spotlight, barra de leitura e sumário ativo.
(function () {
  var raiz = document.documentElement;

  // ---- Tema claro/escuro ----
  var btn = document.querySelector('.btn-tema');
  if (btn) {
    btn.addEventListener('click', function () {
      var novo = raiz.getAttribute('data-theme') === 'claro' ? 'escuro' : 'claro';
      raiz.setAttribute('data-theme', novo);
      try { localStorage.setItem('tema', novo); } catch (e) {}
    });
  }

  var reduz = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ---- Revelar ao rolar ----
  if ('IntersectionObserver' in window && !reduz) {
    var alvos = document.querySelectorAll('.card, .aula, .painel, .arquivo, .stat, .etapa, .galeria a, .ficha div');
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('visto'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -30px 0px' });
    alvos.forEach(function (el, i) {
      el.classList.add('revela');
      el.style.transitionDelay = (i % 6) * 55 + 'ms';
      io.observe(el);
    });
  }

  // ---- Spotlight que segue o mouse ----
  document.querySelectorAll('a.card, .spot').forEach(function (el) {
    el.addEventListener('pointermove', function (ev) {
      var r = el.getBoundingClientRect();
      el.style.setProperty('--mx', (ev.clientX - r.left) + 'px');
      el.style.setProperty('--my', (ev.clientY - r.top) + 'px');
    });
  });

  // ---- Barra de leitura ----
  var barra = document.querySelector('.barra-leitura');
  if (barra) {
    var att = function () {
      var max = raiz.scrollHeight - raiz.clientHeight;
      barra.style.width = (max > 0 ? (raiz.scrollTop / max) * 100 : 0) + '%';
    };
    document.addEventListener('scroll', att, { passive: true });
    att();
  }

  // ---- Sumário: destaca a seção atual ----
  var links = document.querySelectorAll('.sumario a[href^="#"]');
  if (links.length && 'IntersectionObserver' in window) {
    var mapa = {};
    links.forEach(function (a) { mapa[decodeURIComponent(a.getAttribute('href').slice(1))] = a; });
    var atual = null;
    var spy = new IntersectionObserver(function (es) {
      es.forEach(function (e) {
        if (e.isIntersecting) {
          var a = mapa[e.target.id];
          if (a && a !== atual) {
            if (atual) atual.classList.remove('atual');
            a.classList.add('atual');
            atual = a;
          }
        }
      });
    }, { rootMargin: '-90px 0px -70% 0px' });
    Object.keys(mapa).forEach(function (id) {
      var h = document.getElementById(id);
      if (h) spy.observe(h);
    });
  }
})();
