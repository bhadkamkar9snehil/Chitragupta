// XBatch Helpdesk launcher: <script src=".../embed.js" data-user="{XStudioUserID}" defer></script>
(function () {
  var me = document.currentScript;
  var origin = new URL(me.src).origin;
  var user = me.getAttribute("data-user") || "";
  var accent = me.getAttribute("data-accent") || "#c2410c";
  var open = false;
  var frame, button;

  function toggle() {
    open = !open;
    if (!frame) {
      frame = document.createElement("iframe");
      frame.src = origin + "/" + (user && user.indexOf("{") < 0 ? "?user=" + encodeURIComponent(user) : "");
      frame.title = "XBatch Helpdesk";
      frame.allow = "clipboard-write";
      frame.style.cssText = "position:fixed;right:20px;bottom:88px;width:min(420px,calc(100vw - 40px));height:min(680px,calc(100vh - 120px));border:0;border-radius:16px;box-shadow:0 12px 48px rgba(0,0,0,.24);z-index:2147483646;background:#fff;transition:opacity .16s,transform .16s";
      document.body.appendChild(frame);
    }
    frame.style.opacity = open ? "1" : "0";
    frame.style.transform = open ? "none" : "translateY(8px)";
    frame.style.pointerEvents = open ? "auto" : "none";
    button.setAttribute("aria-expanded", String(open));
    button.innerHTML = open ? ICON_CLOSE : ICON_CHAT;
  }

  var ICON_CHAT = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/></svg>';
  var ICON_CLOSE = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>';

  function mount() {
    button = document.createElement("button");
    button.type = "button";
    button.setAttribute("aria-label", "Open XBatch Helpdesk");
    button.setAttribute("aria-expanded", "false");
    button.style.cssText = "position:fixed;right:20px;bottom:20px;width:56px;height:56px;border-radius:50%;border:0;cursor:pointer;display:grid;place-items:center;z-index:2147483647;box-shadow:0 6px 20px rgba(0,0,0,.25);background:" + accent;
    button.innerHTML = ICON_CHAT;
    button.addEventListener("click", toggle);
    document.body.appendChild(button);
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", mount);
  else mount();
})();
