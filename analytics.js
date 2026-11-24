/* 访问统计（GoatCounter，隐私友好：不收集个人信息、不写 Cookie）
 * 后台：https://chenread.goatcounter.com （已注册）
 * 实现：不用官方 gc.zgo.at/count.js —— 该 CDN 域名在国内被 DNS 污染（解析到 Facebook IP），
 *       访客会加载失败。GoatCounter 记账本质就是一次对 /count 的 GET（返回 1x1 GIF），
 *       这里直接发 Image 探针，等价且国内可达。
 */
(function () {
  var CODE = "chenread"; // GoatCounter 站点 code
  if (!CODE || navigator.doNotTrack === "1") return;
  var url = "https://" + CODE + ".goatcounter.com/count" +
    "?p=" + encodeURIComponent(location.pathname) + // 只记路径，不记 sharecode 等查询串
    "&t=" + encodeURIComponent(document.title) +
    "&r=" + encodeURIComponent(document.referrer || "") +
    "&rnd=" + Math.random().toString(36).slice(2);
  new Image().src = url;
})();
