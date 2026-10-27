(() => {
  // Preserve old inbound links without using browser locale to override explicit URLs.
  const legacy = new URLSearchParams(location.search).get('lang');
  if (location.pathname === '/' && (legacy === 'it' || legacy === 'en')) {
    location.replace('/' + legacy + '/' + location.hash);
    return;
  }
  const form = document.getElementById('cform');
  if (!form) return;
  form.addEventListener('submit', (event) => {
    event.preventDefault();
    if (!form.reportValidity()) return;
    const fields = new FormData(form);
    const topic = form.elements.topic.selectedOptions[0].textContent;
    const body = fields.get('message') + '\n\n— ' + fields.get('name') + ' · ' + fields.get('email');
    document.getElementById('fmsg').textContent = document.documentElement.lang === 'it'
      ? 'La richiesta non è ancora inviata. Completa l’invio nella tua app email, oppure scrivi a hello@lytostudio.com.'
      : 'Your enquiry has not been sent yet. Send it in your email app, or write to hello@lytostudio.com.';
    location.href = 'mailto:hello@lytostudio.com?subject=' + encodeURIComponent('Lyto · ' + topic) + '&body=' + encodeURIComponent(body);
  });
})();
