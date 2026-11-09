const menu = document.querySelector('.menu-toggle');
const nav = document.querySelector('#navigation');
menu.addEventListener('click', () => {
  const expanded = menu.getAttribute('aria-expanded') === 'true';
  menu.setAttribute('aria-expanded', String(!expanded));
  nav.classList.toggle('open', !expanded);
});
nav.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
  nav.classList.remove('open');
  menu.setAttribute('aria-expanded', 'false');
}));
document.addEventListener('keydown', event => {
  if (event.key === 'Escape') {
    nav.classList.remove('open');
    menu.setAttribute('aria-expanded', 'false');
  }
});
const filters = document.querySelectorAll('[data-filter]');
filters.forEach(button => button.addEventListener('click', () => {
  filters.forEach(item => item.setAttribute('aria-pressed', String(item === button)));
  let count = 0;
  document.querySelectorAll('[data-publication]').forEach(item => {
    item.hidden = button.dataset.filter !== 'all' && item.dataset.publication !== button.dataset.filter;
    if (!item.hidden) count++;
  });
  document.querySelector('#filter-status').textContent = count + (count === 1 ? ' publication shown' : ' publications shown');
}));
const citationDialog = document.querySelector('#citation-dialog');
document.querySelectorAll('[data-cite]').forEach(button => button.addEventListener('click', () => {
  document.querySelector('#citation-text').textContent = document.getElementById(button.dataset.cite).content.textContent;
  document.querySelector('#copy-citation').textContent = 'Copy BibTeX';
  citationDialog.showModal();
}));
document.querySelector('#copy-citation').addEventListener('click', async event => {
  try {
    await navigator.clipboard.writeText(document.querySelector('#citation-text').textContent);
    event.target.textContent = 'Copied';
  } catch {
    event.target.textContent = 'Select and copy the text above';
  }
});
document.querySelectorAll('[data-close]').forEach(button => button.addEventListener('click', () => button.closest('dialog').close()));
document.querySelectorAll('dialog').forEach(dialog => dialog.addEventListener('click', event => {
  if (event.target === dialog) {
    const rect = dialog.getBoundingClientRect();
    if (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom) dialog.close();
  }
}));
const share = document.querySelector('#share-button');
if (share) share.addEventListener('click', () => document.querySelector('#share-dialog').showModal());
