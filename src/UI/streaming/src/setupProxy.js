const createProxyMiddleware = require("http-proxy-middleware");

module.exports = function (app) {
  app.use(
    "/reqforward",
    createProxyMiddleware({
      target: "http://adc.core:60008",
      changeOrigin: true,
    })
  );
  app.use(
    "/videos",
    createProxyMiddleware({
      target: "http://localhost/70005",
      changeOrigin: true,
    })
  );
};
