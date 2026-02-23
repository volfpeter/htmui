from htmy import SafeStr

init_on_htmx_history_restore = SafeStr(
    """<script>
document.addEventListener('htmx:historyRestore', () => {
  if (window.basecoat) window.basecoat.initAll();
});
</script>"""
)
